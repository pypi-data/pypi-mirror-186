import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class NodeSocket:
    """Socket object.
    Input and ouput sockets of a Node.

    Attributes:
        name (str): socket name.
        node (Node): node this socket belongs to.
        type (str): socket type.
        index (int): index of this socket in the SocketCollection.
        links (list): links
        property (unknown):
        link_limit (int): maxminum number of link.
    """

    identifier: str = "NodeSocket"
    default_value: float = 0.0
    link_limit: int = 1

    def __init__(self, name, node=None, type="INPUT", index=0, property=None) -> None:
        """Init a instance of NodeSocket.

        Args:
            name (str): name of the socket
            node (_type_, optional): _description_. Defaults to None.
            index (int, optional): _description_. Defaults to 0.
        """
        self.name = name
        self.node = node
        self.type = type
        self.index = index
        self.links = []
        self.property = property

    def to_dict(self):
        """Export to a dictionary.
        Data to be saved to database. For basic JSON support.
        """
        # data from socket itself
        dbdata = {
            "name": self.name,
            "identifier": self.identifier,
            "type": self.type,
            "link_limit": self.link_limit,
            "links": [],
        }
        # data from linked sockets
        for link in self.links:
            if self.type == "INPUT":
                dbdata["links"].append(
                    {
                        "from_node": link.from_node.name,
                        "from_socket": link.from_socket.name,
                    }
                )
            else:
                dbdata["links"].append(
                    {
                        "to_node": link.to_node.name,
                        "to_socket": link.to_socket.name,
                    }
                )
        return dbdata

    def add_link(self, link):
        """Handle multi-link here"""
        pass

    def add_property(self, property):
        """"""
        self.property = property

    @classmethod
    def from_dict(cls, data):
        """Rebuild Socket object from dictionary representation."""
        socket = cls(data["name"], type=data["type"])
        return socket

    @property
    def value(self):
        return self.node.properties[self.name].value

    @value.setter
    def value(self, value):
        self.node.properties[self.name].value = value

    def __repr__(self) -> str:
        s = ""
        s += 'NodeSocekt(name="{}", node="{}", links = ['.format(self.name, self.node)
        for link in self.links:
            s += '"{}", '.format(link)
        s += "])\n"
        return s
