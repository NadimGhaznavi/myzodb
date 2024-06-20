"""
Mining/BlockFoundEvent/BlockFoundEvent.py

A record to store the P2Pool daemon and the date and time that the message appeared in the 
log file.
"""

import persistent

class BlockFoundEvent(persistent.Persistent):

  def __init__(self, pool_name, timestamp):
    self._pool_name = pool_name
    self._timestamp = timestamp
    
  def pool_name(self, new_pool_name=None):
    if new_pool_name:
      self._pool_name = new_pool_name
    return self._pool_name
  
  def timestamp(self, new_timestamp=None):
    if new_timestamp:
      self._timestamp = new_timestamp
    return self._timestamp

  def __lt__(self, other):
    return self.timestamp() < other.timestamp()
  def __le__(self, other):
    return self.timestamp() <= other.timestamp()
  def __eq__(self, other):
    return self.timestamp() == other.timestamp()
  def __ne__(self, other):
    return self.timestamp() != other.timestamp()
  def __hash__(self):
    return hash(self.timestamp())
  def __str__(self):
    return f"Block found in {self.pool_name()} at {self.timestamp()}"
  
