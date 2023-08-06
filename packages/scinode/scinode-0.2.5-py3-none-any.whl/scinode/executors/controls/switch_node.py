from scinode.core.executor import Executor


class ScinodeSwitch(Executor):
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

        print("    Run for Switch node")
        dbdata = self.dbdata
        switch_node = DBNode(uuid=dbdata["uuid"])
        # nodetree data
        nt = DBNodeTree(uuid=dbdata["meta"]["nodetree_uuid"])
        # because we skip the daemon to set the state
        # we have to update the result manully here
        results = pickle.loads(self.dbdata["results"])
        results[0]["value"] = self.kwargs["Input"]
        switch_node.update_db_keys({"results": pickle.dumps(results)})
        # set node state to be finished to avoid deadblock
        switch_node.update_db_keys({"state": "FINISHED"})
        switch_node.update_db_keys({"action": "NONE"})
        #
        # find all children nodes of the "switch" node
        if self.kwargs["Switch"]:
            # reset all nodes and launch
            print("reset node")
            nt.reset_node(dbdata["name"], launch=True)
        else:
            # skip all nodes
            print("skip node")
            nt.skip_node(dbdata["name"])
        this_results = (self.kwargs["Input"],)
        return this_results
