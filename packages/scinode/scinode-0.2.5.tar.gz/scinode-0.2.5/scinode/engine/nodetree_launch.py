"""
"""
import datetime
from scinode.core import DBItem
from scinode.database.client import scinodedb
from scinode.utils.db import insert_one, update_one
import logging

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class LaunchNodeTree(DBItem):
    """Launch nodetree to the database.

    Becareful, we have two data for nodetree.
    - full_data: includes all nodes data
    - short_data: only includes basic nodes data

    - if it does not exist in the database, save it to the database
    - if it exist in the database, find the difference. Update the difference in the database.

    uuid: str
        uuid of the nodetree.

    Example:

    >>> from scinode.engine.nodetree_launch import LaunchNodeTree
    >>> ntdata = nodetree.to_dict()
    >>> lnt = LaunchNodeTree(ntdata)
    >>> lnt.launch()
    """

    db_name: str = "nodetree"

    def __init__(self, ntdata) -> None:
        """_summary_

        Args:
            ntdata (dict): data of nodetree to be launched.
        """
        self.ntdata = ntdata
        self.uuid = ntdata["uuid"]
        self.name = ntdata["name"]

    def assign_UUID(self):
        """Assign uuid to nodetree and nodes"""
        import uuid

        # assign uuid to nodetree
        if not self.ntdata["uuid"]:
            self.ntdata["uuid"] = str(uuid.uuid1())
            self.ntdata["state"] = "CREATED"
            self.uuid = self.ntdata["uuid"]
        # assign uuid to nodes
        for name, node in self.ntdata["nodes"].items():
            # assign ndoetree uuid and daemon to node
            node["meta"]["nodetree_uuid"] = self.ntdata["uuid"]
            if not node["uuid"]:
                node["uuid"] = str(uuid.uuid1())
                node["state"] = "CREATED"
            if not node["meta"]["daemon_name"]:
                node["meta"]["daemon_name"] = self.ntdata["meta"]["daemon_name"]

    def build_link(self):
        """Update uuid for the links.

        - update uuid for links in nodes
        - generate links for nodetree
        - update link for ouput nodes
        """
        links = []
        for name, node in self.ntdata["nodes"].items():
            self.ntdata["nodes"][name]["uuid"] = node["uuid"]
            for input in node["inputs"]:
                for link in input["links"]:
                    full_link = link.copy()
                    full_link["to_node"] = node["name"]
                    full_link["to_socket"] = input["name"]
                    links.append(full_link)
        self.ntdata["links"] = links

    def insert_nodetree_to_db(self):
        """Save a new nodetree in the database.

        - nodetree
        - all nodes
        """
        from scinode.utils.db import insert_one
        from scinode.utils.nodetree import get_nt_short_data

        # pprint(self.ntdata)
        self.ntdata["created"] = datetime.datetime.utcnow()
        self.ntdata["lastUpdate"] = datetime.datetime.utcnow()
        ntdata = get_nt_short_data(self.ntdata)
        # init message
        insert_one(ntdata, scinodedb["nodetree"])
        self.insert_nodes_to_database(self.ntdata["nodes"])

    def save(self):
        """Save Nodetree.

        - Assign uuid if needed.
        - Update uuid for links. Build compressed nodes for nodetree.
        - Analysis connectivity
        - Check exist in database or not. If not in database, save directly.
        - If in database, analyze the difference, save accordingly.
        """
        self.assign_UUID()
        self.build_link()
        self.build_connectivity()
        in_db = self.exist_in_db()
        if in_db:
            self.update_nodetree_db()
            self.reset_nodes(self.modified_nodes)
        else:
            self.insert_nodetree_to_db()
        logger.debug(
            "Save nodetree: name={}, uuid={}".format(
                self.ntdata["name"], self.ntdata["uuid"]
            )
        )

    def update_nodetree_db(self):
        """Update nodetree in database.

        - analyze the difference.
        - save new nodes to database
        - update modified nodes to database.
        """
        self.check_diff()
        new_nodes, modified_nodes, modified_outputs = self.check_diff()
        self.modified_nodes = modified_nodes
        self.insert_nodes_to_database(new_nodes)
        logger.debug("Nodes to be updated: {}".format(modified_nodes))
        self.update_nodes_to_database(modified_nodes)
        # modified_outputs
        self.update_nodes_output_to_database(modified_outputs)
        # final
        self.update_nodetree_to_database(new_nodes)

    def insert_nodes_to_database(self, nodes):
        """Insert nodes to database

        Args:
            nodes (list): a list of node names.
        """
        import pickle

        for name in nodes:
            # print(self.ntdata["nodes"][name])
            if self.ntdata["nodes"][name]["meta"]["node_type"] in ["REF"]:
                self.ntdata["nodes"][name]["state"] = "FINISHED"
                self.ntdata["nodes"][name]["action"] = "NONE"
            logger.debug("Insert node: {}".format(name))
            self.ntdata["nodes"][name]["properties"] = pickle.dumps(
                self.ntdata["nodes"][name]["properties"]
            )
            self.ntdata["nodes"][name]["results"] = pickle.dumps(
                self.ntdata["nodes"][name]["results"]
            )
            self.ntdata["nodes"][name]["created"] = datetime.datetime.utcnow()
            self.ntdata["nodes"][name]["lastUpdate"] = datetime.datetime.utcnow()
            insert_one(self.ntdata["nodes"][name], scinodedb["node"])

    def update_nodes_to_database(self, nodes):
        """update nodes to database.

        Args:
            nodes (list): a list of node names.
        """
        import pickle

        for name in nodes:
            if self.ntdata["nodes"][name]["meta"]["node_type"] in ["REF"]:
                continue
            logger.debug("update node: {}".format(name))
            self.ntdata["nodes"][name]["properties"] = pickle.dumps(
                self.ntdata["nodes"][name]["properties"]
            )
            # be careful when updating results
            if "results" in self.ntdata["nodes"][name]:
                self.ntdata["nodes"][name]["results"] = pickle.dumps(
                    self.ntdata["nodes"][name]["results"]
                )
            self.ntdata["nodes"][name]["lastUpdate"] = datetime.datetime.utcnow()
            update_one(self.ntdata["nodes"][name], scinodedb["node"])

    def update_nodes_output_to_database(self, nodes):
        """Update nodes to database

        Args:
            nodes (list): a list of node names.
        """
        import pickle

        for name in nodes:
            logger.debug("update node: {}".format(name))
            self.ntdata["nodes"][name]["properties"] = pickle.dumps(
                self.ntdata["nodes"][name]["properties"]
            )
            # do not update results
            outputs = {
                "uuid": self.ntdata["nodes"][name]["uuid"],
                "outputs": self.ntdata["nodes"][name]["outputs"],
            }
            update_one(outputs, scinodedb["node"])

    def update_nodetree_to_database(self, new_nodes):
        """update nodetree to database"""
        import datetime
        from scinode.utils.nodetree import get_nt_short_data

        logger.debug("update nodetree: {}".format(self.ntdata["name"]))
        self.ntdata["lastUpdate"] = datetime.datetime.utcnow()
        ntdata = get_nt_short_data(self.ntdata)
        # print("update_nodetree_to_database: ", ntdata["nodes"])
        # insert new node to "nodes" field
        items = {f"nodes.{name}": ntdata["nodes"][name] for name in new_nodes}
        # skip field
        ntdata.pop("nodes")
        ntdata.update(items)
        update_one(ntdata, scinodedb["nodetree"])

    def reset_nodes(self, nodes):
        """Reset nodes

        Args:
            nodes (list): a list of node names.
        """
        for name in nodes:
            logger.debug(f"Reset node: {name}")
            self.push_message([f"{self.uuid},node,{name}:action:RESET"])

    def launch(self):
        """Launch Nodetree
        - set action to launch.
        - save to db
        """
        self.ntdata["state"] = "CREATED"
        self.ntdata["action"] = "LAUNCH"
        # reset modified noes
        self.set_nodes_action("LAUNCH")
        self.save()
        logger.debug(
            "Launch nodetree: name={}, uuid={}".format(
                self.ntdata["name"], self.ntdata["uuid"]
            )
        )

    def set_nodes_action(self, action):
        """Set node action."""
        for name, node in self.ntdata["nodes"].items():
            # print("Reset node: {}".format(node))
            node["action"] = action

    def check_diff(self):
        """Find difference between nodetree and its database.

        Returns:
            new_nodes: new nodes
            modified_nodes: modified nodes
        """
        from scinode.utils.nt_analysis import DifferenceAnalysis
        from scinode.utils.nodetree import get_nt_full_data

        nt1 = get_nt_full_data({"uuid": self.uuid})
        dc = DifferenceAnalysis(nt1=nt1, nt2=self.ntdata)
        new_nodes, modified_nodes, modified_outputs = dc.build_difference()
        logger.debug("New nodes: {}".format(new_nodes))
        logger.debug("Modified nodes: {}".format(modified_nodes))
        return new_nodes, modified_nodes, modified_outputs

    def exist_in_db(self):
        """Check nodetree exist in database or not.

        Returns:
            bool: _description_
        """
        # query the db first, if exist, skip this step
        if self.uuid != "" and self.dbdata is not None:
            logger.debug(
                "Nodetree: name={}, uuid={} exist in database".format(
                    self.ntdata["name"], self.ntdata["uuid"]
                )
            )
            return True
        return False

    def build_connectivity(self, ntdata=None):
        """Analyze the connectivity of nodetree and save it into dict."""
        from scinode.utils.nt_analysis import ConnectivityAnalysis

        if ntdata is None:
            ntdata = self.ntdata
        logger.debug("Calculate child nodes...")
        nc = ConnectivityAnalysis(ntdata)
        children = nc.build_children()
        inputs, outputs = nc.get_input_output()
        connectivity = {
            "children": children,
            "inputs": inputs,
            "outputs": outputs,
        }
        self.ntdata["connectivity"] = connectivity

    def push_message(self, action):
        """Update state and action in the broker.

        Args:
            data (dict): _description_
        """
        from scinode.database.client import scinodedb

        query = {"name": "scinode"}
        newvalues = {"$push": {"msg": {"$each": action}}}
        scinodedb["broker"].update_one(query, newvalues)


if __name__ == "__main__":
    from scinode.nodetree import NodeTree

    nt = NodeTree(name="test_debug_math")
    float1 = nt.nodes.new("TestFloat", "float1")
    float1.properties["Float"].value = 3.0
    math1 = nt.nodes.new("TestAdd", "add1")
    math1.properties["x"].value = 2
    nt.links.new(float1.outputs[0], math1.inputs[1])
    nt.launch()
