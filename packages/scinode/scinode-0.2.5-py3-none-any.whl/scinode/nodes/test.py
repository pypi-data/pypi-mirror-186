from scinode.core.node import Node


class TestFloat(Node):
    identifier = "TestFloat"
    name = "TestFloat"
    catalog = "Test"

    kwargs = ["t", "Float"]

    def create_properties(self):
        self.properties.new("Int", "t", data={"default": 1})
        self.properties.new("Float", "Float", data={"default": 0.0})

    def create_sockets(self):
        self.outputs.new("Float", "Float")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "test_float",
        }


class TestString(Node):
    identifier = "TestString"
    name = "String"
    catalog = "Test"

    kwargs = ["t", "String"]

    def create_properties(self):
        self.properties.new("Int", "t", data={"default": 1})
        self.properties.new("String", "String", data={"default": ""})

    def create_sockets(self):
        self.outputs.new("String", "String")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "test_string",
        }


class TestAdd(Node):

    identifier: str = "TestAdd"
    name = "TestAdd"
    catalog = "Test"
    kwargs = ["t", "x", "y"]

    def create_properties(self):
        self.properties.new("Int", "t", data={"default": 1})
        self.properties.new("Float", "x", data={"default": 0})
        self.properties.new("Float", "y", data={"default": 0})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("Float", "x")
        self.inputs.new("Float", "y")
        self.outputs.new("Float", "Result")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "test_add",
        }


class TestMinus(Node):

    identifier: str = "TestMinus"
    name = "TestMinus"
    catalog = "Test"
    kwargs = ["t", "x", "y"]

    def create_properties(self):
        self.properties.new("Int", "t", data={"default": 1})
        self.properties.new("Float", "x", data={"default": 0})
        self.properties.new("Float", "y", data={"default": 0})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("Float", "x")
        self.inputs.new("Float", "y")
        self.outputs.new("Float", "Result")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "test_minus",
        }


class TestPower(Node):

    identifier: str = "TestPower"
    name = "TestAdd"
    catalog = "Test"
    kwargs = ["t", "x", "y"]

    def create_properties(self):
        self.properties.new("Int", "t", data={"default": 1})
        self.properties.new("Float", "x", data={"default": 0})
        self.properties.new("Float", "y", data={"default": 0})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("Float", "x")
        self.inputs.new("Float", "y")
        self.outputs.new("Float", "Result")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "test_power",
        }


class TestGreater(Node):

    identifier: str = "TestGreater"
    name = "TestGreater"
    catalog = "Test"
    kwargs = ["t", "x", "y"]

    def create_properties(self):
        self.properties.new("Int", "t", data={"default": 1})
        self.properties.new("Float", "x", data={"default": 0})
        self.properties.new("Float", "y", data={"default": 0})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("Float", "x")
        self.inputs.new("Float", "y")
        self.outputs.new("Float", "Result")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "test_greater",
        }


class TestLess(Node):

    identifier: str = "TestLess"
    name = "TestLess"
    catalog = "Test"
    kwargs = ["t", "x", "y"]

    def create_properties(self):
        self.properties.new("Int", "t", data={"default": 1})
        self.properties.new("Float", "x", data={"default": 0})
        self.properties.new("Float", "y", data={"default": 0})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("Float", "x")
        self.inputs.new("Float", "y")
        self.outputs.new("Float", "Result")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "test_less",
        }


class TestSqrt(Node):

    identifier: str = "TestSqrt"
    name = "TestSqrt"
    catalog = "Test"
    kwargs = ["t", "x"]

    def create_properties(self):
        self.properties.new("Int", "t", data={"default": 1})
        self.properties.new("Float", "x", data={"default": 1})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("Float", "x")
        self.outputs.new("Float", "Result")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "test_sqrt",
        }


class TestRange(Node):

    identifier: str = "TestRange"
    name = "Range"
    catalog = "Test"
    kwargs = ["start", "stop", "step"]

    def create_properties(self):
        self.properties.new("Float", "start", data={"default": 1})
        self.properties.new("Float", "stop", data={"default": 5})
        self.properties.new("Float", "step", data={"default": 1})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.outputs.new("Float", "Result")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "test_range",
        }


class TestWriteFile(Node):
    identifier = "TestWriteFile"
    name = "WriteFile"
    catalog = "Test"

    kwargs = ["Directory", "Filename", "Content"]

    def create_properties(self):
        self.properties.new("String", "Directory", data={"default": "test"})
        self.properties.new("String", "Filename", data={"default": "abc"})
        self.properties.new("String", "Content", data={"default": "abc"})

    def create_sockets(self):
        self.outputs.new("String", "Filepath")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "TestWriteFile",
            "type": "class",
        }


class TestPerson(Node):

    identifier: str = "TestPerson"
    name = "Person"
    catalog = "Test"
    args = ["name", "age"]

    def create_properties(self):
        self.properties.new("Float", "name", data={"default": "Bob"})
        self.properties.new("Float", "age", data={"default": 5})

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.outputs.new("General", "Person")

    def get_executor(self):
        return {
            "path": "scinode.executors.test",
            "name": "person",
            "type": "function",
        }


node_list = [
    TestFloat,
    TestString,
    TestPower,
    TestAdd,
    TestMinus,
    TestGreater,
    TestLess,
    TestSqrt,
    TestRange,
    TestWriteFile,
    TestPerson,
]
