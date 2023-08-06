import click
from pathlib import Path


@click.group(help="CLI tool to manage configuration. e.g. database.")
def config():
    pass


@config.command(help="Reset database.")
@click.confirmation_option(
    prompt="This will delete all data in the database. Are you reset?"
)
def reset():
    from scinode.database.db import ScinodeDB

    db = ScinodeDB()
    for name in ["nodetree", "node", "daemon"]:
        db.reset(name)


@config.command(help="Setup profile")
@click.option("--file", help="Read configuration from file.", type=str)
def setup(file):
    import socket
    from scinode.config import ScinodeConfig

    config = ScinodeConfig()
    if file:
        import json

        with open(file, "r") as f:
            datas = json.load(f)
            config.saveDatas(datas)
    else:
        computer = click.prompt("Name of the computer:", default=socket.gethostname())
        db_address = click.prompt(
            "Address of mongodb service:", default="mongodb://localhost:27017/"
        )
        db_name = click.prompt("Name of the database:", default="scinode_db")
        datas = {
            "computer": computer,
            "db_address": db_address,
            "db_name": db_name,
        }
        config.saveDatas(datas)


@config.command(help="Show profile")
def show():
    from scinode.config.scinode_config import ScinodeConfig

    config = ScinodeConfig()
    config.show()
