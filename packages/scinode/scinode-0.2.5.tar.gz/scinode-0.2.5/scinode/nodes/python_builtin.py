from scinode.core.node import Node


class IntNode(Node):
    """Output a int value."""

    identifier = "Int"
    name = "Int"

    args = ["Value"]

    def create_properties(self):
        self.properties.new("Int", "Value", data={"default": 0})

    def create_sockets(self):
        self.outputs.new("Int", "Result")

    def get_executor(self):
        return {
            "path": "builtins",
            "name": "int",
            "type": "function",
        }


class FloatNode(Node):
    """Output a float value."""

    identifier = "Float"
    name = "Float"

    args = ["Value"]

    def create_properties(self):
        self.properties.new("Float", "Value", data={"default": 0.0})

    def create_sockets(self):
        self.outputs.new("Float", "Result")

    def get_executor(self):
        return {
            "path": "builtins",
            "name": "float",
            "type": "function",
        }


class BoolNode(Node):
    """Output a bool value."""

    identifier = "Bool"
    name = "Bool"

    args = ["Value"]

    def create_properties(self):
        self.properties.new("Bool", "Value", data={"default": True})

    def create_sockets(self):
        self.outputs.new("Bool", "Result")

    def get_executor(self):
        return {
            "path": "builtins",
            "name": "bool",
            "type": "function",
        }


class StrNode(Node):
    """Output a string."""

    identifier = "Str"
    name = "Str"

    args = ["Value"]

    def create_properties(self):
        self.properties.new("String", "Value", data={"default": ""})

    def create_sockets(self):
        self.outputs.new("String", "Result")

    def get_executor(self):
        return {
            "path": "builtins",
            "name": "str",
            "type": "function",
        }


class Getattr(Node):
    """The Getattr node sets the value of the attribute of an object.

    Executor:
        Python builtin function: getattr()

    Results:
        A pyhont object.

    Example:

    >>> att = nt.nodes.new("Getattr")
    >>> att.properties["Name"].value = "real"

    """

    identifier: str = "Getattr"
    node_type: str = "Normal"

    def create_properties(self):
        self.properties.new("String", "Name", data={"default": "__class__"})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("General", "Source")
        self.inputs.new("General", "Name")
        self.outputs.new("General", "Result")
        self.args = ["Source", "Name"]

    def get_executor(self):
        return {
            "path": "builtins",
            "name": "getattr",
            "type": "function",
        }


class Setattr(Node):
    """The Setattr node sets the value of the attribute of an object.

    Executor:
        Python builtin function: setattr()

    Results:
        A pyhont object.

    Example:

    >>> nt = NodeTree(name="test_setattr")
    >>> person1 = nt.nodes.new("TestPerson", "person1")
    >>> str1 = nt.nodes.new("TestString", "str1")
    >>> str1.properties["String"].value = "Peter"
    >>> att = nt.nodes.new("Setattr")
    >>> att.properties["Name"].value = "name"
    >>> nt.links.new(person1.outputs[0], att.inputs["Source"])
    >>> nt.links.new(str1.outputs[0], att.inputs["Value"])

    """

    identifier: str = "Setattr"
    node_type: str = "Normal"

    def create_properties(self):
        self.properties.new("String", "Name", data={"default": "__class__"})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("General", "Source")
        self.inputs.new("General", "Name")
        self.inputs.new("General", "Value")
        self.outputs.new("General", "Result")
        self.args = ["Source", "Name", "Value"]

    def get_executor(self):
        return {
            "path": "scinode.executors.python",
            "name": "setattr",
            "type": "function",
        }


class Getitem(Node):
    """The Getitem node suppors index lookups.

    Executor:
        Python builtin function: __getitem__()

    Results:
        A pyhont object.

    Example:

    >>> getitem1 = nt.nodes.new("Getitem", "getitem1")
    >>> arange1 = nt.nodes.new("ScinodeNumpy", "arange")
    >>> arange1.set({"function": "arange", "start": 1, "stop": 5, "step": 2})
    >>> nt.links.new(nt.nodes["power1"].outputs[0], getitem1.inputs["Source"])
    >>> nt.links.new(arange1.outputs[0], getitem1.inputs["Index"])
    """

    identifier: str = "Getitem"
    node_type: str = "Normal"

    def create_properties(self):
        self.properties.new("Int", "Index", data={"default": 0})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("General", "Source")
        self.inputs.new("General", "Index")
        self.outputs.new("General", "Result")
        self.args = ["Source", "Index"]

    def get_executor(self):
        return {
            "path": "scinode.executors.python",
            "name": "getitem",
            "type": "function",
        }


class Setitem(Node):
    """The Setitem node is used for assigning a value to an item.

    Executor:
        Python builtin function: __setitem__()

    Results:
        A pyhont object.

    Example:

    >>> setitem1 = nt.nodes.new("Setitem", "setitem1")
    >>> arange1 = nt.nodes.new("ScinodeNumpy", "arange")
    >>> arange1.set({"function": "arange", "start": 1, "stop": 5, "step": 2})
    >>> linspace2 = nt.nodes.new("ScinodeNumpy", "linspace2")
    >>> linspace2.set({"function": "linspace", "start": 11, "stop": 15, "num": 2})
    >>> nt.links.new(nt.nodes["linspace1"].outputs[0], setitem1.inputs["Source"])
    >>> nt.links.new(arange1.outputs[0], setitem1.inputs["Index"])
    >>> nt.links.new(linspace2.outputs[0], setitem1.inputs["Value"])
    """

    identifier: str = "Setitem"
    node_type: str = "Normal"

    def create_properties(self):
        self.properties.new("Int", "Index", data={"default": 0})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("General", "Source")
        self.inputs.new("General", "Index")
        self.inputs.new("General", "Value")
        self.outputs.new("General", "Result")
        self.args = ["Source", "Index", "Value"]

    def get_executor(self):
        return {
            "path": "scinode.executors.python",
            "name": "setitem",
            "type": "function",
        }


node_list = [
    IntNode,
    FloatNode,
    BoolNode,
    StrNode,
    Getattr,
    Setattr,
    Getitem,
    Setitem,
]
