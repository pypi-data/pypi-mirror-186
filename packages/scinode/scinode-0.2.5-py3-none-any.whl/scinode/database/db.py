from scinode.database.client import scinodedb
from pprint import pprint
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class ScinodeDB:
    """Class used to query and manipulate the database."""

    def __init__(self) -> None:
        self.db = scinodedb

    def delete(self, name, query):
        resutls = self.db[name].delete_many(query)
        print("{} {} deleted.".format(resutls.deleted_count, name))

    def reset(self, name):
        if name.upper() == "NODETREE":
            self.db["nodetree"].delete_many({})
        elif name.upper() == "NODE":
            self.db["node"].delete_many({})
        elif name.upper() == "DAEMON":
            self.db["daemon"].delete_many({})
        elif name.upper() == "BROKER":
            self.db["broker"].delete_many({})
        else:
            print("{} is not in the database.".format(name))
            return
        print("Reset '{}' successfully.".format(name))

    def list(self):
        names = self.db.list_collection_names()
        data = {}
        for name in names:
            n = self.db[name].find().count()
            data[name] = n
        # print(pd.DataFrame(data))
        pprint(data)

    def update_db_keys(self, name, query={}, items={}):
        """update data and state to database"""
        newvalues = {"$set": items}
        self.db[name].update_many(query, newvalues)
        print(
            "update collection: {}, query: {}, Set: {}".format(name, query, newvalues)
        )
