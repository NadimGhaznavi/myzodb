"""
Infrastructure/Db4eTree/DB4eTree.py
"""
import persistent
from BTrees.OOBTree import TreeSet

class Db4eTree(persistent.Persistent):
  """
  Db4eTree is a generic container class. It uses BTrees.LOBTree (64-bit integer
  keys and Objects as values) to store data. This is a persistent class.
  """
  def __init__(self, name):
    """
    __init(name)__
    Constructor. It initializes its addtibutes:
    * _name = name
    * _items = Treeset()
    """
    self._name = name
    self._items = TreeSet()

  def add_item(self, key, item):
    """
    add_item(key, item)

    Add a new object into the TreeSet.

    Accepts:
    * key
    * item
    """
    self._items.insert(key, item)

  def del_item(self, key):
    """
    del_item(key)
    
    If it exists, remove an item from the Treeset.

    Accepts:
    * key
    """
    # Make sure the key is in the items.
    assert key in self._items, f"FATAL ERROR: key ({key}) is not in TreeSet"
    
    self._items.discard(key)
    
  def get_item(self, key):
    """ 
    get_item(key)

    If it exists, rturn the object in the Treeset stored at key.

    Accepts:
    * key
    Returns:
    * Object stored with that key or None
    """
    if key in self._items:
      return self._items[key]
    else
      print(f"FATAL ERROR: key ({key}) is not in TreeSet)")
      sys.exit(1)

  def items(self):
    """
    items()

    Returns the entire TreeSet instance

    Returns:
    * Number of items
    """
    return self._items
  
  def print_status(self):
    print(f"---------- {self._name}")
    print(f" Number of items({len(self._items)})")
    for item in self._items:
      # Call print_status() on contained objects
      item.print_status()
    