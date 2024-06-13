"""
Mining/BlockFoundEvent/BlockFoundEvent.py

A record to store the P2Pool daemon and the date and time that the message appeared in the 
log file.
"""

import persistent

class BlockFoundEvent(persistent.Persistent):

  def __init__(self, pool, timestamp):
    self._pool = pool
    self._timestamp = timestamp
    
  def pool(self, new_pool=None):
    if new_pool:
      self._pool = new_pool
    return self._pool
  
  def timestamp(self, new_timestamp=None):
    if new_timestamp:
      self._timestamp = new_timestamp
    return self._timestamp
