import pkg_resources


def register(pool, entries, entry_point_type="Node"):
    for entry in entries:
        if entry.identifier not in pool:
            pool[entry.identifier] = entry
        else:
            raise Exception(
                "{} {} is already registered.".format(
                    entry_point_type, entry.identifier
                )
            )


def get_entries(entry_point_name, entry_point_type="Node"):
    pool = {}
    for entry_point in pkg_resources.iter_entry_points(entry_point_name):
        new_entries = entry_point.load()
        register(pool, new_entries, entry_point_type)
    return pool


def get_time(total_seonds):
    d = divmod(total_seonds, 86400)  # days
    h = divmod(d[1], 3600)  # hours
    m = divmod(h[1], 60)  # minutes
    s = m[1]  # seconds
    t = "{:d}d-{:d}h-{:d}m".format(d[0], h[0], m[0])
    return t


def load_nodetree(uuid):
    from scinode.nodetree import NodeTree

    nt = NodeTree.load_data_from_db(uuid)
    return nt


def load_node(uuid):
    from scinode.core.node import Node

    node = Node.load_data_from_db(uuid)
    return node


def load_yaml(filename=None, string=None):
    import yaml

    # load data
    if filename:
        with open(filename, "r") as f:
            data = yaml.safe_load(f)
    elif string:
        data = yaml.safe_load(string)
    else:
        raise Exception("Please specific a filename or yaml string.")
    return data
