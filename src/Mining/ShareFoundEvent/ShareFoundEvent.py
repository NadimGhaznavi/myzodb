"""
Mining/ShareFoundEvent/ShareFoundEvent.py

A record to store the Miner and the timestamp when the message appeared in the P2Pool log.
"""

import persistent

class ShareFoundEvent(persistent.Persistent):

  def __init__(self, miner, effort, difficulty, timestamp):
    self._miner = miner
    self._effort = effort
    self._difficulty = difficulty
    self._timestamp = timestamp
    self._ip = None
    
  def __lt__(self, other):
    if self._timestamp < other._timestamp:
      return True
    else:
      return False
  
  def __le__(self, other):
    if (self < other):
      return True
    return(self == other)

  def __eq__(self, other):
    if self._timestamp == other._timestamp:
      return True
    else:
      return False
    
  def __ne__(self, other):
    return not (self == other)
  
  def __hash__(self):
    return hash(self._timestamp)

  def miner(self, new_miner=None):
    if new_miner:
      self._miner = new_miner
    return self._miner
  
  def effort(self, new_effort=None):
    if new_effort:
      self._effort = new_effort
    return self._effort

  def difficulty(self, new_difficulty=None):
    if new_difficulty:
      self._difficulty = new_difficulty
    return self._difficulty

  def timestamp(self, new_timestamp=None):
    if new_timestamp:
      self._timestamp = new_timestamp
    return self._timestamp

  def ip(self, new_ip=None):
    if new_ip:
      self._ip = new_ip
    return self._ip
