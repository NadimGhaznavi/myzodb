import os
import sys
import persistent
import persistent.list
sys.path.append(os.path.join(os.getcwd(), "Db4eRoot"))
from Db4eRoot import Db4eRoot


class History(Db4eRoot):
  def __init__(self):
    self.xmr_trans = persistent.list.PersistentList()
    self.share_trans = persistent.list.PersistentList()
    self._p_changed = False