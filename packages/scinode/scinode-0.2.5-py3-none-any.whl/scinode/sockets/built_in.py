from scinode.core.socket import NodeSocket


class SocketGeneral(NodeSocket):
    """General socket."""

    identifier: str = "General"
    default_value: float = None

    def __init__(self, name, node=None, type="INPUT", index=0) -> None:
        super().__init__(name, node, type, index)


class SocketFloat(NodeSocket):
    """Float socket."""

    identifier: str = "Float"
    default_value: float = 0.0

    def __init__(self, name, node=None, type="INPUT", index=0) -> None:
        super().__init__(name, node, type, index)


class SocketInt(NodeSocket):
    """Int socket."""

    identifier: str = "Int"
    default_value: int = 0

    def __init__(self, name, node=None, type="INPUT", index=0) -> None:
        super().__init__(name, node, type, index)


class SocketString(NodeSocket):
    """String socket."""

    identifier: str = "String"
    default_value: str = ""

    def __init__(self, name, node=None, type="INPUT", index=0) -> None:
        super().__init__(name, node, type, index)


class SocketBool(NodeSocket):
    """Bool socket."""

    identifier: str = "Bool"
    default_value: bool = False

    def __init__(self, name, node=None, type="INPUT", index=0) -> None:
        super().__init__(name, node, type, index)


socket_list = [
    SocketGeneral,
    SocketInt,
    SocketFloat,
    SocketString,
    SocketBool,
]
