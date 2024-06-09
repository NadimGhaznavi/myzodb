import persistent
from BTrees.OOBTree import TreeSet

class Wallets(Db4eRoot, persistent.Persistent):

  def __init__(self, name):
    self._name = name
    self._wallets = TreeSet()

  def print_status(self):
    """
    Print a status message.
    """
    print(f"---------- Wallets -----------------------")

  def interactive_menu(self):
    print("")
    print("========== Wallet Operations ============")
    print("")
    print("  1. List Wallets")
    print("  2. Add Wallet")
    print("  3. Remove Wallet")
    print("  4. Query Wallet")      
    print("  5. Exit")
    print("")
    choice = input("Enter your choice: ")
    print("")

    if choice == "1":
      self.print_wallets()

    elif choice == "2":
      self.interactive_add_wallet()

    elif choice == "3":
      self.interactive_del_wallet()

    elif choice == "4":
      self.interactive_query_wallet()
    
    elif choice == "5":
      return

    else:
      print("Invalid choice. Please try again.")
      self.interactive_menu()

  def interactive_add_wallet(self):
    print(f"---------- Add New Wallet ---------------------")
    
    wallet_addr = (input("Enter the wallet address below:\n"))
    wallet_name = (wallet_addr[0:6])
    wallet_name_userinput = input("Enter a name for this wallet [{wallet.name()}]: ")
    if wallet_name_userinput:
      wallet_name = wallet_name_userinput
    
    # Create a new wallet, set it's address and add it to our wallets
    # collection with the wallet name as the key.
    wallet = Wallet(wallet_name)
    wallet.addr(wallet_addr)
    self.add_item(wallet_name, wallet)


    def add_item(self, wallet_name, wallet):
      """
      Add an item to our _wallets B-Tree structure.
      """
      self._wallets.insert(wallet_name, wallet)