from pprint import pprint
import logging

logger = logging.getLogger(__name__)
logger.setLevel("DEBUG")


def get_node_data(query, proj={"_id": 0, "results": 0}):
    from scinode.database.client import scinodedb
    import pickle

    ndata = scinodedb["node"].find_one(query, proj)
    for key in ["properties", "results"]:
        if ndata.get(key):
            ndata[key] = pickle.loads(ndata[key])
    return ndata


def yaml_to_dict(node):
    """Convert yaml data into dict."""
    meta = node.get("meta", {})
    meta["identifier"] = node.pop("identifier")
    node["meta"] = meta
    # properties
    properties = {}
    if node.get("properties"):
        for name, p in node["properties"].items():
            properties[name] = {"value": p}
    node["properties"] = properties
    return node


def to_edit_dict(node_full):
    import pickle
    import yaml

    # print("ntdata: ", ntdata)
    nd = {
        "identifier": node_full["meta"]["identifier"],
        "name": node_full["name"],
        "uuid": node_full["uuid"],
        "state": node_full["state"],
        "action": node_full["action"],
        "description": node_full["description"],
        "meta": {
            "daemon_name": node_full["meta"]["daemon_name"],
        },
    }
    if node_full["meta"]["node_type"].upper() == "REF":
        return nd
    # set node_full properties
    properties = node_full.get("properties")
    if properties:
        nd["properties"] = {}
        for name, p in properties.items():
            nd["properties"][name] = p["value"]
    # inputs
    nd["inputs"] = []
    for input in node_full["inputs"]:
        for link in input["links"]:
            link["to_socket"] = input["name"]
            nd["inputs"].append(link)
    return nd


def get_input_parameters_from_db(dbdata):
    """get inputs from database

    The inputs are the outputs of parent nodes and
    the properties of the node itself.

    Returns:
        _type_: _description_
    """
    import pickle

    # get data of the node itself
    paramters = pickle.loads(dbdata.get("properties"))
    # print("data: ", paramters)
    # get inputs sockets data
    inputs = dbdata.get("inputs")
    for input in inputs:
        # un-linked socket
        # print(input["links"])
        if len(input["links"]) == 0:
            logger.debug("un-linked socket")
            if input["name"] not in paramters:
                paramters[input["name"]] = {"value": None}
        elif len(input["links"]) == 1:
            # linked socket
            logger.debug("    single-linked socket")
            link = input["links"][0]
            results = get_node_results(
                query={
                    "meta.nodetree_uuid": dbdata["meta"]["nodetree_uuid"],
                    "name": link["from_node"],
                }
            )
            # print("results of node {}: ".format(link["from_node"]), results)
            if results is None:
                continue
            index = None
            # find the input socket based on socket name
            for i in range(len(results)):
                if results[i]["name"] == link["from_socket"]:
                    index = i
            if index is None:
                raise Exception(
                    "Can not find input socket {}".format(link["from_socket"])
                )
            paramters[input["name"]] = {"value": results[index]["value"]}
        # check multi-input
        elif len(input["links"]) > 1:
            # linked socket
            logger.debug("    multi-linked socket")
            paramters[input["name"]] = {"value": []}
            for link in input["links"]:
                results = get_node_results(
                    query={
                        "meta.nodetree_uuid": dbdata["meta"]["nodetree_uuid"],
                        "name": link["from_node"],
                    }
                )
                if results is None:
                    continue
                index = None
                # find the input socket based on socket name
                for i in range(len(results)):
                    if results[i]["name"] == link["from_socket"]:
                        index = i
                if index is None:
                    raise Exception(
                        "Can not find input socket {}".format(link["from_socket"])
                    )
                # print("    Node: {} socket: {} : ".format(
                # nodes[link["from_node"]]["name"]), results[index]["value"])
                value = results[index]["value"]
                if isinstance(value, dict):
                    paramters[input["name"]]["value"].update(value)
                elif isinstance(value, list):
                    paramters[input["name"]]["value"].extend(value)
                else:
                    paramters[input["name"]]["value"].append(value)
        # print("Input {}".format(input["name"]), paramters[input["name"]])
    return paramters


def inspect_executor_arguments(parameters, args_keys, kwargs_keys):
    """Get the positional and keyword arguments

    Args:
        executor (_type_): _description_
        parameters (_type_): _description_
    """
    args = []
    kwargs = {}
    for key in args_keys:
        args.append(parameters[key]["value"])
    for key in kwargs_keys:
        kwargs[key] = parameters[key]["value"]
    return args, kwargs


def get_node_results(query, proj={"meta": 1, "results": 1}):
    dbdata = get_node_data(query, proj=proj)
    if dbdata is None:
        return None
    elif dbdata["meta"]["node_type"] == "REF":
        dbdata = get_node_data({"uuid": dbdata["meta"]["ref_uuid"]}, proj=proj)
        if dbdata is None:
            return None
        else:
            return dbdata.get("results")
    return dbdata.get("results")


def node_shape(self, data):
    """_summary_

    Args:
        data (_type_): _description_


    =========
    |       o
    |       |
    |t      |
    |x      |
    o       |
    ========
    """
    pass
