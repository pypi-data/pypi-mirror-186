from scinode.core.executor import Executor


class ScinodeScatter(Executor):
    """Scatter nodes executor"""

    def run(self):
        """
        0) Find all subtrees created by this node, and delete them
        1) Find all children nodes after the scatter node
        2) Create a new nodetree nt1
        3) build all children node inside new nodetree nt1
        4) use REF node
        5) launch the nodetree
        """
        print("Run for scatter ".format(self.name))
        self.prepare()
        self.new_nodetree()
        self.set_gather_state()

    def prepare(self):
        from scinode.core.db_nodetree import DBNodeTree

        self.delete_sub_nodetree()
        if isinstance(self.kwargs["Input"], dict):
            labels = self.kwargs["Input"].keys()
        else:
            labels = range(len(self.kwargs["Input"]))
        self.labels = labels
        print("  Scatter labels: ".format(self.labels))
        # nodetree data
        self.nt = DBNodeTree(uuid=self.dbdata["meta"]["nodetree_uuid"])
        self.copy_nodes = set(self.nt.record["connectivity"]["children"][self.name][1])

    def delete_sub_nodetree(self):
        """Delete nodetrees which are scattered from this node."""
        from scinode.database.nodetree import NodetreeClient

        # Find all subtrees created by this node, and delete them
        client = NodetreeClient()
        query = {"scatter_node": self.uuid}
        client.delete(query)

    def update_scatter_node(self, nt, label):
        """Create ref nodes for the missing nodes.
        Check the missing input nodes
        1) if the input node is scatter node, make a copy node, update the results.
        """
        import pickle

        node = nt.nodes[self.name]
        print("    set the input socket for the nodes connect to the scatter node")
        print()
        results = ({"name": "Result", "value": self.kwargs["Input"][label]},)
        node.update_db_keys({"results": pickle.dumps(results)})
        print(f"Node {self.name} is a COPY node.")
        node.update_db_keys(
            {
                "meta.node_type": "COPY",
                "state": "FINISHED",
                "action": "NONE",
            }
        )
        # add label for all children nodes
        node.update_db_keys({"meta.scattered_label": str(label)})

    def new_nodetree(self):
        """Copy nodes to new nodetree"""
        for label in self.labels:
            # add new nodetree
            name = "{}_{}".format(self.nt.name, label)
            print(
                "    Copy {} nodes to new nodetree: {}, .".format(
                    name, len(self.copy_nodes)
                )
            )
            nt = self.nt.copy(
                name,
                self.copy_nodes,
                is_child=True,
                scatter_node=self.uuid,
                scattered_label=label,
            )
            self.update_scatter_node(nt, label)
            nt.update_db_keys({f"nodes.{self.name}.node_type": "COPY"})
            #
            nt.launch()

    def set_gather_state(self):
        from scinode.database.db import scinodedb

        scatter = {}
        for label in self.labels:
            scatter[str(label)] = "CREATED"
        # all the children nodes should not run, instead the action should be gather.
        query = {"name": "scinode"}
        for name in self.copy_nodes:
            print(f"    Set Node {name} state to SCATTERED.")
            newvalues = {
                "$push": {
                    "msg": {
                        "$each": [
                            f"{self.nodetree_uuid},node,{name}:state:SCATTERED",
                            f"{self.nodetree_uuid},node,{name}:action:NONE",
                        ]
                    }
                }
            }
            scinodedb["broker"].update_one(query, newvalues)
            #
            print(f"    Add new key: scatter for Node {name}.")
            newvalues = {"$set": {f"nodes.{name}.scatter": scatter}}
            scinodedb["nodetree"].update_one(query, newvalues)
        return (None,)
