from scinode.database.db import ScinodeDB
import pandas as pd
from pprint import pprint
import pickle
import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

pd.set_option("display.max_rows", None)


class NodeClient(ScinodeDB):
    """Class used to query and manipulate the database.

    Example:

    >>> client = NodeClient()
    >>> client.list({"name": "math"})
    """

    def __init__(self) -> None:
        super().__init__()

    def list(self, query={}, limit=100):
        """List node.

        Args:
            query (dict, optional): _description_. Defaults to {}.
            limit (int, optional): _description_. Defaults to 100.
        """
        from scinode.utils import get_time

        data = self.db["node"].find(
            query,
            {
                "_id": 0,
                "index": 1,
                "name": 1,
                "state": 1,
                "action": 1,
                "lastUpdate": 1,
                "meta.nodetree_uuid": 1,
            },
        )
        logger.debug(query)
        new_data = []
        for d in data:
            dt = int((datetime.datetime.utcnow() - d["lastUpdate"]).total_seconds())
            d["lastUpdate_second"] = dt
            d["lastUpdate"] = get_time(dt)
            #
            # ntdata = self.db["nodetree"].find_one(
            # {"uuid": d["meta"]["nodetree_uuid"]},
            # {"_id": 0, "name": 1},
            # )
            # d["nodetree"] = ntdata["name"]
            new_data.append(d)
        df = pd.DataFrame(new_data)
        if df.empty:
            print("index   name   state   action")
        else:
            df = df.sort_values(by=["lastUpdate_second"], ascending=False)[-limit:]
            print(df[["index", "name", "state", "action", "lastUpdate"]])

    def get_full_data(self, query):
        data = self.db["node"].find_one({"index": query["index"]}, {"log": 0})
        if data is None:
            print("We can not find node with query: {}".format(query))
            return
        data["properties"] = pickle.loads(data["properties"])
        data["results"] = pickle.loads(data["results"])
        return data

    def get_yaml_data(self, query):
        import yaml
        from scinode.utils.node import to_edit_dict

        ndata = self.get_full_data(query)
        data = to_edit_dict(ndata)
        s = yaml.dump(data, sort_keys=False)
        return s, ndata

    def show(self, query={}, all=False):
        """Show node data

        Args:
            query (dict, optional): _description_. Defaults to {}.
        """
        import sys, yaml
        from scinode.utils.node import to_edit_dict

        data = self.get_full_data(query)
        if not all:
            data = to_edit_dict(data)
            s = yaml.dump(data, sys.stdout, sort_keys=False)
        else:
            pprint(data)

    def log(self, query={}):
        """Show the execution log of this node.

        Args:
            query (dict, optional): _description_. Defaults to {}.
        """
        data = self.db["node"].find_one(
            {"index": query["index"]}, {"log": 1, "name": 1, "uuid": 1}
        )
        if data is None:
            print("We can not find node with query: {}".format(query))
            return
        print("Node: {}, {}".format(data["name"], data["uuid"]))
        pprint(data["log"])


if __name__ == "__main__":
    d = NodeClient()
    d.list()
    d.show({"index": 1})
