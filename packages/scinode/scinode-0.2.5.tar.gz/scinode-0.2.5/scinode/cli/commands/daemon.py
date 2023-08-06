import click
from pathlib import Path
import os


@click.group(help="CLI tool to manage Daemon.")
def daemon():
    pass


@daemon.command(help="Start the daemon.")
@click.argument("name", default="localhost", type=str)
@click.option(
    "--pool",
    type=click.Choice(["thread", "process"], case_sensitive=False),
    default="thread",
)
@click.option("--worker", default=0, help="Sleep time")
@click.option("--foreground", is_flag=True, default=False, help="Use foreground mode")
@click.option("--sleep", default=1, help="Sleep time")
def start(name, pool, worker, foreground, sleep):
    from scinode.daemon.daemon import ScinodeDaemon
    from scinode.profile import ScinodeProfile
    from scinode.database.client import scinodedb
    from scinode.database.daemon import DaemonClient

    p = ScinodeProfile()
    computer = p.load_activate_profile()["computer"]
    data = scinodedb["daemon"].find_one({"name": name, "computer": computer})
    if data is None:
        print(
            "\nWarning!!! Daemon {} on computer: {} is not setup.\n".format(
                name, computer
            )
        )
        print("Please setup a new one or choose daemon from:")
        client = DaemonClient()
        client.show({"computer": computer})
        return
    daemon = ScinodeDaemon(name, pool=pool, worker=worker, sleep=sleep)
    print("Start daemon {}, sleep: {}".format(daemon.name, sleep))
    if foreground:
        daemon.run()
    else:
        daemon.start()


@daemon.command(help="Stop the daemon.")
@click.argument("name", default="localhost", type=str)
def stop(name):
    from scinode.daemon.daemon import ScinodeDaemon

    daemon = ScinodeDaemon(name)
    daemon.stop()


@daemon.command(help="Restart the daemon.")
@click.argument("name", default="localhost", type=str)
@click.option(
    "--pool",
    type=click.Choice(["thread", "process"], case_sensitive=False),
    default="thread",
)
@click.option("--worker", default=0, help="Sleep time")
@click.option("--sleep", default=1, help="Sleep time")
@click.confirmation_option(prompt="Does the daemon run on this computer?")
def restart(name, pool, worker, sleep):
    from scinode.daemon.daemon import ScinodeDaemon

    daemon = ScinodeDaemon(name, pool=pool, worker=worker, sleep=sleep)
    daemon.restart()


@daemon.command(help="Show the log file of the daemon.")
@click.option("--limit", help="Number of lines to be shown.", default=100, type=int)
@click.argument("name", default="localhost", type=str)
def log(name, limit):
    from scinode.daemon.daemon import ScinodeDaemon

    daemon = ScinodeDaemon(name=name)
    daemon.showlog(limit)


@daemon.command(help="Add new daemon.")
@click.option("--file", help="Read configuration from file.", type=str)
def add(file):
    from scinode.daemon.config import DaemonConfig

    if file:
        DaemonConfig.add_from_json(file)
    else:
        default_path = str(os.path.join(Path.home(), "scinode"))
        name = click.prompt("Name of this daemon:", default="localhost")
        broker = click.prompt(
            "Use this daemon for message broker:", default="Yes", type=bool
        )
        workdir = click.prompt("Default working directory:", default=default_path)
        sleep = click.prompt("Sleep time:", default=1)
        print("broker: ", broker)
        config = DaemonConfig(name=name, workdir=workdir, sleep=sleep, broker=broker)
        config.save_to_db()


@daemon.command(help="Delete daemons.")
@click.argument("name")
@click.confirmation_option(prompt="Are you sure you want to delete the daemons?")
def delete(name):
    from scinode.daemon.daemon import ScinodeDaemon
    from scinode.database.client import scinodedb
    from scinode.database.daemon import DaemonClient
    import datetime

    client = DaemonClient()
    query = {"name": name}
    datas = scinodedb["daemon"].find_one(query, {"_id": 0})
    daemon = ScinodeDaemon(name=datas["name"])
    d = daemon.data
    t = int((datetime.datetime.utcnow() - d["lastUpdate"]).total_seconds())
    if t < 2 * d["sleep"]:
        print(
            "Daemon {} is likely running now. Please stop it first.".format(
                datas["name"]
            )
        )
    else:
        print("Delete daemon: {}".format(datas["name"]))
        client.delete("daemon", {"uuid": datas["uuid"]})


@daemon.command(help="List daemons.")
@click.option("--name", help="Name of the item.")
@click.option("--index", help="Index of the item.", type=int)
@click.option("--uuid", help="uuid of the item.")
@click.option("--state", help="state of the item.")
def list(name, index, uuid, state):
    from scinode.database.daemon import DaemonClient

    client = DaemonClient()
    query = {}
    if name:
        query["name"] = name
    if index:
        query["index"] = index
    if uuid:
        query["uuid"] = uuid
    if state:
        query["state"] = state
    client.list(query)


@daemon.command(help="Show the data of a daemon.")
@click.argument("index", type=int)
def show(index):
    from scinode.database.daemon import DaemonClient

    client = DaemonClient()
    query = {}
    query["index"] = index
    client.show(query)
