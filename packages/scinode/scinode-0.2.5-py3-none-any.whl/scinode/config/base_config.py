from pathlib import Path
import pandas as pd
import os


class Config:
    """Configuration
    Local database using json file.
    """

    name = "base"

    def __init__(self) -> None:
        directory = os.path.join(Path.home(), ".scinode")
        if not os.path.exists(directory):
            os.mkdir(directory)
        self.config_file = os.path.join(directory, "{}.json".format(self.name))

    @property
    def datas(self):
        return self.loadDatas()

    def loadDatas(self):
        """Load datas from json file.

        Returns:
            list: a list of the configuration datas.
        """
        import json
        import os

        # read file
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                datas = json.load(f)
        else:
            datas = []
        return datas

    def saveDatas(self, datas):
        """Save datas into a json file.

        Args:
            datas (list): A list of dict data.
        """
        import json

        with open(self.config_file, "w") as f:
            datas = json.dump(datas, f, indent=4)

    def insert_one(self, item):
        """Insert one item into json file.

        Args:
            item (dict): new data.
        """
        import json

        datas = self.datas
        for data in datas:
            if data["name"] == item["name"]:
                print(
                    "Item {} already exist! Please add another one.".format(
                        item["name"]
                    )
                )
                return
        datas.append(item)
        with open(self.config_file, "w") as f:
            datas = json.dump(datas, f, indent=4)

    def delete(self, query=None, index=None):
        """Delete item in json file by query.

        Args:
            query (dict): query with key and value
        """
        datas = self.datas
        # data to be keeped
        new_datas = []
        if index is not None:
            del datas[index]
            new_datas = datas
        elif query is not None:
            for data in datas:
                match = True
                # compare query
                for key, value in query.items():
                    if data[key] != value:
                        match = False
                        break
                # skip matched item
                if not match:
                    new_datas.append(data)
        self.saveDatas(new_datas)

    def show(self):
        """Show all datas"""
        data = self.config_datas
        df = pd.DataFrame(data)
        if df.empty:
            print("No data found.")
        else:
            print(df)

    def add_from_json(self, file):
        """Load datas from json file.

        Returns:
            list: a list of the configuration datas.
        """
        import json

        # read file
        with open(file, "r") as f:
            datas = json.load(f)
        self.insert_one(datas)
