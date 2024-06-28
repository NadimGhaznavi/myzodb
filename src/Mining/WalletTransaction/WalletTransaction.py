"""
Mining/WalletTransaction/WalletTransaction.py

A record to store transaction information exported from the Monero GUI Wallet
"""

class WalletTransaction():

  def __init__(self, block_num, timestamp, amount, fee, txid):
    # blockHeight,epoch,date,direction,amount,atomicAmount,fee,txid,label,subaddrAccount,paymentId,description
    self._block_num = block_num
    self._timestamp = timestamp
    self._amount = amount
    self._fee = fee
    self._txid = txid

  def __str__(self):
    return f"Wallet Transaction for {self._amount} XMR at {self._timestamp}"
  
  def amount(self, new_amount=None):
    if new_amount:
      self._amount = new_amount
    return self._amount

  def block_height(self, new_block_height=None):
    if new_block_height:
      self._block_height = new_block_height
    return self._block_height

  def memo(self, new_memo=None):
    if new_memo:
      self._memo = new_memo
    return self._memo

  def receiver(self, new_receiver=None):
    if new_receiver:
      self._receiver = new_receiver
    return self._receiver

  def sender(self, new_sender=None):
    if new_sender:
      self._sender = new_sender
    return self._sender
  
  def timestamp(self, new_timestamp=None):
    if new_timestamp:
      self._timestamp = new_timestamp
    return self._timestamp

  def txid(self, new_txid=None):
    if new_txid:
      self._txid = new_txid
    return self._txid

  