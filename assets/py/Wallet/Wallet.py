import os
import sys

sys.path.append(os.path.join(os.getcwd(), "Db4eRoot"))
from Db4eRoot import Db4eRoot

class Wallet(Db4eRoot):
  """
  Class that represents a crypto currency wallet.
  """

  def __init__(self):
    # Execute parent class's constructor
    #super().__init__()
    pass

  def interactive_menu(self):
    print("")
    print("  5. Exit")
    print("---------- Wallet Menu ------------------")
    print("")
    print("  1. Add New Wallet")
    print("  2. Print All Wallets")
    print("")
    choice = input("Enter your choice: ")

    if choice == "1":
      self.add_new_wallet()

    elif choice == "2":
      # TODO
      pass

    else:
      print("Invalid choice. Please try again.")
      self.interactive_menu()

  def add_new_wallet(self):
    # TODO
    pass