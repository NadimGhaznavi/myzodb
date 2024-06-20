from ZEO import ClientStorage
from ZODB import DB
import transaction
from ZODB.PersistentMapping import PersistentMapping
from BTrees.OOBTree import TreeSet

# Database 4 Everything's port number: 51970
ZEO_SERVER = "zeo.osoyalce.com"
ZEO_PORT = 51970

class Db4eZOE():
  def __init__(self):
    self._zeo_port = ZEO_PORT
    self._zeo_server = ZEO_SERVER

    self.init_db()

  def init_db(self):
    root = self.root()
    if not hasattr(root, 'mining'):
      root.mining = PersistentMapping()
      transaction.commit()
    
    if not hasattr(root, 'history'):
      root.history = PersistentMapping()
      root.history['xmr_transactions'] = TreeSet()
      root.history['block_found_events'] = TreeSet()
      root.history['share_found_events'] = TreeSet()
      transaction.commit()
    
  def zeo_port(self):
    return self._zeo_port
  
  def zeo_server(self):
    return self._zeo_server

  def root(self):
    address = self.zeo_server(), self.zeo_port()
    storage = ClientStorage.ClientStorage(address)
    db = DB(storage)
    conn = db.open()
    root = conn.root()
    return root
    
  def print_status(self):
    print("\n---------- Db4eZOE Status -----------------")
    print(f"  ZEO server             : {self.zeo_server()}")
    print(f"  ZOE server port number : {self.zeo_port()}")
    history = self.root().history
    print(f"\n---------- History ------------------------")
    root = self.root()
    num_block_found_events = len(root.history['block_found_events'])
    num_share_found_events = len(root.history['share_found_events'])
    num_xmr_transactions = len(root.history['xmr_transactions'])

    print(f"  XMR Transactions ({num_xmr_transactions})")
    for elem in root.history['xmr_transactions'].keys():
      print(f"  - {elem}")

    print(f"  Block Found Events ({num_block_found_events})")
    for elem in root.history['block_found_events'].keys():
      print(f"  - {elem}")

    print(f"  Share Found Events ({num_share_found_events})")
    for elem in root.history['share_found_events'].keys():
      print(f"  - {elem}")
    