import importlib

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Collection:
    """Collection of instances of a property.
    Like an extended list, with the functions: new, find, delete, clear.

    Attributes:
        path (str): path to import the module.
    """

    path: str = ""

    def __init__(self, parent) -> None:
        """Init a collection instance

        Args:
            parent (unknow): object this collection belongs to.
        """
        self._items = []
        self.parent = parent

    def __iter__(self):
        for item in self._items:
            yield item

    def __getitem__(self, index):
        if isinstance(index, int):
            return self._items[index]
        elif isinstance(index, str):
            return self.get(index)

    def new(self, identifier, name=None):
        """Add new item into this collection.

        Args:
            identifier (str): Class for the new item
            name (str, optional): name of the new item. Defaults to None.

        Returns:
            Class Object: A instance of the class.
        """
        module = importlib.import_module(self.path)
        ItemClass = getattr(module, identifier)
        item = ItemClass(name)
        self._items.append(item)
        return item

    def add(self, item):
        self._items.append(item)

    def get(self, name):
        """Find item by name

        Args:
            name (str): _description_

        Returns:
            _type_: _description_
        """
        for item in self._items:
            if item.name == name:
                return item
        return None

    def get_by_uuid(self, uuid):
        """Find item by uuid

        Args:
            uuid (str): _description_

        Returns:
            _type_: _description_
        """
        for item in self._items:
            if item.uuid == uuid:
                return item
        return None

    def keys(self):
        keys = []
        for item in self._items:
            keys.append(item.name)
        return keys

    def clear(self):
        """Remove all items from this collection."""
        self._items = []

    def __delitem__(self, index):
        del self._items[index]

    def __len__(self):
        return len(self._items)


def decorator_check_name(func):
    """Check name exist or not.

    Args:
        func (_type_): _description_
    """

    def wrapper_func(*args, **kwargs):
        if len(args) > 2 and args[2] in args[0].keys():
            raise Exception(
                "{} already exist, please choose another name.".format(args[1])
            )
        if kwargs.get("name", None) in args[0].keys():
            raise Exception(
                "{} already exist, please choose another name.".format(args[1])
            )
        item = func(*args, **kwargs)
        return item

    return wrapper_func


class NodeTreeCollection(Collection):
    """NodeTree colleciton"""

    path = "scinode.nodetree"

    def __init__(self, parent) -> None:
        super().__init__(parent)

    @decorator_check_name
    def new(self, identifier, name=None):
        module = importlib.import_module(self.path)
        ItemClass = getattr(module, identifier)
        item = ItemClass(name, nodetree=self.parent)
        self._items.append(item)
        return item


class NodeCollection(Collection):
    """Node colleciton"""

    def __init__(self, parent) -> None:
        super().__init__(parent)

    @decorator_check_name
    def new(self, identifier, name=None, uuid=None):
        from scinode.nodes import node_pool
        import difflib

        if identifier not in node_pool:
            nodes = difflib.get_close_matches(identifier, node_pool)
            if len(nodes) == 0:
                msg = "Node: {} is not defined.".format(identifier)
            else:
                msg = "Node: {} is not defined. Do you mean {}".format(
                    identifier, ", ".join(nodes)
                )
            raise Exception(msg)
        ItemClass = node_pool[identifier]
        id = max([0] + [item.id for item in self._items]) + 1
        logger.info("New node, id: {}, name: {}".format(id, name))
        item = ItemClass(id, nodetree=self.parent, name=name, uuid=uuid)
        self._items.append(item)
        return item


class PropertyCollection(Collection):
    """Property colleciton"""

    path = "scinode.core.property"

    def __init__(self, parent) -> None:
        super().__init__(parent)

    @decorator_check_name
    def new(self, identifier, name=None, data={}):
        from scinode.properties import property_pool
        import difflib

        if identifier not in property_pool:
            properties = difflib.get_close_matches(identifier, property_pool)
            if len(properties) == 0:
                msg = "Property: {} is not defined.".format(identifier)
            else:
                msg = "Property: {} is not defined. Do you mean {}".format(
                    identifier, ", ".join(properties)
                )
            raise Exception(msg)
        ItemClass = property_pool[identifier]
        item = ItemClass(name, **data)
        self._items.append(item)
        return item


class InputSocketCollection(Collection):
    """Input Socket colleciton"""

    path = "scinode.core.socket"

    def __init__(self, parent) -> None:
        super().__init__(parent)

    @decorator_check_name
    def new(self, identifier, name=None):
        module = importlib.import_module(self.path)
        ItemClass = getattr(module, identifier)
        item = ItemClass(name, node=self.parent, type="INPUT", index=len(self._items))
        self._items.append(item)
        return item

    @decorator_check_name
    def new(self, identifier, name=None):
        from scinode.sockets import socket_pool
        import difflib

        if identifier not in socket_pool:
            sockets = difflib.get_close_matches(identifier, socket_pool)
            if len(sockets) == 0:
                msg = "Socket: {} is not defined.".format(identifier)
            else:
                msg = "Socket: {} is not defined. Do you mean {}".format(
                    identifier, ", ".join(sockets)
                )
            raise Exception(msg)
        ItemClass = socket_pool[identifier]
        item = ItemClass(name, node=self.parent, type="INPUT", index=len(self._items))
        self._items.append(item)
        return item


class OutputSocketCollection(Collection):
    """Output Socket colleciton"""

    path = "scinode.core.socket"

    def __init__(self, parent) -> None:
        super().__init__(parent)

    @decorator_check_name
    def new(self, identifier, name=None):
        from scinode.sockets import socket_pool
        import difflib

        if identifier not in socket_pool:
            sockets = difflib.get_close_matches(identifier, socket_pool)
            if len(sockets) == 0:
                msg = "Socket: {} is not defined.".format(identifier)
            else:
                msg = "Socket: {} is not defined. Do you mean {}".format(
                    identifier, ", ".join(sockets)
                )
            raise Exception(msg)
        ItemClass = socket_pool[identifier]
        item = ItemClass(name, node=self.parent, type="OUTPUT", index=len(self._items))
        self._items.append(item)
        return item


class LinkCollection(Collection):
    """Link colleciton"""

    def __init__(self, parent) -> None:
        super().__init__(parent)

    def new(self, input, output, type=1):
        from scinode.core.link import NodeLink

        item = NodeLink(input, output)
        self._items.append(item)
        return item

    def __delitem__(self, index):
        self._items[index].unmount()
        del self._items[index]

    def clear(self):
        """Remove all links from this collection.
        And remove the link in the nodes.
        """
        for item in self._items:
            item.unmount()
        self._items = []
