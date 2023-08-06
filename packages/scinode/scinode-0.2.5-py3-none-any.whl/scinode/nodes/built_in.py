from scinode.core.node import Node


class ScinodeNode(Node):
    identifier: str = "ScinodeNode"
    node_type: str = "Normal"

    def get_executor(self):
        return None


node_list = [
    ScinodeNode,
]
