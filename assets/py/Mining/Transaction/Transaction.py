class db4eTransaction():
  def __init__(self):
    """
    Constructor
    """
    self._sender = None
    self._recipient = None
    self._timestamp = None
    self._memo = None

  @property
  def sender(self):
    return self._sender
  
  @sender.setter
  def sender(self, sender: str):
     self._sender = sender
    
  @property
  def recipient(self):
    return self._recipient

  @recipient.setter
  def recipient(self, recipient: str):
    self._recipient = recipient
    
  @property
  def timestamp(self):
    return self._timestamp
  
  @timestamp.setter
  def timestamp(self, timestamp: datetime):
    self._timestamp = timestamp
  
  @property
  def memo(self):
    return self._memo
  
  @memo.setter
  def memo(self, memo: str):
    self._memo = memo
  