#-----------------IMPORTs-------------------
import gc
import logging
from ..Classes.classes import class_mute_all
from ..Classes.when_class import when

#-------------------------------------------
class Session:
  def __init__(self):
    self.LEADER_ID=None
    self.TIME=None
    self.STATUS=None
    self.STATUS=gc.collect()
    self.c=0; 
    self.pomodoro_started=False
    self.ids_get=[]
    self.joined=0
    self.ids=set()
    self.study_time_global=0
    self.rest_time_global=0
    self.status_class=class_mute_all(None) 
    self.close=when() 
    self.vc=None; 
    self.class_e=None 
    self.class_i=None
    self.silent=None
    self.restart()
  async def set_leader_id(self, id):
    try:
      if self.LEADER_ID is not None:
        self.LEADER_ID=id
      else:
        SM = logging.getLogger("SecurityMessage")
        SM.error("User already have a session")
        
        raise Exception("User already have a session")
    except:
        SM = logging.getLogger("SecurityMessage")
        SM.error("User already have a session")
        
  async def set_time(self, **time_remaining):
    self.TIME=time_remaining
  async def set_status(self, status):
    self.STATUS=status
  async def get(self, var:str):
    return self.__getattribute__(var)
  def restart(self):
    self.LEADER_ID=None
    self.TIME=None
    self.STATUS=None
    self.c=0; 
    self.pomodoro_started=False
    self.ids_get=[]
    self.joined=0
    self.ids=set()
    self.study_time_global=0
    self.rest_time_global=0
    self.status_class=class_mute_all(None)
    self.close=when() 
    self.vc=None; 
    self.class_e=None 
    self.class_i=None
    self.silent=None
    SM = logging.getLogger("Event")
    SM.error("restarting...")
    
    return
  def pushleader(self):
    self.ids.add(self.LEADER_ID)
    return
  def clear(self):
    self.LEADER_ID=gc.collect()
    self.TIME=gc.collect()
    self.STATUS=gc.collect()
    self.c=gc.collect()
    self.pomodoro_started=gc.collect()
    self.ids_get=gc.collect()
    self.joined=gc.collect()
    self.ids=gc.collect()
    self.study_time_global=gc.collect()
    self.rest_time_global=gc.collect()
    self.status_class=gc.collect()
    self.close=gc.collect()
    self.vc=gc.collect()
    self.class_e=gc.collect()
    self.class_e=gc.collect()
    SM = logging.getLogger("Event")
    SM.error("cleaning...")
    
    return
