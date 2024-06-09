"""
Infrastructure/Db4eTree/DB4eTree.py
"""
import persistent
from BTrees.OOBTree import TreeSet

class Db4eTree(Db4eRoot, persistent.Persistent):
  """
  Db4eTree is a generic container class. It uses BTrees.LOBTree (64-bit integer
  keys and Objects as values) to store data. This is a persistent class.
  """
  def __init__(self, name):
    self._name = name
    self._items = TreeSet()

  def add_item(self, key, item):
    self._items.insert(key, item)

  def items(self):
    return self._items

