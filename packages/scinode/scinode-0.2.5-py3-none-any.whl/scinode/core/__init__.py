import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class DBItem:
    """Class that represents an item from database.
    Includes a collection of methods used to interact with
    the database.

    Attributes:
        identifier (str): identifier of the class.
        db_name (str): name of the collection in the database.
        item_type (str): type the Item. e.g. Nodetree, Node
        name (str): name of the instance
    """

    identifier: str = "DBItem"
    db_name: str = ""
    item_type: str = "DBItem"

    def __init__(self, uuid="") -> None:
        """init a DBItem with uuid.

        Args:
            uuid (_type_, optional): _description_. Defaults to None.
        """
        self.uuid = uuid

    def init_db(self):
        """Initialize into the database with basic data, including:
        - uuid
        - identifier
        - metadata
        - state: Created
        - action: None
        - error: ""
        """
        # query the db first, if exist, skip this init step
        if self.uuid != "" and self.dbdata is not None:
            return
        if self.uuid == "":
            import uuid

            self.uuid = str(uuid.uuid1())
        # insert to database
        data = {
            "identifier": self.identifier,
            "uuid": self.uuid,
            "meta": {},
            "state": "CREATED",
            "action": "NONE",
            "error": "",
        }
        # print(data)
        item = self.insert_one(data)
        logger.debug(
            "Init db for {}: {}, uuid={}".format(self.item_type, self.name, self.uuid)
        )

    def add_from_json(self, file):
        """Load data from a json file, then insert into database.

        Args:
            file (str): json file
        """
        import json

        with open(file) as f:
            datas = json.load(f)
        if self.uuid == "":
            if not datas.get("uuid", False):
                import uuid

                self.uuid = str(uuid.uuid1())
            else:
                self.uuid = datas.get("uuid")
        # print(datas)
        self.insert_one(datas)

    def insert_one(self, item):
        """Insert one item to database.

        Args:
            item (dict): data of the item.
        """
        from scinode.utils.db import insert_one

        insert_one(item, self.db)

    def launch(self):
        """Launch the job"""
        self.init_db()
        self.action = "LAUNCH"

    def reset(self):
        """Reset the state to "CREATED".
        The uuid will be the same. Therefore, launch the job only
        update the data in the database. No new item will be created.
        """
        self.state = "CREATED"
        self.state = "NONE"

    def reset_state(self):
        """Reset the state and action.
        Therefore, the node will re-run when launched.
        """
        self.state = "CREATED"
        self.action = "LAUNCH"

    @property
    def db(self):
        """Database collection

        Returns:
            MongoDB collection: _description_
        """
        from scinode.database.client import scinodedb

        return scinodedb[self.db_name]

    def get_dbdata(self, query, proj={}):
        """Item data from database

        Returns:
            dict: _description_
        """
        dbdata = self.db.find_one(query, proj)
        return dbdata

    @property
    def dbdata(self):
        """Item data from database

        Returns:
            dict: _description_
        """
        query = {"uuid": self.uuid}
        dbdata = self.get_dbdata(query)
        return dbdata

    @property
    def state(self):
        return self.getstate()

    def getstate(self):
        query = {"uuid": self.uuid}
        state = self.db.find_one(query, {"state": 1})["state"]
        return state

    @state.setter
    def state(self, value):
        self.update_db_keys({"state": value})

    @property
    def action(self):
        query = {"uuid": self.uuid}
        # print("query: ", query, "db name: ", self.db_name)
        action = self.db.find_one(query, {"action": 1})["action"]
        return action

    @action.setter
    def action(self, value):
        self.update_db_keys({"action": value})

    def pause(self):
        self.state = "PAUSED"
        self.action = "NONE"
        print("Node {} was paused.".format(self.name))

    def play(self):
        self.state = "READY"
        self.action = "LAUNCH"
        print("Node {} was played.".format(self.name))

    def cancel(self):
        self.action = "CANCEL"

    def skip(self):
        self.state = "SKIPPED"
        print("Node {} was skipped".format(self.name))
        self.action = "NONE"

    def update_db_keys(self, items={}):
        """update data and state to database"""
        query = {"uuid": self.uuid}
        newvalues = {"$set": items}
        self.db.update_one(query, newvalues)

    def push_db_keys(self, items={}):
        """update data and state to database"""
        query = {"uuid": self.uuid}
        newvalues = {"$push": items}
        self.db.update_one(query, newvalues)

    def copy(self, name):
        """Copy a item and insert it to the database."""
        import uuid

        record = self.db.find_one({"uuid": self.uuid}, {"_id": 0})
        # change name and uuid
        record["name"] = name
        record["uuid"] = str(uuid.uuid1())
        self.insert_one(record)
        return record
