import click
from scinode.core.db_nodetree import DBNodeTree


@click.group(help="CLI tool to manage node.")
def node():
    pass


@node.command(help="Reset node and its branch in the database.")
@click.option("--name", help="Name of the node.")
@click.option("--index", help="Index of the node.", type=int)
@click.option("--state", help="State of the node.")
@click.option("--uuid", help="uuid of the node.")
def reset(name, index, uuid, state):
    from scinode.database.client import scinodedb

    query = {}
    if name:
        query["name"] = {"$regex": name}
    if index:
        query["index"] = index
    if uuid:
        query["uuid"] = uuid
    if state:
        query["state"] = state
    items = scinodedb["node"].find(
        query, {"_id": 0, "name": 1, "meta.nodetree_uuid": 1}
    )
    if items is None:
        return
    for item in items:
        msg = f"{item['meta']['nodetree_uuid']},node,{item['name']}:action:RESET"
        scinodedb["broker"].update_one({"name": "scinode"}, {"$push": {"msg": msg}})


@node.command(help="Show nodes.")
@click.option("-n", "--name", help="Name of the item.")
@click.option("-i", "--index", help="Index of the item.", type=int)
@click.option("--state", help="State of the item.")
@click.option("--uuid", help="uuid of the item.")
@click.option("--action", help="Action of the item.")
@click.option("--limit", help="Limit of the item.", type=int, default=100)
def list(name, index, uuid, state, action, limit):
    from scinode.database.node import NodeClient

    client = NodeClient()
    query = {}
    if name:
        query["name"] = {"$regex": name}
    if index:
        query["index"] = index
    if uuid:
        query["uuid"] = uuid
    if state:
        query["state"] = state
    if action:
        query["action"] = action
    client.list(query, limit)


@node.command(help="Show the data of a node.")
@click.argument("index", type=int)
@click.option("--all", is_flag=True, help="All node data.")
def show(index, all):
    from scinode.database.node import NodeClient

    client = NodeClient()
    query = {}
    query["index"] = index
    client.show(query, all=all)


@node.command(help="Show the log of a node.")
@click.argument("index", type=int)
def log(index):
    from scinode.database.node import NodeClient

    client = NodeClient()
    query = {}
    query["index"] = index
    client.log(query)


@node.command(help="Delete nodes.")
@click.option("-n", "--name", help="Name of the item.")
@click.option("-i", "--index", help="Index of the item.", type=int)
@click.option("--uuid", help="uuid of the item.")
@click.option("--state", help="State of the item.")
@click.option("--action", help="Action of the item.")
@click.confirmation_option(prompt="Are you sure you want to delete the items?")
def delete(name, index, uuid, state, action):
    from scinode.database.node import NodeClient

    client = NodeClient()
    query = {}
    if name:
        query["name"] = {"$regex": name}
    if index:
        query["index"] = index
    if uuid:
        query["uuid"] = uuid
    if state:
        query["state"] = state
    if action:
        query["action"] = action
    client.delete("node", query)


@node.command(help="Pause nodes.")
@click.option("-n", "--name", help="Name of the item.")
@click.option("-i", "--index", help="Index of the item.", type=int)
@click.option("--state", help="State of the item.")
@click.option("--uuid", help="uuid of the item.")
@click.option("--action", help="Action of the item.")
# @click.confirmation_option(prompt='Are you sure you want to delete the items?')
def pause(name, index, uuid, state, action):
    from scinode.database.client import scinodedb

    query = {}
    if name:
        query["name"] = {"$regex": name}
    if index:
        query["index"] = index
    if uuid:
        query["uuid"] = uuid
    if state:
        query["state"] = state
    if action:
        query["action"] = action
    items = scinodedb["node"].find(
        query, {"_id": 0, "name": 1, "meta.nodetree_uuid": 1}
    )
    if items is None:
        return
    for item in items:
        msg = f"{item['meta']['nodetree_uuid']},node,{item['name']}:state:PAUSED"
        scinodedb["broker"].update_one({"name": "scinode"}, {"$push": {"msg": msg}})
        click.secho(f'Pause node: {item["name"]} successfully!', fg="green")


