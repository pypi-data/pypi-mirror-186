from scinode.core.executor import Executor


class ScinodeUpdate(Executor):
    """Out the properties

    Args:
        BaseNode (_type_): _description_
    """

    def run(self):
        """
        1) Find all children nodes before the gather node
        3) Gather input socket data
        """
        from scinode.core.db_nodetree import DBNodeTree
        from scinode.core.db_node import DBNode
        import pickle

        dbdata = self.dbdata
        print(
            "    Run for Update node, count: {}".format(self.dbdata["meta"]["counter"])
        )
        # nodetree data
        update_node = DBNode(uuid=dbdata["uuid"])
        nt = DBNodeTree(uuid=dbdata["meta"]["nodetree_uuid"])
        inputs = dbdata["inputs"]
        non_from_nodes = []
        for link in inputs[1]["links"]:
            non_from_nodes.append(link["from_node"])
        # because we skip the daemon to set the state
        # we have to update the result manully here
        results = pickle.loads(self.dbdata["results"])
        print("   Counter: {}".format(dbdata["meta"]["counter"]))
        if dbdata["meta"]["counter"] > 0:
            # reset all nodes and launch
            nt.reset_node(dbdata["name"], launch=True)
            results[0]["value"] = self.kwargs["Update"]
            # print("    results: ", results)
            this_results = (self.kwargs["Update"],)
        else:
            results[0]["value"] = self.kwargs["Input"]
            this_results = (self.kwargs["Input"],)
        update_node.update_db_keys({"results": pickle.dumps(results)})
        update_node.update_db_keys({"meta.counter": dbdata["meta"]["counter"] + 1})
        update_node.update_db_keys({"state": "FINISHED"})
        update_node.update_db_keys({"action": "NONE"})
        return this_results
