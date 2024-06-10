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

# Import required db4e classes
from Transactions.Transactions import Transactions

class Wallet():
  """
  Class that represents a crypto currency wallet.
  """

  def __init__(self, wallet_name):
    self._name = wallet_name
    self._transactions = Transactions()

  def interactive_menu(self):
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