@node.command(help="Play nodes.")
@click.option("-n", "--name", help="Name of the item.")
@click.option("-i", "--index", help="Index of the item.", type=int)
@click.option("--state", help="State of the item.")
@click.option("--uuid", help="uuid of the item.")
@click.option("--action", help="Action of the item.")
# @click.confirmation_option(prompt='Are you sure you want to delete the items?')
def play(name, index, uuid, state, action):
    from scinode.database.client import scinodedb

    query = {}
    if name:
        query["name"] = {"$regex": name}
    if index:
        query["index"] = index
    if state:
        query["state"] = state
    if uuid:
        query["uuid"] = uuid
    if action:
        query["action"] = action
    items = scinodedb["node"].find(
        query, {"_id": 0, "name": 1, "meta.nodetree_uuid": 1}
    )
    if items is None:
        return
    for item in items:
        msg = f"{item['meta']['nodetree_uuid']},node,{item['name']}:state:CREATED"
        scinodedb["broker"].update_one({"name": "scinode"}, {"$push": {"msg": msg}})
        click.secho(f'Play node: {item["name"]} successfully!', fg="green")


@node.command(help="Cancel nodes. Warning: cancel won't stop running tasks.")
@click.option("-n", "--name", help="Name of the item.")
@click.option("-i", "--index", help="Index of the item.", type=int)
@click.option("--state", help="State of the item.")
@click.option("--uuid", help="uuid of the item.")
@click.option("--action", help="Action of the item.")
# @click.confirmation_option(prompt='Are you sure you want to delete the items?')
def cancel(name, index, uuid, state, action):
    from scinode.database.client import db_node

    query = {}
    if name:
        query["name"] = {"$regex": name}
    if index:
        query["index"] = index
    if uuid:
        query["uuid"] = uuid
    if state:
        query["state"] = state
    if action:
        query["action"] = action
    items = db_node.find(query, {"_id": 0, "name": 1, "meta.nodetree_uuid": 1})
    if items is None:
        return
    nt = DBNodeTree(uuid=items[0]["meta"]["nodetree_uuid"])
    for item in items:
        nt.cancel_node(name=item["name"])


@node.command(help="Kill nodes.")
@click.option("-n", "--name", help="Name of the item.")
@click.option("-i", "--index", help="Index of the item.", type=int)
@click.option("--state", help="State of the item.")
@click.option("--uuid", help="uuid of the item.")
@click.option("--action", help="Action of the item.")
# @click.confirmation_option(prompt='Are you sure you want to delete the items?')
def kill(name, index, uuid, state, action):
    from scinode.database.client import db_node

    query = {}
    if name:
        query["name"] = {"$regex": name}
    if index:
        query["index"] = index
    if uuid:
        query["uuid"] = uuid
    if state:
        query["state"] = state
    if action:
        query["action"] = action
    items = db_node.find(query, {"_id": 0, "name": 1, "meta.nodetree_uuid": 1})
    if items is None:
        return
    nt = DBNodeTree(uuid=items[0]["meta"]["nodetree_uuid"])
    for item in items:
        nt.kill_node(name=item["name"])


@node.command(help="Edit the data of a node.")
@click.argument("index", type=int)
def edit(index):
    from scinode.database.node import NodeClient

    client = NodeClient()
    query = {}
    query["index"] = index
    current_node, data = client.get_yaml_data(query)
    node_edit = click.edit(current_node, extension=".toml")
    # print(node_edit)
    if node_edit:
        nt = DBNodeTree(uuid=data["meta"]["nodetree_uuid"])
        nt.edit_node_from_yaml(uuid=data["uuid"], string=node_edit)
        click.secho(f'Edit node {data["name"]} successfully!', fg="green")


@node.command(help="Set property of node.")
@click.argument("property", type=str)
@click.argument("value")
@click.option("-n", "--name", help="Name of the item.")
@click.option("-i", "--index", help="Index of the item.", type=int)
@click.option("--state", help="State of the item.")
@click.option("--uuid", help="uuid of the item.")
@click.option("--action", help="Action of the item.")
def set(property, value, name, index, uuid, state, action):
    from scinode.database.client import db_node

    query = {}
    if name:
        query["name"] = {"$regex": name}
    if index:
        query["index"] = index
    if uuid:
        query["uuid"] = uuid
    if state:
        query["state"] = state
    if action:
        query["action"] = action
    items = db_node.find(query, {"_id": 0, "name": 1, "meta.nodetree_uuid": 1})
    if items is None:
        return
    data = {str(property): value}
    # print(data)
    for item in items:
        nt = DBNodeTree(uuid=item["meta"]["nodetree_uuid"])
        nt.set_node_property(item["name"], data)
        click.secho(
            f'Set Nodetree: {nt.name}, Node: {item["name"]}, Property: {property}, Value: {value}',
            fg="green",
        )


def abort_if_false(ctx, param, value):
    print(param)
    if not value:
        ctx.abort()
