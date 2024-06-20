"""
Mining/MiningZODB/MiningZODB.py
"""
import sys
import transaction

# Append the projects directories to the module search path
project_dirs = [ 
  "/opt/prod/db4e/src/Infrastructure", 
  "/opt/prod/db4e/src/Mining", 
  "/opt/prod/db4e/src/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

# Import required db4e modules.
from Db4eZODB.Db4eZODB import Db4eZODB

class MiningZODB(Db4eZODB):

  def add_block_found_event(self, event):
    """
    Put new add_found_event instances here:

    root.history.block_found_events
    """
    root = self.root()
    timestamp = event.timestamp()
    print(f"{root}")
    events = root.history['block_found_events']
    events.insert(event)
    transaction.commit()

