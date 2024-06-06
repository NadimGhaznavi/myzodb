import sys
import ZODB, ZODB.FileStorage


class Db4eRoot:
  """
  Abstract root class for the ZenoDB project, inheriting from ZODB.

  Attributes:
  * _root: The root object of the ZODB database.
  * _name: The name of the object.
  """

  def __init__(self, zodb_file):
    """
    Constructor.
    """  
    storage = ZODB .FileStorage.FileStorage(zodb_file)
    self.db = ZODB.DB(storage)
    self.db.open()
    self.zodb_file = zodb_file

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
        wallet.add_wallet_menu()

      elif choice == "3":
        self.db.print_wallets()

      elif choice == "3":
        chart = EarningsChart()
        chart.updateCsv()

      elif choice == "4":
        sys.exit(0)

      else:
        print("Invalid choice. Please try again.")
        self.print_menu()

    
  def print_status(self):
    print("\n========== Status =====")
    print("Environment: TBD") # Should be PROD, DEV or QA
    print("ZODB file location: ", self.zodb_file)
  
  def __str__(self):
    """
    Returns:
    * A string containing the object's class and name.
    """
    return f"{self.__class__.__name__}(name={self._name})"
