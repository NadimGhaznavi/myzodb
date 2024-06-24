#!/usr/bin/python3
"""
Mining/MiningMongoDb/MiningMongoDb.py
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
from Db4eMongoDb.Db4eMongoDb import Db4eMongoDb
from BlockFoundEvent.BlockFoundEvent import BlockFoundEvent
from ShareFoundEvent.ShareFoundEvent import ShareFoundEvent
from XMRTransaction.XMRTransaction import XMRTransaction

class MiningMongoDb():

  def insert_uniq_one(self, new_event):
    db = self.db()
    mining_col = db["mining"]
    timestamp = new_event['timestamp']
    if not mining_col.find_one({'timestamp': timestamp}):
      mining_col.insert_one(new_event)

  def add_block_found_event(self, block_found_event):
    pool_name = block_found_event.pool_name()
    timestamp = block_found_event.timestamp()
    new_event = {
      'doc_type' : 'block_found_event',
      'p2pool' : pool_name,
      'timestamp' : timestamp
    }
    self.insert_uniq_one(new_event)

  def add_share_found_event(self, share_found_event):
    miner = share_found_event.miner()
    effort = share_found_event.effort()
    difficulty = share_found_event.difficulty()
    ip_addr = share_found_event.ip_addr()
    timestamp = share_found_event.timestamp()
    new_event = {
      'doc_type' : 'share_found_event',
      'miner' : miner,
      'effort' : effort,
      'difficulty' : difficulty,
      'ip_addr' : ip_addr,
      'timestamp' : timestamp
    }
    self.insert_uniq_one(new_event)

  def add_xmr_transaction(self, xmr_transaction):
    sender = xmr_transaction.sender()
    receiver = xmr_transaction.receiver()
    amount = xmr_transaction.amount()
    memo = xmr_transaction.memo()
    timestamp = xmr_transaction.timestamp()
    new_transaction = {
      'doc_type' : 'xmr_transaction',
      'sender' : sender,
      'receiver' : receiver,
      'amount' : amount,
      'memo' : memo,
      'timestamp' : timestamp
    }
    self.insert_uniq_one(new_transaction)
  
  def db(self):
    db = Db4eMongoDb()
    return db.db()

  def get_events(self, event_type):
    db = self.db()
    mining_col = db["mining"]
    events = mining_col.find({'doc_type': event_type})
    return events
    
  def print_status(self):
    print("---------- MiningMongoDb Status -----------")

    events = self.get_events('xmr_transaction')
    #print(f"-- XMR Transactions ({len(events)})")
    print(f"-- XMR Transactions -----------------------")
    xmr_count = 0
    for event in events:
      xmr_count = xmr_count + 1
      sender = event['sender']
      receiver = event['receiver'][0:6]
      amount = event['amount']
      memo = event['memo']
      timestamp = event['timestamp']
      print(f"{timestamp} : From ({sender}) To ({receiver}) Amount ({amount}) Memo ({memo})")
    print(f"Total number of records ({xmr_count})")

    events = self.get_events('share_found_event')
    #print(f"-- Share Found Events ({len(events)})")
    print(f"-- Share Found Events ---------------------")
    share_count = 0
    for event in events:
      share_count = share_count + 1
      miner = event['miner']
      effort = event['effort']
      difficulty = event['difficulty']
      ip_addr = event['ip_addr']
      timestamp = event['timestamp']
      print(f"{timestamp} : Miner ({miner}) Effort ({effort}) Difficulty ({difficulty}) IP Address ({ip_addr}))")
    print(f"Total number of records ({share_count})")

    events = self.get_events('block_found_event')
    #print(f"-- Block Found Events ({len(events)})")
    print(f"-- Block Found Events ---------------------")
    block_count = 0
    for event in events:
      block_count = block_count + 1
      p2pool = event['p2pool']
      timestamp = event['timestamp']
      print(f"{timestamp} : P2Pool ({p2pool})")
    print(f"Total number of records ({block_count})")
    
    print("-------------------------------------------")
    print("Total number of records:\n")
    print(f"  XMR Transactions   : {xmr_count}")
    print(f"  Block Found Events : {block_count}")
    print(f"  Share Found Events : {share_count}")
    print(f"\n               Total : {xmr_count + block_count + share_count}")

def main():
  db4e = Db4eRoot()
  db = db4e.db()
  mining = Db4eMining(db)
  mining.print_status()

if __name__ == '__main__':
    main()