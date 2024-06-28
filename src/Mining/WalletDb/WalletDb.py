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

  def num_transactions(self):
    mining_db = MiningDb()
    events = mining_db.get_events('xmr_transaction')
    count = 0
    for event in events:
      count = count + 1
    return count