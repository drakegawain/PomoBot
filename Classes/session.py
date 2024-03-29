#-----------------IMPORTs-------------------
import gc
from Classes.classes import class_mute_all
from Classes.when_class import when
from Cli_Commands.Print_Padronization.ppadron import prntpdr
import Configs.configs as cfg
#-------------------------------------------
class Session:
  def __init__(self):
    self.LEADER_ID=None
    self.TIME=None
    self.STATUS=None
    self.STATUS=gc.collect()
    #-----Global-Variables-from-the-session
    self.c=0; 
    self.pomodoro_started=False;
    self.ids_get=[];
    self.joined=0;
    self.ids=set();
    self.study_time_global=0;
    self.rest_time_global=0;
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
        raise Exception('THIS USER ALREADY HAVE A SESSION')
    except:
      print('User already is a leader of another session {}'.format(__name__))
  async def set_time(self, **time_remaining):
    self.TIME=time_remaining
  async def set_status(self, status):
    self.STATUS=status
  async def get(self, var):
    vardict ={
      'STATUS':self.STATUS,
      'c':self.c,
      'pomodoro_started':self.pomodoro_started,
      'ids_get':self.ids_get,
      'joined':self.joined,
      'ids':self.ids,
      'study_time_global':self.study_time_global,
      'rest_time_global':self.rest_time_global,
      'status_class':self.status_class,
      'close':self.close,
      'vc':self.vc,
      'class_e':self.class_e,
      'class_i':self.class_i
    }
    get=vardict.get('{}'.format(var))
    return get
  def restart(self):
    self.LEADER_ID=None
    self.TIME=None
    self.STATUS=None
    self.c=0; 
    self.pomodoro_started=False;
    self.ids_get=[];
    self.joined=0;
    self.ids=set();
    self.study_time_global=0;
    self.rest_time_global=0;
    self.status_class=class_mute_all(None)
    self.close=when() 
    self.vc=None; 
    self.class_e=None 
    self.class_i=None
    self.silent=None
    prntpdr(cfg.black, "restarting...")
    return
  def set_global_var(self, var, value):
    vardict ={
      'c':self.c,
      'pomodoro_started':self.pomodoro_started,
      'ids_get':self.ids_get,
      'joined':self.joined,
      'ids':self.ids,
      'study_time_global':self.study_time_global,
      'rest_time_global':self.rest_time_global,
      'status_class':self.status_class,
      'close':self.close,
      'vc':self.vc,
      'class_e':self.class_e,
      'class_i':self.class_i
    }
    sgv=vardict.get('{}'.format(var))
    sgv=value
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
    prntpdr(cfg.green, "cleanning...")
    return
