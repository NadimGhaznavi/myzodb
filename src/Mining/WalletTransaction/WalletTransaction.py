"""
Mining/WalletTransaction/WalletTransaction.py

A record to store transaction information exported from the Monero GUI Wallet
"""

class WalletTransaction():

  def __init__(self, block_num, timestamp, amount, fee, txid, sender, memo=None):
    # blockHeight,epoch,date,direction,amount,atomicAmount,fee,txid,label,subaddrAccount,paymentId,description
    self._block_num = block_num
    self._timestamp = timestamp
    self._amount = amount
    self._fee = fee
    self._txid = txid
    self._sender = sender
    self._memo = memo

  def __str__(self):
    return f"Wallet Transaction for {self._amount} XMR at {self._timestamp}"
  
  def amount(self, new_amount=None):
    if new_amount:
      self._amount = new_amount
    return self._amount

  def block_num(self, new_block_num=None):
    if new_block_num:
      self._block_num = new_block_num
    return self._block_num
  
  def fee(self, new_fee=None):
    if new_fee:
      self._fee = new_fee
    return self._fee

  def memo(self, new_memo=None):
    if new_memo:
      self._memo = new_memo
    return self._memo

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

  