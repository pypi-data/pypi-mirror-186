scinode_properties = {
    "Int": "Int",
    "Float": "Float",
    "String": "String",
    "Bool": "Bool",
    "FloatVector": "FloatVector",
    "FloatMatrix": "FloatMatrix",
    "Enum": "Enum",
    "Color": "Color",
    "File": "File",
}


template = [
    {
        "name": "Test",
        "meta": {
            "catalog": "Template",
            "args": ["text", "float", "enum", "bool", "matrix"],
            "kwargs": ["input1", "intpu2"],
        },
        "executor": {
            "path": "numpy",
            "name": "add",
            "type": "function",
        },
        "properties": [
            {
                "name": "text",
                "type": "String",
                "defaultVal": "abc",
            },
            {
                "name": "float",
                "type": "Float",
                "defaultVal": 10.0,
            },
            {
                "name": "enum",
                "type": "Enum",
                "defaultVal": 0,
                "options": ["a", "b", "c"],
            },
            {
                "name": "bool",
                "type": "Bool",
                "defaultVal": True,
            },
            {
                "name": "matrix",
                "type": "FloatMatrix",
                "size": [2, 3],
                "defaultVal": [1, 2, 3, 4, 5, 6],
            },
            {
                "name": "input1",
                "type": "Float",
                "defaultVal": 0,
            },
            {
                "name": "input2",
                "type": "FloatVector",
                "size": 3,
                "defaultVal": [1, 2, 3],
            },
        ],
        "inputs": [
            {
                "name": "input1",
                "type": "SocketFloat",
            },
            {
                "name": "input2",
                "type": "SocketFloatVector",
            },
        ],
        "outputs": [
            {
                "name": "Output",
                "type": "SocketFloat",
            },
        ],
    }
]


class NodeFromJson:
    """Create Node class from Json data"""

    def __init__(self, ndata) -> None:

        self.ndata = ndata
        self.identifier = "{}{}".format(ndata["meta"]["catalog"], ndata["name"])

    def build_exec_string_node(self):
        header_string = self.build_header()
        # =============================================
        init_string = self.build_sockets()
        property_string = self.build_properties()
        executor_string = self.build_executor()
        # print(header_string)
        # print(property_string)
        # print(init_string)
        # print(executor_string)
        code = header_string + property_string + init_string + executor_string
        return code

    def build_header(self):
        ndata = self.ndata
        header_string = """
class {0}{1}(Node):
    identifier: str = "{0}{1}"
    catalog = "{0}"
    name = "{1}"
    args = {2}
    kwargs = {3}

    """.format(
            ndata["meta"]["catalog"],
            ndata["name"],
            ndata["meta"]["args"],
            ndata["meta"]["kwargs"],
        )
        return header_string

    def build_properties(self):
        if "properties" not in self.ndata:
            return ""
        s = """
    def create_properties(self):
        """
        for data in self.ndata["properties"]:
            data["default"] = data.pop("defaultVal", None)
            s += """
        self.properties.new("{}", "{}", data={})
        """.format(
                scinode_properties[data.pop("type")], data.pop("name"), data
            )
        if len(self.ndata["properties"]) == 0:
            s += """
        pass
        """
        return s

    def build_sockets(self):
        init_string = """
    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()"""
        inputs = self.ndata["inputs"]
        n = len(inputs)
        for i in range(n):
            data = inputs[i]
            init_string += """
        self.inputs.new("{}", "{}")""".format(
                data["type"], data["name"]
            )
        outputs = self.ndata["outputs"]
        n = len(outputs)
        for i in range(n):
            data = outputs[i]
            init_string += """
        self.outputs.new("{}", "{}")""".format(
                data["type"], data["name"]
            )
        return init_string

    def build_executor(self):
        import json

        s = """
    def get_executor(self):
        return {}
    """.format(
            self.ndata["executor"]
        )
        return s


def build_node_to_py(data):
    import json

    s = """
from scinode.core.node import Node
    """
    nodes = "\nnode_list = ["
    for ndata in data:
        # ndata = json.loads(ndata)
        c = NodeFromJson(ndata)
        s += c.build_exec_string_node()
        nodes += """{0},\n""".format(c.identifier)
    nodes += "]"
    s += nodes
    return s


def save_nodes_to_py(s):
    import pathlib
    import os

    path = pathlib.Path(__file__).parent.resolve()
    with open(os.path.join(path, "node_from_database.py"), "w") as f:
        f.write(s)


def build_nodes_from_db():
    from scinode.database.client import scinodedb

    print("build_nodes_from_db: ")
    data = list(scinodedb["component"].find({}))
    print("Total: {} components".format(len(data)))
    s = build_node_to_py(data)
    save_nodes_to_py(s)


if __name__ == "__main__":
    from scinode.database.client import scinodedb

    data = list(scinodedb["component"].find({}))
    s = build_node_to_py(data)
    save_nodes_to_py(s)
