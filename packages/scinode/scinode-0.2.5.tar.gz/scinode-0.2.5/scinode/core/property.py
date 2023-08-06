class NodeProperty:
    """Scinode property.

    When variable is saved to a database, the type of the variable will
    be lost. We use this Property Class to label the type of the data,
    thus we can restore the data from database.

    The data_type is also helpful for the Editor to show the data in the
    GUI.
    """

    data_type = "Node"

    def __init__(self, name, description="", default=None, update=None) -> None:
        """_summary_

        Args:
            name (str): name of the varible
            options (list, optional): options of the varible. Defaults to [].
            description (str, optional): _description_. Defaults to "".
            default (_type_, optional): _description_. Defaults to None.
            update (function, optional): The callback function when
                udpate the item. Defaults to None.
        """
        self.name = name
        self.description = description
        self.default = default
        self.update = update
        self._value = self.default

    def to_dict(self):
        """Data to be saved to database."""
        data = {
            "value": self.value,
            "name": self.name,
            "type": self.data_type,
        }
        return data

    @classmethod
    def from_dict(cls, data):
        p = cls(data["name"])
        p.data_type = data["type"]
        p.value = data["value"]
        return p

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.set_value(value)

    def set_value(self, value):
        # run the callback function
        self._value = value
        if self.update is not None:
            self.update()

    def __str__(self):
        return '{}(name="{}", value={})'.format(self.data_type, self.name, self._value)

    def __repr__(self):
        return '{}(name="{}", value={})'.format(self.data_type, self.name, self._value)
