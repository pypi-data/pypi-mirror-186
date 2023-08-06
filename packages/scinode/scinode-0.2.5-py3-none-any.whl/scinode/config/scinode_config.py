from scinode.config.base_config import Config
import pandas as pd
import os


class ScinodeConfig(Config):
    """Configuration for SciNode."""

    name = "config"

    def __init__(self) -> None:
        super().__init__()

    def loadDatas(self):
        """Load datas
        1) first from environment variable
        2) if not found, then from json file.

        Returns:
            list: a list of the configuration datas.
        """
        import json
        import os

        # first from environment variable
        db_address = os.environ.get("scinode_db_address", None)
        db_name = os.environ.get("scinode_db_name", None)
        computer = os.environ.get("scinode_computer", None)
        if db_address and db_name and computer:
            datas = {"computer": computer, "db_address": db_address, "db_name": db_name}
            return datas
        # then read json file
        if os.path.exists(self.config_file):
            with open(self.config_file, "r") as f:
                datas = json.load(f)
        else:
            # set default
            datas = {"computer": "test", "db_address": "mongodb://localhost:27017/", "db_name": "scinode_db"}
        return datas

    def show(self):
        datas = self.datas
        print("")
        print("Computer:    {}".format(datas["computer"]))
        print("DB address:  {}".format(datas["db_address"]))
        print("DB name:     {}\n".format(datas["db_name"]))


dbconfig = ScinodeConfig()
db_config_datas = dbconfig.loadDatas()
