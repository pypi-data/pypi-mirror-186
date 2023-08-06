from scinode.database.db import ScinodeDB
from pprint import pprint
import datetime
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

pd.set_option("display.max_rows", 200)


class DaemonClient(ScinodeDB):
    """Class used to query and manipulate the database."""

    def __init__(self) -> None:
        super().__init__()

    def get_data(self, query={}):
        data = list(self.db["daemon"].find(query))
        for d in data:
            d["lastUpdate"] = int(
                (datetime.datetime.utcnow() - d["lastUpdate"]).total_seconds()
            )
        return data

    def list(self, query={}):
        """List daemon"""
        data = self.get_data(query)
        df = pd.DataFrame(data)
        if df.empty:
            print(
                "index",
                "name",
                "broker",
                "computer",
                "workdir",
                "pid",
                "worker",
                "sleep",
                "lastUpdate",
            )
        else:
            print(
                df[
                    [
                        "index",
                        "name",
                        "broker",
                        "computer",
                        "workdir",
                        "pid",
                        "worker",
                        "sleep",
                        "lastUpdate",
                    ]
                ]
            )

    def show(self, query={}):
        data = self.db["daemon"].find_one({"index": query["index"]})
        if data is None:
            print("We can not find daemon with query: {}".format(query))
            return
        pprint(data)


if __name__ == "__main__":
    d = DaemonClient()
    d.list()
    d.show({"index": 1})
