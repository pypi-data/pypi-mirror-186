from scinode.daemon.base_daemon import BaseDaemon
from scinode.engine import EngineNode, Broker
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from scinode.utils.db import update_one
from scinode.profile.profile import profile_datas
import os
from pathlib import Path
import datetime

home = Path.home()


class ScinodeDaemon(BaseDaemon):
    """Daemon that fetch nodetree from database and call the
    engine to execute it.

    name: str
        Name of the daemon.
    pool: float
        Pool type: ThreadPoolExecutor or ProcessPoolExecutor
    worker: int
        Number of worker. Default 100 for ThreadPoolExecutor.
        4 for ProcessPoolExecutor.
    sleep: float
        Time interval to fetch data. Default 1.0

    """

    def __init__(self, name, pool="thread", worker=0, sleep=None, broker=None):
        self.name = name
        self.sleep = sleep if sleep is not None else self.data["sleep"]
        self.broker = broker if broker is not None else self.data["broker"]
        if pool.upper() == "THREAD":
            # print("Use ThreadPoolExecutor.")
            self.Pool = ThreadPoolExecutor
            self.worker = worker if worker != 0 else 100
        else:
            # print("Use ProcessPoolExecutor.")
            self.Pool = ProcessPoolExecutor
            self.worker = worker if worker != 0 else 4
        logfile = os.path.join(
            home, ".scinode/daemon-{}-{}.log".format(profile_datas["name"], name)
        )
        super().__init__(logfile)

    def run(self):
        """Call engine to submit the job and collect the returned futures."""
        import time
        from scinode.database.client import scinodedb

        self.db = scinodedb
        self.update_data()
        #
        if self.broker:
            init_broker()
        # check the old process
        self.clean_old_process()
        self.futures = {}
        with self.Pool(max_workers=self.worker) as pool:
            step = 0
            while True:
                print("{} {}".format(self.name, step))
                update_one(
                    {"name": self.name, "lastUpdate": datetime.datetime.utcnow()},
                    self.db["daemon"],
                    key="name",
                )
                # --------------------------------------------------
                if self.broker:
                    self.process_broker()
                self.process_node(pool)
                # f.close()
                step += 1
                time.sleep(self.sleep)

    def process_broker(self):
        """Process nodetree"""
        broker = Broker()
        broker.process()
        del broker

    def process_node(self, pool):
        """Process node"""
        # the entrance point is nodetree
        # if a nodetree is paused, all the child nodes will not be look at.
        query = {
            "state": "RUNNING",
            "action": {"$nin": ["NEED_HELP"]},
        }
        ntdatas = list(self.db["nodetree"].find(query, {"_id": 0, "nodes": 1}))
        # print("nodetree: ", ntdatas)
        for ntdata in ntdatas:
            for name, ndata in ntdata["nodes"].items():
                # print("node: ", ndata)
                # the entrance point is nodetree
                # if a nodetree is paused, all the child nodes will not be look at.
                if (
                    ndata["node_type"] in ["REF", "COPY"]
                    or ndata["state"] not in ["READY", "RUNNING"]
                    or ndata["action"] not in ["LAUNCH", "GATHER", "CANCEL"]
                    or ndata["daemon"] != self.name
                ):
                    continue
                # print("-" * 60)
                print("\nRunning node: {}".format(ndata["name"]))
                node = EngineNode(uuid=ndata["uuid"], daemon_name=self.name)
                future = node.process(
                    pool, self.futures.get(ndata["uuid"]), action=ndata["action"]
                )
                self.futures[ndata["uuid"]] = future
                del node
        del ntdatas

    def clean_old_process(self):
        """Clean old process.

        When daemon is interupted, the old process is persist in a fake `running` state.
        """
        from scinode.core.db_nodetree import DBNodeTree

        # query nodes
        query = {
            "action": {"$in": ["UPDATE", "NONE"]},
            "state": {"$in": ["RUNNING"]},
        }
        query["meta.daemon_name"] = self.name
        ntdatas = list(
            self.db["nodetree"].find(
                query,
                {"name": 1, "uuid": 1, "nodes": 1},
            )
        )
        print("Reset: ")
        for ntdata in ntdatas:
            nt = DBNodeTree(uuid=ntdata["uuid"])  # , self.daemon_name)
            for name, node in ntdata["nodes"].items():
                if node["state"] == "RUNNING":
                    nt.reset_node(name, launch=True)
            nt.launch()

    def showlog(self, limit=100):
        with open(self.logfile) as f:
            lines = f.readlines()
            for line in lines[-limit:]:
                print(line.strip())

    def update_data(self):
        """Update data in the database.
        - pid
        - worker
        - sleep
        """
        pid = os.getpid()
        data = {
            "name": self.name,
            "pid": pid,
            "worker": self.worker,
            "sleep": self.sleep,
            "lastUpdate": datetime.datetime.utcnow(),
        }
        # print("udpate: ", data)
        update_one(data, self.db["daemon"], key="name")
        # print("Write pid to database")

    def validate_name(self, name):
        from scinode.database.client import scinodedb

        data = scinodedb["daemon"].find_one({"name": name})
        if data is not None:
            return True
        else:
            print("Daemon {} is not setup.".format(name))
            return False

    @property
    def data(self):
        from scinode.database.client import scinodedb

        data = scinodedb["daemon"].find_one({"name": self.name})
        return data

    @property
    def lastUpdate(self):
        return self.get_lastUpdate()

    def get_lastUpdate(self):
        dt = (datetime.datetime.utcnow() - self.data["lastUpdate"]).total_seconds()
        return dt

    def get_pid(self):
        data = self.data
        pid = data.get("pid", 0)
        # print("name: {}, pid: {}".format(self.name, pid))
        return pid


def init_broker():
    """Init broker."""
    from scinode.database.db import scinodedb

    data = scinodedb["broker"].find_one({"name": "scinode"})
    if not data:
        broker = {
            "name": "scinode",
            "log": "",
            "msg": [],
            "indices": [0],
        }
        scinodedb["broker"].insert_one(broker)
        print("Init broker successfully!")


if __name__ == "__main__":
    daemon = ScinodeDaemon("localhost")
    daemon.start(daemonize=False)
