#-------------IMPORTs------------
import os
import asyncio
import gc
import logging
import mysql.connector
#--------------------------------
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
    self.status_class=Trigger(None) 
    self.close=When() 
    self.vc=None; 
    self.class_e=None 
    self.class_i=None
    self.silent=None
    self.clear()
    self.__restart()
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
  def __restart(self):
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
    self.status_class=Trigger(None)
    self.close=When() 
    self.vc=None; 
    self.class_e=None 
    self.class_i=None
    self.silent=None
    logger = logging.getLogger("Event")
    logger.error("restarting...")
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
    self.trigger=gc.collect()
    self.close=gc.collect()
    self.voiceChannel=gc.collect()
    self.class_e=gc.collect()
    self.class_e=gc.collect()
    logger = logging.getLogger("Event")
    logger.error("cleaning...")
    return

class When:
  """#This file assigns the classes that manipulate variables
  the main class is when, that assigns a variable value to a function
  and sets a variable when_, when the variable value is changed its value to when_, the function is executed."""
  def __init__(self):
    self.value = 0
    self.when_ = 0
    self.functions = None
    self.args = None
    self.task = None
  def set(self, value):
    self.value = value
    if self.value == self.when_:
      self.task = asyncio.create_task(self.functions(*self.args))
  def if_when(self, when_):
    self.when_ = when_
  def set_functions(self, function):
    self.functions = function
  def set_args(self, *args):
    self.args = args
  def cancel(self):
    self.task.cancel()

class execWhen:
  """this class executes a function after a timeout"""
  def __init__(
    self, TIMEOUT, FUNCTION, *ARGS
  ):
    self.TIMEOUT=TIMEOUT
    self.FUNCTION=FUNCTION
    self.ARGS=ARGS
    self.FUTURE=None
  def exec(self):
    loop = asyncio.get_running_loop()
    self.FUTURE=loop.create_future()
    HANDLE=loop.call_later(self.TIMEOUT, self.FUNCTION,  *self.ARGS)
    self.FUTURE.add_done_callback(lambda *args:HANDLE.cancel())
  def release_future(self):
    if not self.FUTURE.done():
      self.FUTURE.set_result(None)
  
class Trigger:
  """This class is used to bind a function to a variable.
  When this variable is changed, the function binded is executed and
  the variable is changed with the method set"""
  def __init__(self, status):
    self.status = status
    self.commands = []
    self.parameters = []
  def add_parameters(self, parameter):
    """this method handles the parameters of the binded function"""
    self.parameters.append(parameter)
    return 
  def set(self, status):
    self.status = status
    for x in self.commands:
      x(self.parameters[0], self.parameters[1], self.parameters[2])
  def bind(self, commands):
    self.commands.append(commands)

class SecurityMessage:
  def __init__(self, command:str, ctx:str, userid:int):
    self.command=command
    self.message=''
    self.ctx=ctx
    self.reason=''
    self.user=userid
    self.logger=logging.getLogger("SecurityMessage")
    self.error=None
    self.table=os.getenv("error_table")
    self.__db=mysql.connector.connect(
    host="localhost",
    user=os.getenv("db_usr"),
    password=os.getenv("db_psswd"),
    database=os.getenv("database")
)
    self.__cursor=self.__db.cursor(buffered=True)
  async def send(self, error:int):
    try:
      self.search_reason(error)
    except TypeError:
      print('error in send search_reason')
    try:
      self.set_message()
    except:
      print('error in send set_message')
    try:
      message=self.ctx
      await message.channel.send(self.message)
      self.logger.error("{}  :  {}".format(self.error, self.command))
    except:
      self.logger.error("Error in third block SecurityMessage_send")
      
  def set_message(self):
    self.message=("\n>>> <@{user}> \nUnfourtunally PomoBot could'nt call ``{command}`` **because**: **{reason}**".format(user=self.user, command=self.command, reason=self.reason))
  def search_reason(self, error:int):
    self.error = error
    #implemented errors
    #pomostop_101 - User outside the session
    #pomostop_121 - No session running
    #pomostop_141 - User outside Voice_Channel
    #pomodoro_201 - User already in another session
    #pomodoro_221 - Inputs must be a integer
    #pomodoro_251 - Must have two inputs
    #pomodoro_271 - Only one session per voice_channel at the same time
    #pomojoin_301 - No session running
    #cursor = cfg.cursor
    self.__cursor.execute("select message from {table} where number = '{number}'".format(table=self.table, number=self.error))
    res = self.__cursor.fetchone()
    self.reason = res[0]
    return

