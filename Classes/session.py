#--This-file-handles-the-current-session-
#--and-its-status:Time-Remaining,-leader,  
#--Status:Open,-Close,-Null
from Classes.classes import class_mute_all
from Classes.when_class import when

class Session:
  def __init__(self):
    self.LEADER_ID=None
    self.TIME=None
    self.STATUS=None
    #-----Global-Variables-from-the-session
    self.c=0; #counter
    self.pomodoro_started=False;
    self.ids_get=[];
    self.joined=0;
    self.ids=set();
    self.study_time_global=0;
    self.rest_time_global=0;
    self.status_class=class_mute_all(None) #This class mute's all
    self.close=when() #Starts a when class, see in when_class
    self.vc=None; #This is a voice variable, its used in play_audio
    self.class_e=None #This variables are classes
    self.class_i=None
  async def set_leader_id(self, id):
    try:
      if self.LEADER_ID is not None:
        self.LEADER_ID=id
      else:
        raise Exception('THIS USER ALREADY HAVE A SESSION')
    except:
      print('User already is a leader of other session {}'.format(__name__))
  async def set_time(self, **time_remaining):
    self.TIME=time_remaining
  async def set_status(self, status):
    self.STATUS=status
  async def get(self, var):
    return self.var
  def restart(self):
    self.LEADER_ID=None
    self.TIME=None
    self.STATUS=None
  def set_global_var(self, var, value):
    self.var=value
