"""
Mining/XMRTransaction/XMRTransaction.py

A record to store the transaction information for when the P2P deamon detects
a XMR payout for shares found in the PPLNS window.
"""

class XMRTransaction():

  def __init__(self, sender, receiver, amount, timestamp, memo=None):
    self._sender = sender
    self._receiver = receiver
    self._amount = amount
    self._memo = memo
    self._timestamp = timestamp
    
  def __str__(self):
    return f"XMR Transaction for {self._amount} XMR at {self._timestamp}"
  
  def sender(self, new_sender=None):
    if new_sender:
      self._sender = new_sender
    return self._sender
  
  def receiver(self, new_receiver=None):
    if new_receiver:
      self._receiver = new_receiver
    return self._receiver

  def amount(self, new_amount=None):
    if new_amount:
      self._amount = new_amount
    return self._amount

  def timestamp(self, new_timestamp=None):
    if new_timestamp:
      self._timestamp = new_timestamp
    return self._timestamp

  def memo(self, new_memo=None):
    if new_memo:
      self._memo = new_memo
    return self._memo
