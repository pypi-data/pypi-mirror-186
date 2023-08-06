from scinode.core.node import Node


class TemplateTest(Node):
    identifier: str = "TemplateTest"
    catalog = "Template"
    name = "Test"
    args = ["text", "float", "enum", "bool", "matrix"]
    kwargs = ["input1", "intpu2"]

    def create_properties(self):

        self.properties.new("String", "text", data={"default": "abc"})

        self.properties.new("Float", "float", data={"default": 10})

        self.properties.new(
            "Enum", "enum", data={"options": ["a", "b", "c"], "default": 0}
        )

        self.properties.new("Bool", "bool", data={"default": True})

        self.properties.new(
            "FloatMatrix",
            "matrix",
            data={"size": [2, 3], "default": [1, 2, 3, 4, 5, 6]},
        )

        self.properties.new("Float", "input1", data={"default": 0})

        self.properties.new(
            "FloatVector", "input2", data={"size": 3, "default": [1, 2, 3]}
        )

    def create_sockets(self):
        self.inputs.clear()
        self.outputs.clear()
        self.inputs.new("Float", "input1")
        self.inputs.new("FloatVector", "input2")
        self.outputs.new("Float", "Output")

    def get_executor(self):
        return {"path": "numpy", "name": "add", "type": "function"}


node_list = [
    TemplateTest,
]
