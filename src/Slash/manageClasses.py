#---------------IMPORTS--------------
import logging
import gc
import nextcord
from ..Configs.configs import embed
from .classes import Trigger, Session
from .errorClasses import NoSessionRunning_pomojoin, NoSessionRunning_pomostop
from .manageClasses import exec_mute_all, sstdy
from .manageVars import fetch
from .messages import message_closed_pomodoro
#-----------------------------------------
#---------------BIND----------------------
def bind_status_class_to_mute_all(ctx, ids, session:Session, logger:logging.Logger):
  try:
    trigger=session.trigger
    trigger.add_parameters(ctx)
    trigger.bind(exec_mute_all)
  except:
    logger.warning("Error in {}".format(__name__))
    raise Exception
  return

def bind_status_class_silent(ctx, ids, session:Session, logger:logging.Logger):
  try:
    trigger=session.trigger
    trigger.add_parameters(ctx)
    trigger.bind(sstdy)
  except:
    logger.critical("Error in bind_status_class_silent")
  return
#-------------------------------------------
#---------------THROW-----------------------
def throw_pomodoro_status_close(session:Session, logger:logging.Logger):
  """This method is called when the session needs to be closed. Then, a trigger is started
  and the bot mutes everyone that is inside the session"""
  try:
    trigger=session.trigger
    trigger.add_parameters(session.ids)
    trigger.add_parameters(session)
    trigger.set('close')
  except:
    logger.warning("Error in {}".format(__name__))
    raise Exception
  return 
#-------------------------------------------
#--------------CLOSE-METHODS----------------
def close_pomodoro(ctx:nextcord.Interaction, session:Session):
  try:
    session.close.set('yes')
    session.pomodoro_started = False
    message_closed_pomodoro(ctx, session, embed)
  except:
    raise Exception
  return

async def after_30_seconds_close_pomodoro(ctx:nextcord.Interaction, session:Session, logger:logging.Logger):
  try:
    bind_status_class_to_mute_all(ctx, session.ids, session, logger)
    triggerThrowPomodoroStatusClose=Trigger(30, throw_pomodoro_status_close, session, logger)
    triggerThrowPomodoroStatusClose.exec()
    triggerClosePomodoro=Trigger(30, close_pomodoro, ctx, session)
    triggerClosePomodoro.exec()
  except:
    logger.warning("Error in {}".format(__name__))
  return

async def sec30close(ctx, session, logger):
  try:
    triggerClosePomodoro=Trigger(30, close_pomodoro, ctx, session)
    triggerClosePomodoro.exec()
  except:
    logger.critical("Error in sec30close")
  return
#---------------------------------------------
#---------------------------------------------
#---------------SESSION-METHODS---------------
async def ch_session(dictio:dict, session):
  try:
    if dictio[session] is dictio['Main']:
      return True
    else:
      return False
  except:
    raise Exception 
  return 

async def new_session(dictio:dict):
  dictio['Session_{number}'.format(number=len(dictio))]=Session()
  session=dictio.get('{Session_{number}}'.format(number=len(dictio)))
  return session

async def gather(dictio:dict):
  """Return last session"""
  last_session=len(dictio)
  keys=list(dictio.keys())
  l_session=keys[last_session-1]
  return l_session

async def delete(index, list):
  try:
    garbage=list[index].session["Main"].restart()
    garbage=gc.collect()
  except:
    SM = logging.getLogger("SecurityMessage")
    SM.error("Error in deleting guild {}".format(list[index].guild_name))
  return

async def get_session_pomojoin(ctx, v_channel, dictio:dict):
  """This function get the current running session for command pomojoin"""
  for session in dictio.values():
    if hasattr(session.vc, 'channel'):
      if session.vc.channel is v_channel:
        return session
  raise NoSessionRunning_pomojoin(ctx)

async def get_session(guild, session_list:list):
  """This function finds the index from the list
    that handles the sessions"""
  guild_name=guild.name
  for index in range(len(session_list)):
    guild_name_session_list=session_list[index].get_guild_name()
    if guild_name_session_list is guild_name:
      return session_list[index].get_index()
  for index in range(len(session_list)+1):
    guild_name_session_list=session_list[index].get_guild_name()
    if guild_name_session_list is guild_name:
      return session_list[index].get_index()

async def get_session_ps(ctx, v_channel, dictio:dict):
  """This function get the current running session for command pomostop"""
  for session in dictio.values():
    if hasattr(session.vc, 'channel'):
      if session.vc.channel is v_channel:
          return session
  raise NoSessionRunning_pomostop(ctx)

async def session_handler(dictio:dict, session):
  try:
    for key, value in dictio.items():
      if session == value:
          found_key = key
          break
  except:
    SM = logging.getLogger("SecurityMessage")
    SM.error("Error in session_handler")
    raise Exception
  return found_key

async def search(guild, session_list):
  for session in session_list:
    if session.get_guild_name() == guild.name:
      return session.get_index()

async def searchId(dictio:dict, ID:int):
    HANDLER=None
    for value in dictio.values():
        for i_d in list(value.ids):
            print(i_d)
            if i_d is ID:
                HANDLER=True
    return HANDLER

async def leader(session, ctx):
  """Sets session leader
  Leader joins the session automatically 
  Leader dont need to call pomojoin"""
  response=fetch(ctx)
  author=response[1]
  session.LEADER_ID=author.id
  session.pushleader()
  return
#-----------------------------------------