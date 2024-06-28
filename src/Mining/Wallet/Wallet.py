#!/usr/bin/python3
"""
Mining/Wallet/Walley.py
"""
# Append the Infrastructure directory to the Python path
import csv
import sys
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

from MiningMongoDb.MiningMongoDb import MiningMongoDb
from Db4eStartup.Db4eStartup import Db4eStartup

class Wallet():

  def __init__(self):
    startup = Db4eStartup()
    self._wallet_csv = startup.wallet_csv()

  def load_wallet_csv(self):
    print(f"\nLoading wallet csv data ({self.wallet_csv()})")
    
  def print_status(self):
    db = MiningMongoDb()
    num_transactions = db.num_wallet_transactions()
    print("\n---------- Wallet Status ------------------")
    print(f"  Number of XMR Transactions: {num_transactions}")
  
  def wallet_csv(self, new_wallet_csv=None):
    if new_wallet_csv:
      self._wallet_csv = new_wallet_csv
    return self._wallet_csv

def main():
  wallet = Wallet()
  startup = Db4eStartup()
  action = startup.action()
  if action == 'load_wallet_csv':
    wallet.load_wallet_csv()
  else:
    wallet.print_status()

if __name__ == '__main__':
  main()