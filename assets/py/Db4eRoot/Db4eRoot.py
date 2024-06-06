import os
import sys
import ZODB, ZODB.FileStorage
import persistent
import persistent.list
import persistent.mapping

class Db4eRoot:
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

  def __init__(self, zodb_file, environ):
    """
    Constructor.

    1. Creates a storage object pointing at the zodb_file, where the backend files live.
    2. Creates a ZODB.DB(storage) object with that storage specified and stores it in self.db.
    3. Open's a DB connection and stores it in self.connection
    4. Connects to the root object and stores it in self.root.
    5. Sets self.environ to 
    """  

    storage = ZODB.FileStorage.FileStorage(zodb_file)
    self.db = ZODB.DB(storage)
    self.connection = self.db.open()
    self.environ = environ

    self.load_schema()
    self._name = f"{self.environ} {self.__class__.__name__}"
  

  def load_schema(self):
    """
    Create the basic data structure to access data in the ZODB.
    """
    self.root = persistent.mapping.PersistentMapping()
    self.root['environ'] = self.environ
    self.root['wallets'] = persistent.list.PersistentList()
    self.root['p2pools'] = persistent.list.PersistentList()
    self.root['charts'] = persistent.list.PersistentList()

  def environ(self, new_environ):
    """
    Get/Set method.
    """
    if new_environ:
      self.environ = new_environ
    return self.environ
  
  def __del__(self):
    self.db.close()

  def interactive_menu(self) -> None:
    """
    Print an interactive menu, providing the user with a menu interface for executing
    db4e functions. Also, process the user's choice.
    """
    while True:
      print("========== My ZODB Application ==========")
      print("")
      print("  1. Status")
      print("  2. Create New Wallet")
      print("  3. Print All Wallets")
      print("  4. Load XMR Earnings from CSV File")      
      print("  5. Exit")
      print("")
      choice = input("Enter your choice: ")

      if choice == "1":
        self.print_status()

      elif choice == "2":
        wallet = Wallet()
        wallet.interactive_menu()

      elif choice == "3":
        wallet = Wallet()
        wallet.print_wallets()

      elif choice == "4":
        chart = EarningsChart()
        chart.updateCsv()

      elif choice == "5":
        sys.exit(0)

      else:
        print("Invalid choice. Please try again.")
        self.interactive_menu()

  def print_status(self):
    print("\n========== Status =====")
    print("Environment: TBD") # Should be PROD, DEV or QA
    print("ZODB file location: ", self.environ())
  
  def __str__(self):
    """
    Returns:
    * A string containing the object's class and name.
    """
    return f"{self.__class__.__name__}(name={self._name})"
