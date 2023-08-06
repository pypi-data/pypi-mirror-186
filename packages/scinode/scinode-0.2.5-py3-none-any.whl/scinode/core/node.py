"""Node
"""
from scinode.core.collection import (
    PropertyCollection,
    InputSocketCollection,
    OutputSocketCollection,
)
from uuid import uuid1

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Node:
    """Base class for Node.

    Attributes:

    identifier: str
        The identifier is used for loading the Node.
    node_type: str
        type of this node.
    id: int
        node id in the nodetree.
    nodetree_uuid: str
        uuid of the nodetree this node belongs to.
    daemon_name: str
        name of the daemon which will run this node.
    counter: int
        number of time this node has been executed.
    args: list
        postional arguments of the exector.
    kwargs: list
        keyword arguments of the exector.
    platform: str
        platform that used to creat this node.
    scattered_from: str
        scattered_from node which is copied.

    Examples:

    add nodes:

    >>> float1 = nt.nodes.new("TestFloat", name = "float1")
    >>> add1 = nt.nodes.new("TestDelayAdd", name = "add1")
    """

    identifier: str = "Node"
    node_type: str = "Normal"
    id: int = 0
    nodetree_uuid: str = ""
    daemon_name: str = ""
    counter: int = 0
    platform: str = "scinode"
    args = []
    kwargs = []
    results = ()

    def __init__(
        self,
        id=1,
        name=None,
        uuid=None,
        nodetree=None,
        scattered_from="",
        scattered_label="",
        scatter_node="",
    ) -> None:
        self.id = id
        self.name = name or "{}{}".format(self.identifier, id)
        self.uuid = uuid or str(uuid1())
        self.nodetree = nodetree
        self.scattered_from = scattered_from
        self.scattered_label = scattered_label
        self.scatter_node = scatter_node
        self.ref_uuid = ""
        self.copy_uuid = ""
        self.properties = PropertyCollection(self)
        self.inputs = InputSocketCollection(self)
        self.outputs = OutputSocketCollection(self)
        self.executor = None
        self.state = "CREATED"
        self.action = "NONE"
        self.position = [30 * self.id, 30 * self.id]
        self.description = ""
        self.log = ""
        self.create_properties()
        self.create_sockets()
        logger.info("Create {}: {}".format(self.node_type, self.name))

    def create_properties(self):
        self.properties.clear()

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()

    def reset(self):
        """Reset this node and all its child nodes to "CREATED".

        Note, even through the core principle require that each node
        run independently. This action will set the state of this node and
        all its child nodes to "CREATED". Because this is execute by human.
        In order to do that, we need use the nodetree to reset its child nodes.
        """
        from scinode.core.db_nodetree import DBNodeTree

        if self.node_type not in ["REF"]:
            ent = DBNodeTree(uuid=self.uuid)
            ent.reset_node(self.name)
        self.update()

    def to_dict(self, short=False):
        """Save all datas, include properties, input and output sockets.

        This will be called when execute nodetree
        """
        from scinode.version import __version__

        logger.debug("save_to_db: {}".format(self.name))
        if short:
            data = {
                "name": self.name,
                "identifier": self.identifier,
                "node_type": self.node_type,
                "uuid": self.uuid,
            }
        else:
            meta = self.meta_to_dict()
            properties = self.properties_to_dict()
            input_sockets = self.input_sockets_to_dict()
            output_sockets = self.output_sockets_to_dict()
            executor = self.executor_to_dict()
            data = {
                "version": "scinode@{}".format(__version__),
                "uuid": self.uuid,
                "name": self.name,
                "id": self.id,
                "state": self.state,
                "action": self.action,
                "error": "",
                "meta": meta,
                "properties": properties,
                "inputs": input_sockets,
                "outputs": output_sockets,
                "executor": executor,
                "position": self.position,
                "description": self.description,
                "log": self.log,
            }
            #
            if len(self.results) != len(self.outputs):
                results = ()
                for output in self.outputs:
                    results += ({"name": output.name, "value": output.default_value},)
                data["results"] = results
        return data

    def meta_to_dict(self):
        """Export metadata to a dictionary."""
        meta = {
            "node_type": self.node_type,
            "identifier": self.identifier,
            "nodetree_uuid": self.nodetree.uuid,
            "ref_uuid": self.ref_uuid,
            "copy_uuid": self.copy_uuid,
            "identifier": self.identifier,
            "platform": self.platform,
            "scattered_from": self.scattered_from,
            "scattered_label": self.scattered_label,
            "counter": self.counter,
            "args": self.args,
            "kwargs": self.kwargs,
        }
        if not self.daemon_name:
            meta.update({"daemon_name": self.nodetree.daemon_name})
        else:
            meta.update({"daemon_name": self.daemon_name})
        return meta

    def properties_to_dict(self):
        """Export properties to a dictionary.
        This data will be used for calculation.
        """
        properties = {}
        for p in self.properties:
            properties[p.name] = p.to_dict()
        return properties

    def input_sockets_to_dict(self):
        """Export input sockets to a dictionary."""
        # save all relations using links
        inputs = []
        for socket in self.inputs:
            inputs.append(socket.to_dict())
        return inputs

    def output_sockets_to_dict(self):
        """Export output sockets to a dictionary."""
        # save all relations using links
        outputs = []
        for socket in self.outputs:
            outputs.append(socket.to_dict())
        return outputs

    def executor_to_dict(self):
        """Export executor dictionary to a dictionary.
        Three kinds of executor:
        - Python built-in function. e.g. getattr
        - User defined function
        - User defined class.
        """
        executor = self.get_executor() or self.executor
        if "name" not in executor:
            executor["name"] = executor["path"].split(".")[-1]
            executor["path"] = executor["path"][0 : -(len(executor["name"]) + 1)]
        if "type" not in executor:
            executor["type"] = "function"
        return executor

    @classmethod
    def from_dict(cls, data):
        """Rebuild Node from dict data."""
        node = cls(name=data["name"], uuid=data["uuid"])
        # load properties
        node.update_from_dict(data)
        return node

    def update_from_dict(self, data):
        """udpate node from dict data.
        Set metadata and properties.
        """
        for key in ["uuid", "state", "action", "description"]:
            if data.get(key):
                setattr(self, key, data.get(key))
        self.daemon_name = data["meta"].get("daemon_name")
        # properties
        for name, p in data["properties"].items():
            print(self.properties.keys())
            self.properties[name].value = p["value"]

    @classmethod
    def update_from_yaml(cls, filename=None, string=None):
        """update db node from yaml file.

        Args:
            filename (str, optional): _description_. Defaults to None.
            string (str, optional): _description_. Defaults to None.

        Returns:
            node: _description_
        """
        import yaml
        from scinode.utils.node import yaml_to_dict
        from pprint import pprint

        # load data
        if filename:
            with open(filename, "r") as f:
                ndata = yaml.safe_load(f)
        elif string:
            ndata = yaml.safe_load(string)
        else:
            raise Exception("Please specific a filename or yaml string.")
        ndata = yaml_to_dict(ndata)
        nt = cls.load_from_db(ndata["uuid"])
        return nt

    @classmethod
    def load_from_db(cls, uuid):
        """Load Node data from database."""
        from scinode.utils.node import get_node_data

        print("    Load data for node: uuid={}".format(uuid))
        ndata = get_node_data({"uuid": uuid})
        node = cls.from_dict(ndata)
        return node

    def copy(self, name):
        node = self.__class__(name=name, uuid=None, nodetree_uuid=self.nodetree_uuid)
        node.inputs.copy()
        node.outputs.copy()
        return node

    def get_executor(self):
        return None

    def get_results(self):
        """Item data from database

        Returns:
            dict: _description_
        """
        from scinode.database.client import scinodedb
        import pickle

        query = {"uuid": self.uuid}
        data = scinodedb["node"].find_one(query, {"results": 1})
        results = pickle.loads(data["results"])
        return results

    def update(self):
        """Update node."""
        import pickle
        from scinode.database.client import scinodedb

        query = {"uuid": self.uuid}
        data = scinodedb["node"].find_one(
            query, {"state": 1, "action": 1, "results": 1, "meta.counter": 1}
        )
        self.counter = data["meta"]["counter"]
        self.results = pickle.loads(data["results"])

    def __repr__(self) -> str:
        s = ""
        s += 'Node(name="{}", uuid="{}", inputs = ['.format(self.name, self.uuid)
        for input in self.inputs:
            s += '"{}", '.format(input.name)
        s += "], outputs = ["
        for output in self.outputs:
            s += '"{}", '.format(output.name)
        s += "])\n"
        return s

    def set(self, data):
        """Set properties by a dict.

        Args:
            data (dict): _description_
        """
        for key, value in data.items():
            self.properties[key].value = value

    def get(self, key):
        """Get the value of property by key.

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        return self.properties[key].value


def build_node_from_json(dbdata):
    import importlib

    module = importlib.import_module("{}".format(dbdata["node_path"]))
    node_type = getattr(module, dbdata["node_type"])
    node = node_type.from_json(dbdata)
    return node
