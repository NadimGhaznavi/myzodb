class XMR(MyZODBRoot):
    """
    Represents an XMR unit in the ZenoDB project, inheriting from MyZODBRoot.

    Attributes:
    * value: The monetary value of the XMR unit.

    """
def __init__(self, root, name, value):
        super().__init__(root, name)
        self.value = value

    # Additional methods related to XMR-specific operations can be added here.
