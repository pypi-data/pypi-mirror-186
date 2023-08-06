"""
"""
from scinode.engine import EngineNodeTree
from scinode.database.client import scinodedb
import time
import logging


logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class Broker:
    """Broker Class.
    message-broker for SciNode.


    Example:

    >>> # load message
    >>> broker = Broker()
    >>> broker.process()
    >>> msg = broker.dbdata["msg"]
    """

    db_name: str = "broker"

    def __init__(self) -> None:
        """_summary_

        Args:
            uuid (_type_, optional): _description_. Defaults to None.
        """
        pass

    @property
    def dbdata(self):
        from scinode.database.client import scinodedb

        return scinodedb["broker"].find_one(
            {"name": "scinode"}, {"_id": 0, "msg": 1, "indices": 1}
        )

    @property
    def start(self):
        "Get the start of the new message"
        from scinode.database.client import scinodedb

        data = scinodedb["broker"].find_one(
            {"name": "scinode"}, {"_id": 0, "indices": {"$slice": -1}}
        )
        return data["indices"][0]

    def process(self):
        """apply message to nodetree and node"""
        start = self.start
        msg = scinodedb["broker"].find_one(
            {"name": "scinode"}, {"_id": 0, "msg": {"$slice": [start, 1e6]}}
        )["msg"]
        # print("start: ", start)
        # print("msg: ", msg)
        nmsg = len(msg)
        # print("apply_nodetree_message: ", bdata["nodetree"])
        if nmsg == 0:
            return
        for m in msg:
            print("process: ", m)
            uuid, catalog, body = m.split(",")
            if catalog == "nodetree":
                try:
                    self.apply_nodetree_message(uuid, body)
                except Exception as e:
                    print(e)
            elif catalog == "node":
                try:
                    self.apply_node_message(uuid, body)
                except Exception as e:
                    print(e)
            else:
                raise Exception(f"Unknown type {catalog}")
        scinodedb["broker"].update_one(
            {"name": "scinode"}, {"$push": {"indices": start + nmsg}}
        )

    def apply_nodetree_message(self, uuid, msg):
        print("apply_nodetree_message: ", msg)
        key, value = msg.split(":")
        # print(name, m)
        if key == "action":
            self.apply_nodetree_action(uuid, value)
        elif key == "state":
            scinodedb["nodetree"].update_one({"uuid": uuid}, {"$set": {key: value}})

    def apply_node_message(self, uuid, msg):
        """apply action to all nodes"""
        from scinode.database.client import scinodedb

        print("apply_node_message: ", msg)
        tstart = time.time()
        data = msg.split(":")
        if len(data) == 3:
            name, key, value = data
            scinodedb["nodetree"].update_one(
                {"uuid": uuid}, {"$set": {f"nodes.{name}.{key}": value}}
            )
            # push message to parent nodetree
            if key == "state" and value not in ["RUNNING"]:
                self.update_nodetree_state(uuid)
                record = scinodedb["nodetree"].find_one({"uuid": uuid}, {"meta": 1})
                if record["meta"]["scatter_node"]:
                    scinodedb["broker"].update_one(
                        {"name": "scinode"},
                        {
                            "$push": {
                                "msg": f"{record['meta']['parent']},node,scatter:{record['meta']['scattered_label']}:{msg}"
                            }
                        },
                    )
            if key == "action":
                self.apply_node_action(uuid, name, value)
        elif len(data) == 5:
            key1, label, name, key2, value = data
            scinodedb["nodetree"].update_one(
                {"uuid": uuid}, {"$set": {f"nodes.{name}.{key1}.{label}": value}}
            )
            self.update_nodetree_state(uuid)
        logger.debug("apply_node_message, time: {}".format(time.time() - tstart))

    def apply_nodetree_action(self, uuid, action):
        """Apply action to nodetree"""
        tstart = time.time()
        if action.upper() == "UPDATE":
            self.update_nodetree_state(uuid)
        elif action.upper() == "LAUNCH":
            self.launch_nodetree(uuid)
        elif action.upper() == "PAUSE":
            self.pause_nodetree(uuid)
        elif action.upper() == "PLAY":
            self.play_nodetree(uuid)
        elif action.upper() == "CANCEL":
            self.cancel_nodetree(uuid)
        elif action.upper() == "RESET":
            self.reset_nodetree(uuid)
        else:
            print("Action {} is not supported.".format(action))
        logger.debug("apply_nodetree_action, time: {}".format(time.time() - tstart))

    def launch_nodetree(self, uuid):
        """Launch nodetree."""
        print("Launch nodetree: {}".format(uuid))
        ntdata = scinodedb["nodetree"].find_one({"uuid": uuid}, {"nodes": 1})
        for name, node in ntdata["nodes"].items():
            node["action"] = "LAUNCH"
        # print("update_node_state: ", ntdata["nodes"])
        scinodedb["nodetree"].update_one(
            {"uuid": uuid}, {"$set": {"nodes": ntdata["nodes"]}}
        )
        self.update_nodetree_state(uuid)

    def pause_nodetree(self, uuid):
        """Pause nodetree."""
        print("Pause nodetree: {}".format(uuid))
        # print("update_node_state: ", ntdata["nodes"])
        scinodedb["nodetree"].update_one({"uuid": uuid}, {"$set": {"state": "PAUSED"}})

    def play_nodetree(self, uuid):
        """Play nodetree."""
        print("Play nodetree: {}".format(uuid))
        # print("update_node_state: ", ntdata["nodes"])
        scinodedb["nodetree"].update_one({"uuid": uuid}, {"$set": {"state": "RUNNING"}})

    def cancel_nodetree(self, uuid):
        """Cancel nodetree."""
        print("Cancel nodetree: {}".format(uuid))
        # print("update_node_state: ", ntdata["nodes"])
        scinodedb["nodetree"].update_one(
            {"uuid": uuid}, {"$set": {"state": "CANCELLED"}}
        )

    def apply_node_action(self, uuid, name, action):
        tstart = time.time()
        # print("apply_node_action: ", self.record["nodes"])
        # print(f"{action} {name}")
        if action == "NONE":
            scinodedb["nodetree"].update_one(
                {"uuid": uuid}, {"$set": {f"nodes.{name}.action": "NONE"}}
            )
        elif action == "PAUSE":
            self.pause_node(uuid, name)
        elif action == "PLAY":
            self.play_node(uuid, name)
        elif action == "SKIP":
            self.skip_node(uuid, name)
        elif action == "RESET":
            self.reset_node(uuid, name)
        elif action == "RESET_LAUNCH":
            self.reset_node(uuid, name, launch=True)
        elif action == "FINISH":
            # TODO
            # self.record[name]["state"] = "FINISHED"
            pass
        # print("apply_node_action: ", self.record["nodes"])
        logger.debug("apply_node_action, time: {}".format(time.time() - tstart))

    def update_nodetree_state(self, uuid):
        """update nodetree state.

        If there is a node change its state, we need to call this funciton.
        """
        print("\nUpdate nodetree: {}".format(uuid))
        nodetree = EngineNodeTree(uuid=uuid)
        nodetree.process()
        del nodetree

    def pause_node(self, uuid, name):
        """Pause node.

        Args:
            name (str): name of the node to be paused
        """
        logger.debug("pause node, name: {}".format(name))
        scinodedb["nodetree"].update_one(
            {"uuid": uuid}, {"$set": {f"nodes.{name}.state": "PAUSED"}}
        )

    def play_node(self, uuid, name):
        """Play node.

        Args:
            name (str): name of the node to be played
        """
        logger.debug("play node, name: {}".format(name))
        scinodedb["nodetree"].update_one(
            {"uuid": uuid}, {"$set": {f"nodes.{name}.state": "CREATED"}}
        )

    def skip_node(self, uuid, name):
        """Skip node.

        Args:
            name (str): name of the node to be skiped
        """
        nodes_to_skip = []
        ntdata = scinodedb["nodetree"].find_one(
            {"uuid": uuid}, {"connectivity.children": 1}
        )
        child_nodes = ntdata["connectivity"]["children"][name][0]
        nodes_to_skip.extend(child_nodes)
        logger.debug("reset node, name: {}".format(name))
        items = {}
        for name in nodes_to_skip:
            items[f"nodes.{name}.state"] = "SKIPPED"
        scinodedb["nodetree"].update_one({"uuid": uuid}, {"$set": items})

    def reset_nodetree(self, uuid):
        """Reset node and all its child nodes.

        Args:
            name (str): name of the node to be paused
        """
        print("Reset nodetree: {}".format(uuid))
        ntdata = scinodedb["nodetree"].find_one({"uuid": uuid}, {"nodes": 1})
        for name in ntdata["nodes"]:
            ntdata["nodes"][name]["state"] = "CREATED"
        # print("update_node_state: ", ntdata["nodes"])
        scinodedb["nodetree"].update_one(
            {"uuid": uuid}, {"$set": {"nodes": ntdata["nodes"]}}
        )

    def reset_node(self, uuid, name, launch=False):
        """Reset node and all its child nodes.

        Args:
            name (str): name of the node to be paused
        """
        nodes_to_reset = [name]
        ntdata = scinodedb["nodetree"].find_one(
            {"uuid": uuid}, {"connectivity.children": 1}
        )
        child_nodes = ntdata["connectivity"]["children"][name][0]
        nodes_to_reset.extend(child_nodes)
        logger.debug("reset node, name: {}".format(name))
        items = {}
        for name in nodes_to_reset:
            items[f"nodes.{name}.state"] = "CREATED"
        if launch:
            for name in nodes_to_reset:
                items[f"nodes.{name}.action"] = "LAUNCH"
        scinodedb["nodetree"].update_one({"uuid": uuid}, {"$set": items})

    def write_log(self, log, daemon=False, database=True):
        if daemon:
            print(log)
        if database:
            old_log = self.db.find_one({"uuid": self.uuid}, {"_id": 0, "log": 1})["log"]
            log = old_log + log
            self.update_db_keys({"log": log})

    def push_db_keys(self, items={}):
        """update data and state to database"""
        query = {"uuid": self.uuid}
        newvalues = {"$push": items}
        self.db.update_one(query, newvalues)

    def show(self):
        print("\n")
        print("Broker: ")
        print("-" * 40)
        data = self.dbdata
        print(data)
        n = len(data["indices"])
        for i in range(1, n):
            print("-" * 20)
            print(i - 1, i)
            for m in data["msg"][data["indices"][i - 1] : data["indices"][i]]:
                uuid, catalog, msg = m.split(",")
                print(uuid, msg)
