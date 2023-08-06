class Executor:
    """Base-class for all executors.

    Prepare and run the code.
    """

    def __init__(self, dbdata={}, daemon_name="localhost", **kwargs) -> None:
        """init a instance of executor.

        Args:
            dbdata (dict, optional): data of the node. Defaults to {}.
            daemon_name (str, optional): name of the daemon. Defaults to "localhost".
        """
        self.kwargs = kwargs
        self.dbdata = dbdata
        self.daemon_name = daemon_name
        self.uuid = dbdata["uuid"]
        self.nodetree_uuid = dbdata["meta"]["nodetree_uuid"]
        self.name = dbdata["name"]
        self.load_data()

    def get_daemon_config(self):
        """Get daemon data by the daemon name

        Returns:
            dict: daemon configuration
        """
        from scinode.daemon.config import DaemonConfig

        daemon = DaemonConfig()
        datas = daemon.datas
        for data in datas:
            if data["name"] == self.daemon_name:
                return data
        return None

    @property
    def daemon_workdir(self):
        data = self.get_daemon_config()
        return data["workdir"]

    def before_run(self):
        """Prepare data before run."""
        pass

    def after_run(self):
        """Handler data after run."""
        pass

    def load_data(self):
        pass

    def run(self):
        """Run the job."""
        pass

    def cancel(self):
        """callback for cancellation."""
        pass
