import os
import sys

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "/opt/prod/db4e/assets/py/Infrastructure", 
  "/opt/prod/db4e/assets/py/Mining", 
  "/opt/prod/db4e/assets/py/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

from Wallets.Wallets import Wallets
from P2Pools.P2Pools import P2Pools
from Reports.Reports import Reports
import persistent

class Db4eRoot():
  """
  Abstract root class for the ZenoDB project, inheriting from ZODB. This class serves as a foundation
  for managing the ZODB database, providing methods for connecting to the database, creating the
  basic data structure for storing and accessing data, and interacting with the user through an
  interactive menu.

  Attributes:
  * _root: The root object of the ZODB database.
  * _name: The name of the object.

  Usage:
  Initialize an instance of the Db4eRoot class with the ZODB file path and environment:
  
  db_root = Db4eRoot('/path/to/zodb_file', 'production')

  To interact with the database, access methods such as `interactive_menu`, `print_status`, and
  others, as needed:
  
  db_root.interactive_menu()
  """

  def __init__(self):
    """
    Constructor.

    1. Calls init_schema() to initialize the architecture
    2. Sets a name for itself
    3. Initializes the db attribute to None
    """  

    self.load_schema()
    self._name = f"{self.__class__.__name__}"
    self._db = None
  
  def db(self, newDb):
    """
    Get/Set method.
    """
    if newDb:
      self._db = newDb
    return self._db

  def print_status(self):
    """
    Print status info.
    """
    print(f"---------- Root --------------------------")
    self.root['wallets'].print_status()
    self.root['p2pools'].print_status()
    self.root['reports'].print_status()

  def load_schema(self):
    """
    Create the basic data structure to access data in the ZODB.
    """
    self.root = persistent.mapping.PersistentMapping()
    self.root['wallets'] = Wallets()
    self.root['p2pools'] = P2Pools()
    self.root['reports'] = Reports()

  def __str__(self):
    """
    Returns:
    * A string containing the object's class and name.
    """
    return f"{self.__class__.__name__}(name={self._name})"
