from scinode.core.property import NodeProperty


class GeneralProperty(NodeProperty):
    """A new class for General type."""

    identifier: str = "General"
    data_type = "General"

    def __init__(self, name, description="", default=0, update=None) -> None:
        super().__init__(name, description, default, update)


class IntProperty(NodeProperty):
    """A new class for integer type."""

    identifier: str = "Int"
    data_type = "Int"

    def __init__(self, name, description="", default=0, update=None) -> None:
        super().__init__(name, description, default, update)

    def set_value(self, value):
        # run the callback function
        if isinstance(value, int):
            self._value = value
            if self.update is not None:
                self.update()
        else:
            raise Exception("{} is not a integer.".format(value))


class FloatProperty(NodeProperty):
    """A new class for float type."""

    identifier: str = "Float"
    data_type = "Float"

    def __init__(self, name, description="", default=0.0, update=None) -> None:
        super().__init__(name, description, default, update)

    def set_value(self, value):
        # run the callback function
        if isinstance(value, (int, float)):
            self._value = value
            if self.update is not None:
                self.update()
        else:
            raise Exception("{} is not a float.".format(value))


class BoolProperty(NodeProperty):
    """A new class for bool type."""

    identifier: str = "Bool"
    data_type = "Bool"

    def __init__(self, name, description="", default=True, update=None) -> None:
        super().__init__(name, description, default, update)

    def set_value(self, value):
        # run the callback function
        if isinstance(value, (bool, int)):
            self._value = bool(value)
            if self.update is not None:
                self.update()
        else:
            raise Exception("{} is not a bool.".format(value))


class StringProperty(NodeProperty):
    """A new class for string type."""

    identifier: str = "String"
    data_type = "String"

    def __init__(self, name, description="", default=None, update=None) -> None:
        super().__init__(name, description, default, update)

    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
            # run the callback function
            if self.update is not None:
                self.update()
        else:
            raise Exception("{} is not a string.".format(value))


class EnumProperty(NodeProperty):
    """A new class for enumeration type."""

    identifier: str = "Enum"
    data_type = "Enum"

    def __init__(
        self, name, options=[], description="", default=None, update=None
    ) -> None:
        super().__init__(name, description, default, update)
        self._options = options

    def set_value(self, value):
        if value in self._options:
            self._value = value
            # run the callback function
            if self.update is not None:
                self.update()
        else:
            raise Exception("{} is not in the option list.".format(value))


# ====================================
# Vector
class VectorProperty(NodeProperty):
    """Scinode Vector property"""

    identifier: str = "Vector"
    data_type = "Vector"

    def __init__(self, name, description="", size=3, default=[], update=None) -> None:
        super().__init__(name, description, default, update)
        self.size = size


class IntVectorProperty(VectorProperty):
    """A new class for integer vector type."""

    identifier: str = "IntVector"
    data_type = "IntVector"

    def __init__(
        self, name, description="", size=3, default=[0, 0, 0], update=None
    ) -> None:
        super().__init__(name, description, size, default, update)

    def set_value(self, value):
        # run the callback function
        if len(value) == self.size:
            for i in range(self.size):
                if isinstance(value[i], int):
                    self._value[i] = value[i]
                    if self.update is not None:
                        self.update()
                else:
                    raise Exception("{} is not a integer.".format(value[i]))
        else:
            raise Exception(
                "Length {} is not equal to the size {}.".format(len(value), self.size)
            )


class FloatVectorProperty(VectorProperty):
    """A new class for float vector type."""

    identifier: str = "FloatVector"
    data_type = "FloatVector"

    def __init__(
        self, name, description="", size=3, default=[0, 0, 0], update=None
    ) -> None:
        super().__init__(name, description, size, default, update)

    def set_value(self, value):
        # run the callback function
        if len(value) == self.size:
            for i in range(self.size):
                if isinstance(value[i], (int, float)):
                    self._value[i] = value[i]
                    if self.update is not None:
                        self.update()
                else:
                    raise Exception("{} is not a float.".format(value[i]))
        else:
            raise Exception(
                "Length {} is not equal to the size {}.".format(len(value), self.size)
            )


class BoolVectorProperty(VectorProperty):
    """A new class for bool vector type."""

    identifier: str = "BoolVector"
    data_type = "BoolVector"

    def __init__(
        self, name, description="", size=3, default=[0, 0, 0], update=None
    ) -> None:
        super().__init__(name, description, size, default, update)

    def set_value(self, value):
        # run the callback function
        if len(value) == self.size:
            for i in range(self.size):
                if isinstance(value[i], (bool, int)):
                    self._value[i] = value[i]
                    if self.update is not None:
                        self.update()
                else:
                    raise Exception("{} is not a bool.".format(value[i]))
        else:
            raise Exception(
                "Length {} is not equal to the size {}.".format(len(value), self.size)
            )


# =======================================
# matrix
class MatrixProperty(NodeProperty):
    """Scinode Matrix property"""

    identifier: str = "Matrix"
    data_type = "Matrix"

    def __init__(
        self, name, description="", size=[3, 3], default=[], update=None
    ) -> None:
        super().__init__(name, description, default, update)
        self.size = size


class FloatMatrixProperty(MatrixProperty):
    """A new class for float matrix type."""

    identifier: str = "FloatMatrix"
    data_type = "FloatMatrix"

    def __init__(
        self,
        name,
        description="",
        size=[3, 3],
        default=[0, 0, 0, 0, 0, 0, 0, 0, 0],
        update=None,
    ) -> None:
        super().__init__(name, description, size, default, update)

    def set_value(self, value):
        import numpy as np

        # run the callback function
        self._value = np.zeros(self.size)
        if len(value) == self.size[0] and len(value[0]) == self.size[1]:
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    self._value[i][j] = value[i][j]
                    if self.update is not None:
                        self.update()
        else:
            raise Exception(
                "Length {} is not equal to the size {}.".format(len(value), self.size)
            )


property_list = [
    IntProperty,
    FloatProperty,
    StringProperty,
    BoolProperty,
    EnumProperty,
    IntVectorProperty,
    FloatVectorProperty,
    BoolVectorProperty,
    FloatMatrixProperty,
]
