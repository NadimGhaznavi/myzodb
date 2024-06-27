#!/usr/bin/python3
"""
Mining/Wallet/Walley.py
"""
# Append the Infrastructure directory to the Python path
import sys
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

from MiningMongoDb.MiningMongoDb import MiningMongoDb

class Wallet():

  def print_status(self):
    db = MiningMongoDb()
    num_transactions = db.num_wallet_transactions()

    print("\n---------- Wallet Status ------------------")
    print(f"  Number of XMR Transactions: {num_transactions}")
    

def main():
  wallet = Wallet()
  wallet.print_status()

if __name__ == '__main__':
  main()