#!/usr/bin/python3
"""
Infrastructure/Db4eZEO/Db4eZEO.py
"""

import sys
from ZEO import ClientStorage
from ZODB import DB
from ZODB.PersistentMapping import PersistentMapping
import transaction
from BTrees.OOBTree import TreeSet

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


class Db4eZEO():
  def __init__(self):
    startup = Db4eStartup()
    self._zeo_server = startup.zeo_server()
    self._zeo_port = startup.zeo_port()
    zeo_address = self.zeo_server(), self.zeo_port()
    storage = ClientStorage.ClientStorage(zeo_address)
    db = DB(storage)
    conn = db.open()
    self._root = conn.root()
    self.init_db()

  def init_db(self):
    root = self.root()
    if not hasattr(root, 'mining'):
      root.mining = PersistentMapping()
      transaction.commit()
    
    if not hasattr(root, 'history'):
      root.history = PersistentMapping()
      root.history['xmr_transactions'] = TreeSet()
      root.history['block_found_events'] = TreeSet()
      root.history['share_found_events'] = TreeSet()
      transaction.commit()

  def menu(self):
    print("\n---------- Db4eZOE Menu -------------------")

  def print_status(self):
    print("\n---------- Db4eZOE Status -----------------")
    print(f"  ZEO server             : {self.zeo_server()}")
    print(f"  ZEO server port number : {self.zeo_port()}")

    history = self.root().history
    print(f"\n---------- History ------------------------")
    root = self.root()

    num_xmr_transactions = len(root.history['xmr_transactions'])
    print(f"  XMR Transactions ({num_xmr_transactions})")
    for elem in root.history['xmr_transactions'].keys():
      print(f"  - {elem}")

    num_block_found_events = len(root.history['block_found_events'])
    print(f"  Block Found Events ({num_block_found_events})")
    for elem in root.history['block_found_events'].keys():
      print(f"  - {elem}")

    num_share_found_events = len(root.history['share_found_events'])
    print(f"  Share Found Events ({num_share_found_events})")
    for elem in root.history['share_found_events'].keys():
      print(f"  - {elem}")

  def root(self):
    return self._root
    
  def zeo_port(self):
    return self._zeo_port
  
  def zeo_server(self):
    return self._zeo_server

def main():
  db = Db4eZEO()
  db.print_status()

if __name__ == '__main__':
  main()