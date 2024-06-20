"""
Mining/MiningZEO/MiningZEO.py
"""
import sys
import transaction
from ZODB.PersistentMapping import PersistentMapping

# Append the project's directories to the module search path
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

# Import required db4e modules.
from Db4eZEO.Db4eZEO import Db4eZEO

class MiningZEO():

  def __init__(self):
    self.init_db()

  def init_db(self):
    db = Db4eZEO()
    root = db.root()

    if not hasattr(root.mining, 'workers'):
      root.mining.workers = PersistentMapping()
      transaction.commit()

  def add_block_found_event(self, event):
    """
    Put new Found Block events here

    root.history.block_found_events
    """
    db = Db4eZEO()
    root = db.root()
    timestamp = event.timestamp()
    events = root.history['block_found_events']

    events.insert(event)
    transaction.commit()

  def add_share_found_event(self, event):
    """
    Put new Share Found events here:

    root.history.block_found_events
    """
    db = Db4eZEO()
    root = db.root()
    timestamp = event.timestamp()
    events = root.history['share_found_events']

    events.insert(event)
    transaction.commit()

  def add_xmr_transaction(self, xmr_transaction):
    """
    Put new XMR transactions here:

    root.history.block_found_events
    """
    db = Db4eZEO()
    root = db.root()
    timestamp = xmr_transaction.timestamp()
    xmr_transactions = root.history['xmr_transactions']

    xmr_transactions.insert(xmr_transaction)
    transaction.commit()
0