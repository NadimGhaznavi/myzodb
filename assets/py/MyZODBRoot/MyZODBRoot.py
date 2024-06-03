class MyZODBRoot:
    """
    Abstract root class for the ZenoDB project, inheriting from ZODB.

    Attributes:
    * _root: The root object of the ZODB database.
    * _name: The name of the object.

    """
def __init__(self, root, name):
        self._root = root

    def get_root(self):
      """
      Returns the root object of the ZODB database.

      Returns:
      * The root object of the ZODB database.

      """
      return self._root

    def set_root(self, root):
      """
      Sets the root object of the ZODB database.

      Args:
      * root: The new root object for the ZODB database.

      """
      self._root = root

    def __str__(self):
      """
      Returns a string representation of the object.

      Returns:
      * A string containing the object's class and name.

      """
      return f"{self.__class__.__name__}(name={self._name})"
