"""
Mining/XMRTransaction/XMRTransaction.py

A record to store the details of an XMR Transaction, specifically the sender, recipient,
amount, a timestamp and an optional memo field.
"""

import persistent

class XMRTransaction(persistent.Persistent):

  def __init__(self, sender, recipient, amount, timestamp, memo=None):
    self._sender = sender
    self._recipient = recipient
    self._amount = amount
    self._timestamp = timestamp
    self._memo = memo

  def sender(self, new_sender=None):
    if new_sender:
      self._sender = new_sender
    return self._sender
  
  def recipient(self, new_recipient=None):
    if new_recipient:
      self._recipient = new_recipient
    return self._recipient
  
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
  
