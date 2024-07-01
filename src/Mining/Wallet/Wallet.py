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

from WalletDb.WalletDb import WalletDb
from Db4eStartup.Db4eStartup import Db4eStartup
from WalletTransaction.WalletTransaction import WalletTransaction

class Wallet():

  def __init__(self):
    startup = Db4eStartup()
    self._wallet_csv = startup.wallet_csv()

  def load_wallet_csv(self):
    wallet_file = self.wallet_csv()
    print(f"\nLoading wallet csv data ({wallet_file})")
    csv_handle = csv.reader(open(wallet_file))

    first_row = True
    for aRow in csv_handle:
      ### CSV File format
      # blockHeight,epoch,date,direction,amount,atomicAmount,fee,txid,label,subaddrAccount,paymentId,description
      # 3177687,1719152144,2024-06-23 10:15:44,in,0.000281461344,281461344,,9ac844bfe5c7b6a2f77130a8da2a4a30d0ab65f163f472863d3fe26910559e02,"Primary account",0,,""
      if first_row == True:
        first_row = False
      else:
        block_num = aRow[0]
        timestamp = aRow[2]
        amount = aRow[4]
        fee = aRow[6]
        txid = aRow[7]
        transaction = WalletTransaction(block_num, timestamp, amount, fee, txid, 'P2Pool')
        db = WalletDb()
        db.add_transaction(transaction)

  def print_status(self):
    db = WalletDb()
    num_transactions = db.num_transactions()
    print("\n---------- Wallet Status ------------------")
    print(f"  Wallet CSV File: {self._wallet_csv}")
    print(f"  Number of XMR Transactions: {num_transactions}")
  memo
memo
memo
memo
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