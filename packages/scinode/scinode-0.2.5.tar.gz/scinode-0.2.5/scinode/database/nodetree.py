from scinode.database.db import ScinodeDB
from scinode.database.client import db_node
import pandas as pd
from pprint import pprint
import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


pd.set_option("display.max_rows", None)


class NodetreeClient(ScinodeDB):
    """Class used to query and manipulate the database.

    Example:

    >>> client = NodeTreeClient()
    >>> client.list({"name": "math"})
    """

    def __init__(self) -> None:
        super().__init__()

    def delete(self, query):
        nodetrees = self.db["nodetree"].find(query)
        count = 0
        for nodetree in nodetrees:
            resutls = self.db["node"].delete_many(
                {"meta.nodetree_uuid": nodetree["uuid"]}
            )
            count += resutls.deleted_count
        resutls = self.db["nodetree"].delete_many(query)
        print(
            "{} nodetree deleted. {} node deleted".format(resutls.deleted_count, count)
        )

    def list(self, query={}, limit=100):
        """List nodetree.

        Args:
            query (dict, optional): _description_. Defaults to {}.
            limit (int, optional): _description_. Defaults to 100.
        """
        from scinode.utils import get_time

        data = self.db["nodetree"].find(
            query,
            {
                "_id": 0,
                "index": 1,
                "name": 1,
                "state": 1,
                "action": 1,
                "lastUpdate": 1,
                "meta": 1,
            },
        )
        if data is None:
            print("We can not find nodetree with query: {}".format(query))
            return
        new_data = []
        for d in data:
            dt = int((datetime.datetime.utcnow() - d["lastUpdate"]).total_seconds())
            d["lastUpdate_second"] = dt
            d["lastUpdate"] = get_time(dt)
            new_data.append(d)
        df = pd.DataFrame(new_data)
        if df.empty:
            print("index    name    state    action  lastUpdate")
            return
        df = df.sort_values(by=["lastUpdate_second"], ascending=False)[-limit:]
        print(df[["index", "name", "state", "action", "lastUpdate"]])

    def show(self, query, broker=False):
        """Show nodetree data.

        Args:
            query (_type_): _description_
        """
        data = self.db["nodetree"].find_one({"index": query["index"]}, {"log": 0})
        if data is None:
            print("We can not find nodetree with query: {}".format(query))
            return
        print("NodeTree: {}: \n".format(data["name"]))
        data["generation_time"] = data.get("_id").generation_time
        pprint(data)
        query = {"meta.nodetree_uuid": data["uuid"]}
        self.show_nodes(data["uuid"], data["nodes"])
        if broker:
            self.show_broker(data["uuid"])

    def show_nodes(self, uuid, nodes):
        from colorama import Fore, Style

        dbnodes = list(
            self.db["node"].find({"meta.nodetree_uuid": uuid}, {"name": 1, "index": 1})
        )
        print("\n  Nodes: ")
        print("{:10s} {:15s} {:10s} {:10s}".format("index", "name", "state", "action"))
        print("-" * 60)
        for node in dbnodes:
            if nodes[node["name"]]["state"] == "FINISHED":
                print(
                    "{:^10d} {:15s} {:10s} {:10s}".format(
                        node["index"],
                        node["name"],
                        Fore.GREEN + nodes[node["name"]]["state"] + Style.RESET_ALL,
                        nodes[node["name"]]["action"],
                    )
                )
            else:
                print(
                    "{:^10d} {:15s} {:10s} {:10s}".format(
                        node["index"],
                        node["name"],
                        nodes[node["name"]]["state"],
                        nodes[node["name"]]["action"],
                    )
                )

    def get_full_data(self, query):
        from scinode.utils.nodetree import get_nt_full_data

        data = get_nt_full_data(query)
        return data

    def get_yaml_data(self, query):
        import yaml
        from scinode.utils.nodetree import to_edit_dict

        ndata = self.get_full_data(query)
        data = to_edit_dict(ndata)
        s = yaml.dump(data, sort_keys=False)
        return s, ndata

    def log(self, query):
        """Show the execution log of this nodetree.

        Args:
            query (_type_): _description_
        """
        data = self.db["nodetree"].find_one(
            {"index": query["index"]}, {"_id": 0, "log": 1, "name": 1, "uuid": 1}
        )
        if data is None:
            print("We can not find nodetree with query: {}".format(query))
            return
        print("Nodetree: {}, {}".format(data["name"], data["uuid"]))
        pprint(data["log"])


if __name__ == "__main__":
    d = NodetreeClient()
    d.list()
    d.show({"index": 1})
