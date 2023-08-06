from scinode.core import DBItem
from scinode.database.client import db_node
import traceback
import logging

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


class EngineNode(DBItem):
    """EngineNode Class.
    Process the node with the data from the database.
    It can be called by the daemon or called manually.

    uuid: str
        uuid of the node.
    name: str
        name of the node.

    Example:
    >>> # load node data from database
    >>> query = {"uuid": "your-node-uuid"}
    >>> dbdata = scinodedb["node"].find_one(query)
    >>> node = EngineNode(uuid=dbdata["uuid"])  # , self.daemon_name)
    >>> future = node.process(pool, future)

    """

    db_name: str = "node"

    def __init__(self, uuid=None, dbdata=None, daemon_name="localhost") -> None:
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
        self.daemon_name = daemon_name
        self.id = self.record["id"]
        self.nodetree_uuid = self.record["meta"]["nodetree_uuid"]
        self.scattered_from = self.record["meta"]["scattered_from"]
        self.scattered_label = self.record["meta"]["scattered_label"]

    def process(self, pool, future=None, action=None):
        """process data based on the action flag.

        Args:
            pool (ThreadPoolExecutor): Pool used to submit job
            future (concurrent.futures.Future, optional): Defaults to None.

        Returns:
            oncurrent.futures.Future: _description_
        """
        try:
            future = self.apply_action(pool, future, action=action)
        except Exception:
            import traceback

            error = traceback.format_exc()
            log = "xxxxxxxxxx Failed xxxxxxxxxx\nNode {} failed due to: {}".format(
                self.name, error
            )
            self.update_db_keys({"state": "FAILED"})
            self.update_db_keys({"action": "NONE"})
            self.update_db_keys({"error": str(error)})
            self.write_log(log)

        return future

    def apply_action(self, pool, future=None, action=None):
        """Apply node action

        Args:
            pool (dict): _description_
            future (future, optional): _description_. Defaults to None.
            action (_type_, optional): _description_. Defaults to None.

        Returns:
            future: _description_
        """
        if not action:
            action = self.record["action"]
        log = "\nDaemon: {}\n".format(self.daemon_name)
        log += "\nAction: {}\n".format(action)
        self.write_log(log)
        if action is None or action.upper() == "NONE":
            return
        elif action.upper() == "LAUNCH":
            future = self.launch(pool)
        elif action.upper() == "GATHER":
            self.gather()
            return None
        elif action.upper() == "CANCEL":
            self.cancel(future)
            return None
        else:
            log = "\nAction {} is not supported.".format(self.action)
            self.write_log(log)
        return future

    def launch(self, pool):
        """Launch node"""
        from scinode.utils.node import (
            get_input_parameters_from_db,
            inspect_executor_arguments,
        )

        # code here
        dbdata = self.record
        log = "\nLaunch node {}, {}\n".format(dbdata["id"], dbdata["name"])
        parameters = get_input_parameters_from_db(dbdata)
        # print("parameters: ", parameters)
        args, kwargs = inspect_executor_arguments(
            parameters, dbdata["meta"]["args"], dbdata["meta"]["kwargs"]
        )
        # print("  Parameters: ", parameters)
        log += "  args, kwargs {} {} \n".format(args, kwargs)
        Executor, executor_type = self.get_executor()
        # print("  Executor: ", Executor)
        # future = pool.submit(executor, parameters)
        # self.action = "NONE"
        # self.state = "RUNNING"
        self.push_message(
            [
                f"{self.nodetree_uuid},node,{self.name}:state:RUNNING",
                f"{self.nodetree_uuid},node,{self.name}:action:NONE",
            ]
        )
        if executor_type.upper() == "CLASS":
            # For user defined node, we can add daemon name to kwargs
            executor = Executor(
                *args, **kwargs, dbdata=dbdata, daemon_name=self.daemon_name
            )
            future = pool.submit(executor.run)
        else:
            future = pool.submit(Executor, *args, **kwargs)
        future.add_done_callback(self.check_future_done)
        self.write_log(log)
        return future

    def gather(self):
        """gather result from child nodes"""
        dbdata = self.dbdata
        # gather results
        import pickle

        results = pickle.loads(dbdata["results"])
        n = len(results)
        # init the results as a list
        for i in range(n):
            results[i]["value"] = []
        # fetch results from children
        children = db_node.find(
            {"meta.scattered_from": dbdata["uuid"]},
            {"uuid": 1, "name": 1, "results": 1},
        )
        for child in children:
            child_results = pickle.loads(child["results"])
            for i in range(n):
                value = child_results[i]["value"]
                results[i]["value"].append(value)
            # print("  Save results: ", results)
        self.update_db_keys({"results": pickle.dumps(results)})
        log = f"Node: {dbdata['name']} is gathered.\n"
        log += "Results: {}".format(results)
        # self.state = "FINISHED"
        # self.action = "NONE"
        self.push_message(
            [
                f"{self.nodetree_uuid},node,{self.name}:state:FINISHED",
                f"{self.nodetree_uuid},node,{self.name}:action:NONE",
            ]
        )
        self.write_log(log)

    @property
    def input_node_data(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        from scinode.utils.node import get_input_node_data

        nodes = get_input_node_data(self.record, db_node)
        # print("Total: {} parent nodes.".format(len(nodes)))
        return nodes

    def check_future_done(self, future):
        """Check if node finished

        Args:
            future (_type_): _description_

        Raises:
            Exception: _description_
        """
        log = "\n  Check result for Node: {}, {}.".format(self.id, self.name)
        if future.exception() is not None:
            error = traceback.format_exc()
            log += "\nxxxxxxxxxx Failed xxxxxxxxxx\n{}".format(error)
            # self.state = "FAILED"
            # self.action = "NEED_HELP"
            self.push_message(
                [
                    f"{self.nodetree_uuid},node,{self.name}:state:FAILED",
                    f"{self.nodetree_uuid},node,{self.name}:action:NEED_HELP",
                ]
            )
            self.update_db_keys({"error": str(error)})
            self.write_log(log)
            return
        elif future.cancelled():
            log == "\n  Job was cancelled"
            # self.state = "CANCELLED"
            # self.action = "NONE"
            self.push_message(
                [
                    f"{self.nodetree_uuid},node,{self.name}:state:CANCELLED",
                ]
            )
            self.update_db_keys({"error": "Job was cancelled"})
            self.write_log(log)
            return
        else:
            # job is done, try to get result
            try:
                self.save_result(future)
            except Exception:
                error = traceback.format_exc()
                log += "\nxxxxxxxxxx Failed xxxxxxxxxx\nFetch results from future failed, due to: {}".format(
                    error
                )
                # self.state = "FAILED"
                # self.action = "NEED_HELP"
                self.push_message(
                    [
                        f"{self.nodetree_uuid},node,{self.name}:state:FAILED",
                        f"{self.nodetree_uuid},node,{self.name}:action:NEED_HELP",
                    ]
                )
                self.update_db_keys({"error": str(error)})
                self.write_log(log)
                return

    def save_result(self, future):
        """Save result to database."""
        import pickle

        future_results = future.result()
        log = "\n    results from future: {}".format(future_results)
        dbdata = self.dbdata
        results = pickle.loads(dbdata["results"])
        # update results with the future_results
        if not isinstance(future_results, tuple):
            future_results = (future_results,)
        if len(future_results) != len(results):
            # self.state = "FAILED"
            # self.action = "NEED_HELP"
            self.push_message(
                [
                    f"{self.nodetree_uuid},node,{self.name}:state:FAILED",
                    f"{self.nodetree_uuid},node,{self.name}:action:NEED_HELP",
                ]
            )
            log += """xxxxxxxxxx Error xxxxxxxxxx\nNumber of results from future:
    {} does not equal to number of sockets: {}.\n""".format(
                len(future_results), len(results)
            )
            self.write_log(log)
            raise Exception(log)
        n = len(results)
        for i in range(n):
            results[i]["value"] = future_results[i]
        # print("  Save results: ", results)
        self.update_db_keys({"results": pickle.dumps(results)})
        # self.state = "FINISHED"
        # self.action = "NONE"
        self.push_message(
            [
                f"{self.nodetree_uuid},node,{self.name}:state:FINISHED",
                f"{self.nodetree_uuid},node,{self.name}:action:NONE",
            ]
        )
        log += "\n  Node: {} is finished".format(dbdata["name"])
        print("\n  Node: {} is finished".format(dbdata["name"]))
        self.write_log(log)

    def get_executor(self):
        import importlib

        data = self.dbdata["executor"]
        module = importlib.import_module("{}".format(data["path"]))
        executor = getattr(module, data["name"])
        type = data.get("type", "function")
        return executor, type

    def cancel(self, future):
        """Cancel node"""
        if future is not None:
            log = "Node is running: {}.\n".format(future.running())
            was_calcelled = future.cancel()
            if was_calcelled:
                state = "CANCELLED"
                log += "Node is cancelled: ".format(was_calcelled)
                action = "NONE"
                # self.update_db_keys({"outputs": {}})
            else:
                state = "FAILED"
                action = "NEED_HELP"
                log += "Can not cancel node.".format()
        else:
            state = "CANCELLED"
            action = "NONE"
            log = "Future is None. Node {} is not running. Can not cancel.".format(
                self.dbdata["name"]
            )
        self.update_db_keys(
            {"state": state, f"{self.nodetree_uuid},node,{self.name}:action": action}
        )
        self.write_log(log)

    def __repr__(self) -> str:
        s = ""
        s += 'EngineNode(name="{}", uuid="{}", nodetree_uuid = {},\
scattered_from = {}, state={}, action={})'.format(
            self.name,
            self.uuid,
            self.nodetree_uuid,
            self.meta["scattered_from"],
            self.state,
            self.action,
        )
        return s

    def write_log(self, log, daemon=False, database=True):
        if daemon:
            print(log)
        if database:
            old_log = self.db.find_one({"uuid": self.uuid}, {"_id": 0, "log": 1})["log"]
            log = old_log + log
            self.update_db_keys({"log": log})

    def push_message(self, action):
        """Update state and action in the broker.

        Args:
            data (dict): _description_
        """
        from scinode.database.client import scinodedb

        query = {"name": "scinode"}
        newvalues = {"$push": {f"msg": {"$each": action}}}
        # print(scinodedb["broker"].find_one(query, {"_id": 0}))
        scinodedb["broker"].update_one(query, newvalues)
        # print(scinodedb["broker"].find_one(query, {"_id": 0}))
