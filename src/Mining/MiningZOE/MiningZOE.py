"""
Mining/MiningZODB/MiningZODB.py
"""
import sys
import transaction

# Append the project's directories to the module search path
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

# Import required db4e modules.
from Db4eZOE.Db4eZOE import Db4eZOE

class MiningZOE(Db4eZOE):

  def add_block_found_event(self, event):
    """
    Put new add_found_event instances here:

    root.history.block_found_events
    """
    db = Db4eZOE()
    root = db.root()
    timestamp = event.timestamp()
    events = root.history['block_found_events']

    events.insert(event)

    transaction.commit()

