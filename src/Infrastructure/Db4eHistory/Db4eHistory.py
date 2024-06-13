import os
import sys
import persistent

# Append the Infrastructure directory to the Python path
project_dirs = [ 
  "/opt/prod/db4e/assets/py/Infrastructure", 
  "/opt/prod/db4e/assets/py/Mining", 
  "/opt/prod/db4e/assets/py/Reports"
]
for project_dir in project_dirs:
  sys.path.append(project_dir)

from Db4eTree.Db4eTree import Db4eTree

class Db4eHistory(persistent.Persistent):

  def __init__(self, db_root):

    if not hasattr(db_root, 'xmr_transactions'):
      db_root_root.xmr_transactions = Db4eTree('XMR Transactions')
    
    if not hasattr(db_root, 'share_found_events')  
      db_root.share_found_events = Db4eTree('Share found events')

    if not hasattr(db_root, 'block_found_events'
      db_root.block_found_events = Db4eTree('Block found event')
