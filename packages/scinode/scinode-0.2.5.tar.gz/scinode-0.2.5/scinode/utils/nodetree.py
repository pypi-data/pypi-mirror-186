def get_nt_full_data(query):
    from scinode.database.client import scinodedb
    from scinode.utils.node import get_node_data
    import pickle

    ntdata = scinodedb["nodetree"].find_one(query)
    nodes = {}
    for name, node in ntdata["nodes"].items():
        nodes[name] = get_node_data({"uuid": node["uuid"]}, {})
    ntdata["nodes"] = nodes
    return ntdata


def get_nt_short_data(ntdata):
    from copy import deepcopy

    ntdata_short = deepcopy(ntdata)
    for name, node in ntdata["nodes"].items():
        if node["meta"]["node_type"] in ["REF"]:
            node["state"] = "FINISHED"
            node["action"] = "NONE"
        ntdata_short["nodes"][name] = {
            "name": node["name"],
            "identifier": node["meta"]["identifier"],
            "node_type": node["meta"]["node_type"],
            "uuid": node["uuid"],
            "state": node["state"],
            "action": node["action"],
            "daemon": node["meta"]["daemon_name"],
        }
    return ntdata_short


def nt_export_py(ntdata):
    import pickle

    # print("ntdata: ", ntdata)
    s = """
from scinode.nodetree import NodeTree
nt = NodeTree(name="{}", uuid="{}")
""".format(
        ntdata["name"], ntdata["uuid"]
    )
    # nodes
    for name, node in ntdata["nodes"].items():
        # print("node: ", node)
        s += """
node = nt.nodes.new("{}", "{}")
""".format(
            node["meta"]["identifier"], node["name"]
        )
        # set node properties
        properties = pickle.loads(node["properties"])
        for name, p in properties.items():
            # print("\np: ", p)
            if p["value"] == "":
                continue
            if p["type"] in ["String", "Enum"]:
                s += """node.properties["{}"].value = "{}"
""".format(
                    p["name"], p["value"]
                )
            else:
                s += """node.properties["{}"].value = {}
""".format(
                    p["name"], p["value"]
                )

    # links
    for link in ntdata["links"]:
        s += """
nt.links.new(nt.nodes["{}"].outputs["{}"], nt.nodes["{}"].inputs["{}"])""".format(
            link["from_node"],
            link["from_socket"],
            link["to_node"],
            link["to_socket"],
        )

    # launch
    s += """
nt.launch()
"""
    return s


def to_edit_dict(ntdata):
    from scinode.utils.node import to_edit_dict

    # print("ntdata: ", ntdata)
    data = {
        "name": ntdata["name"],
        "uuid": ntdata["uuid"],
        "state": ntdata["state"],
        "action": ntdata["action"],
        "description": ntdata["description"],
        "meta": {
            "version": ntdata["version"],
            "platform": ntdata["meta"]["platform"],
            "daemon_name": ntdata["meta"]["daemon_name"],
        },
    }
    # nodes
    data["nodes"] = []
    for name, node in ntdata["nodes"].items():
        nd = to_edit_dict(node)
        data["nodes"].append(nd)
    return data


def nt_export_yaml(ntdata):
    import yaml

    ntdata = to_edit_dict(ntdata)
    s = yaml.dump(ntdata, sort_keys=False)
    return s


def nt_export_yaml_string(ntdata):
    import pickle

    # print("ntdata: ", ntdata)
    s = f"""
name: {ntdata["name"]}
uuid: {ntdata["uuid"]}
state: {ntdata["state"]}
action: {ntdata["action"]}
description: {ntdata["description"]}
meta:
  version: {ntdata["version"]}
  platform: {ntdata["meta"]["platform"]}
  daemon_name: {ntdata["meta"]["daemon_name"]}
"""
    # nodes
    s += """nodes:"""
    for name, node in ntdata["nodes"].items():
        # print("node: ", node)
        s += f"""
  - identifier: {node["meta"]["identifier"]}
    uuid: {node["uuid"]}
    name: {node["name"]}
    state: {node["state"]}
    action: {node["action"]}
"""
        # set node properties
        properties = node.get("properties")
        if properties:
            s += """    properties:"""
        for name, p in properties.items():
            s += f"""
      {p["name"]}: {p["value"]}"""
    # links
    s += """links:"""
    for link in ntdata["links"]:
        s += f"""
  - from_node: {link["from_node"]}
    from_socket: {link["from_socket"]}
    to_node: {link["to_node"]}
    to_socket: {link["to_socket"]}"""
    return s


def nt_export(query, format="yaml", filename=None):
    """Export nodetree to yaml or python

    Args:
        query (_type_): _description_
        filename (_type_, optional): _description_. Defaults to None.
    """
    ntdata = get_nt_full_data(query)
    if format.upper() == "PYTHON":
        s = nt_export_py(ntdata)
    else:
        s = nt_export_yaml(ntdata)
    if filename:
        with open(filename, "w") as f:
            f.write(s)
    return s


def yaml_to_dict(data):
    """Convert yaml data into dict."""
    ntdata = data
    nodes = ntdata.pop("nodes")
    ntdata["nodes"] = {}
    links = []
    for node in nodes:
        # meta
        meta = node.get("meta", {})
        meta["identifier"] = node.pop("identifier")
        node["meta"] = meta
        # properties
        properties = {}
        if node.get("properties"):
            for name, p in node["properties"].items():
                properties[name] = {"value": p}
        node["properties"] = properties
        # links
        if node.get("inputs"):
            for input in node["inputs"]:
                input["to_node"] = node["name"]
                links.append(input)
        ntdata["nodes"][node["name"]] = node
    ntdata["links"] = links
    return ntdata
