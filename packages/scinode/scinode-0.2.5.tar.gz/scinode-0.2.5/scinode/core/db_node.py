from scinode.core import DBItem
import logging

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class DBNode(DBItem):
    """DBNode Class.
    Process the node data from the database.

    db_name: str
        name of the database.
    uuid: str
        uuid of the node.
    name: str
        name of the node.

    Example:

    >>> # load node from database
    >>> node = DBNode(uuid=uuid)
    """

    db_name: str = "node"

    def __init__(self, uuid=None, dbdata=None) -> None:
        """init a instance

        Args:
            uuid (str, optional): uuid of the node.
                Defaults to None.
            dbdata (dict, optional): data of the node from database.
                Defaults to None.
        """
        if dbdata:
            uuid = dbdata["uuid"]
        super().__init__(uuid)
        self.record = self.dbdata
        self.name = self.record["name"]
        self.id = self.record["id"]
        self.scattered_from = self.record["meta"]["scattered_from"]
        self.scattered_label = self.record["meta"]["scattered_label"]

    def copy(
        self, name, nodetree_uuid=None, is_scattered_node=False, scattered_label=""
    ):
        """Copy this node to a new item and insert it into the database.

        Args:
            name (str): name of the new node
            nodetree_uuid (str): uuid of the nodetree.
            is_scattered_node (bool, optional): Is it a scattered node.
                Defaults to False.

        Returns:
            DBNode: a node
        """
        import uuid
        from scinode.utils.node import get_node_data

        record = get_node_data({"uuid": self.uuid}, {"_id": 0})
        # change name and uuid
        record["name"] = name
        record["state"] = "CREATED"
        record["action"] = "NONE"
        record["uuid"] = str(uuid.uuid1())
        # print(record)
        # update uuid in link, now we can only update half
        inputs = record["inputs"]
        for input in inputs:
            for link in input["links"]:
                link["to_node"] = record["name"]
                link["to_node_uuid"] = record["uuid"]
        record["inputs"] = inputs
        outputs = record["outputs"]
        for output in outputs:
            for link in output["links"]:
                link["from_node"] = record["name"]
        record["outputs"] = outputs
        if nodetree_uuid is not None:
            record["meta"]["nodetree_uuid"] = nodetree_uuid
        if is_scattered_node:
            record["meta"]["scattered_from"] = self.uuid
            record["meta"]["scattered_label"] = scattered_label
        # self.insert_one(record)
        # node = self.__class__(uuid=record["uuid"])
        return record

    def copy_as_ref(self, name, nodetree_uuid=None, is_scattered_node=False):
        record = self.copy(
            name=name, nodetree_uuid=nodetree_uuid, is_scattered_node=is_scattered_node
        )
        record["meta"]["node_type"] = "REF"
        record["meta"]["ref_uuid"] = self.uuid
        record["state"] = "FINISHED"
        record["action"] = "NONE"
        return record

    @classmethod
    def update_from_dict(cls, data):
        """Udpate node from dict data.
        Set metadata and properties.
        """
        from scinode.utils.node import get_node_data

        ndata = get_node_data({"uuid": data["uuid"]})
        for key in ["uuid", "state", "action", "description"]:
            if data.get(key):
                ndata[key] = data.get(key)
        for key in ["daemon_name"]:
            if data.get(key):
                ndata["meta"][key] = data.get(key)
        # properties
        for name, p in data["properties"].items():
            ndata["properties"][name]["value"] = p
        # links
        index = {}
        for i, input in enumerate(ndata["inputs"]):
            index[input["name"]] = i
            input["links"] = []
        new_inputs = data.get("inputs", [])
        # print(new_inputs)
        for link in new_inputs:
            # print("link: ", link)
            link["to_node"] = ndata["name"]
            ndata["inputs"][index[link["to_socket"]]]["links"].append(link)
        return ndata

    def update_from_yaml(self, filename=None, string=None):
        """update node from yaml file.

        Args:
            filename (str, optional): _description_. Defaults to None.
            string (str, optional): _description_. Defaults to None.

        Returns:
            node: _description_
        """
        from scinode.utils import load_yaml

        # load data
        ndata = load_yaml(filename=filename, string=string)
        self.update_from_dict(ndata)

    @property
    def dbdata(self):
        """Item data from database

        Returns:
            dict: _description_
        """
        from scinode.utils.node import get_node_data

        query = {"uuid": self.uuid}
        dbdata = get_node_data(query)
        return dbdata

    @property
    def nodetree_uuid(self):
        dbdata = self.get_dbdata({"uuid": self.uuid}, {"meta.nodetree_uuid": 1})
        return dbdata["meta"]["nodetree_uuid"]

    def reset(self, launch=False):
        """Reset node. Include all its properties:
        states, counter and results.
        """
        if self.record["meta"]["node_type"] in ["REF"]:
            return

        if launch:
            action = "LAUNCH"
        else:
            action = "NONE"
        counter = 0
        self.update_db_keys(
            {
                "state": "CREATED",
                "action": action,
                "counter": counter,
                # "results": pickle.dumps(None)
            }
        )

    def getstate(self):
        from scinode.database.db import scinodedb

        query = {"uuid": self.nodetree_uuid}
        data = scinodedb["nodetree"].find_one(query, {"_id": 0, "nodes": 1})["nodes"]
        return data[self.name].get("state")

    def getaction(self):
        from scinode.database.db import scinodedb

        query = {"uuid": self.nodetree_uuid}
        data = scinodedb["nodetree"].find_one(query, {"_id": 0, "nodes": 1})["nodes"]
        return data[self.name].get("action")
