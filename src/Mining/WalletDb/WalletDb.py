#!/usr/bin/python3

"""
Mining/WalletDb/WalletDb.py
"""

import sys

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

# Import required db4e modules.
from Db4eStartup.Db4eStartup import Db4eStartup
from MiningDb.MiningDb import MiningDb

class WalletDb():

  def add_transaction(self, wallet_transaction):
    block_num = wallet_transaction.block_num()
    timestamp = wallet_transaction.timestamp()
    amount = wallet_transaction.amount()
    fee = wallet_transaction.fee()
    txid = wallet_transaction.txid()
    sender = wallet_transaction.sender()
    memo = wallet_transaction.memo()
    new_event = {
      'doc_type' : 'wallet_transaction',
      'sender' : sender,
      'block_num' : block_num,
      'amount' : amount,
      'fee' : fee,
      'txid' : txid,
      'memo' : memo
    }
    miningDb = MiningDb()
    miningDb.insert_uniq_one(new_event)

  def num_transactions(self):
    mining_db = MiningDb()
    events = mining_db.get_events('wallet_transaction')
    count = 0
    for event in events:
      count = count + 1
    return count