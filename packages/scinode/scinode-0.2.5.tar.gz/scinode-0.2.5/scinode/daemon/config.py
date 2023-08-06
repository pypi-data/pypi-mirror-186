from scinode.database.client import scinodedb
from scinode.utils.db import insert_one, update_one
from pathlib import Path
from uuid import uuid1
import datetime
from scinode.profile import profile_datas


class DaemonConfig:
    """Configuration for daemon.

    Args:
        Config (_type_): _description_
    """

    def __init__(
        self,
        name="localhost",
        uuid=None,
        computer=None,
        workdir=str(Path.home()),
        sleep=5,
        broker=False,
    ) -> None:
        self.name = name
        self.workdir = workdir
        self.uuid = uuid if uuid else str(uuid1())
        self.sleep = sleep
        self.broker = broker
        self.computer = computer or profile_datas["computer"]

    @property
    def datas(self):
        return self.loadDatas()

    def loadDatas(self):
        """Load datas from json file.

        Returns:
            list: a list of the configuration datas.
        """
        from scinode.database.daemon import DaemonClient

        client = DaemonClient()
        return client.get_data()

    def show(self):
        from scinode.daemon.daemon import ScinodeDaemon

        config_datas = self.datas
        for i in range(len(config_datas)):
            daemon = ScinodeDaemon(name=config_datas[i]["name"])
            is_running = daemon.get_status()
            pidfile = daemon.read_pidfile()
            pid = pidfile["pid"]
            worker = pidfile["worker"]
            config_datas[i]["pid"] = pid
            config_datas[i]["worker"] = worker
            config_datas[i]["running"] = is_running == 0

    def save_to_db(self):
        from colorama import Fore, Style

        data = list(scinodedb["daemon"].find({"name": self.name}))
        if len(data) != 0:
            print(
                Fore.RED
                + f"\n Error! \nDaemon {self.name} is already registered. Please choose another name.\n"
                + Style.RESET_ALL
            )
            return
        if self.broker:
            data = list(scinodedb["daemon"].find())
            for d in data:
                if d["broker"]:
                    print(
                        Fore.RED
                        + f"\n Error! \nDaemon {d['name']} is already registered as the broker.!\n"
                        + Style.RESET_ALL
                    )
                return
        data = {
            "name": self.name,
            "computer": self.computer,
            "broker": self.broker,
            "uuid": self.uuid,
            "workdir": self.workdir,
            "pid": 0,
            "worker": 0,
            "sleep": self.sleep,
            "running": False,
            "action": None,
            "lastUpdate": datetime.datetime.utcnow(),
        }
        insert_one(data, scinodedb["daemon"])

    @classmethod
    def add_from_json(cls, file):
        """Load datas from json file.

        Returns:
            list: a list of the configuration datas.
        """
        import json

        # read file
        with open(file, "r") as f:
            datas = json.load(f)
            d = cls(**datas)
            d.save_to_db()
