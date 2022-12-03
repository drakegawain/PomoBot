#---------------IMPORTS--------------
import logging
import gc
import nextcord
from ..Configs.configs import embed
from ..Configs.configs import session_guilds as guildList
from .classes import Trigger, Session, execWhen
from .manageVars import fetch
from .messages import message_closed_pomodoro
#-----------------------------------------
#---------------BIND----------------------
#-----------------------------------------
def bind(bindFunc, triggerName:str, ctx, ids, session:Session, logger:logging.Logger) -> None:
  try:
    trigger=session.trigger.get(triggerName)
    trigger.add_parameters(ctx)
    trigger.bind(bindFunc)
  except:
    logger.warning("Error in {}".format(__name__))
    raise Exception
  return

def bindSilent(bindFunc, triggerName:str, ctx, ids, session:Session, logger:logging.Logger) -> None:
  try:
    trigger=session.trigger.get(triggerName)
    trigger.add_parameters(ctx)
    trigger.bind(bindFunc)
  except:
    logger.critical("Error in bind_status_class_silent")
  return
#-------------------------------------------
#---------------THROW-----------------------
def throw_pomodoro_status_close(session:Session, logger:logging.Logger) -> None:
  """This method is called when the session needs to be closed. Then, a trigger is started
  and the bot mutes everyone that is inside the session"""
  try:
    trigger=session.trigger.get("throwClose")
    trigger.add_parameters(session.ids)
    trigger.add_parameters(session)
    trigger.set('close')
  except:
    logger.warning("Error in {}".format(__name__))
    raise Exception
  return 
#-------------------------------------------
#--------------CLOSE-METHODS----------------
def close_pomodoro(ctx:nextcord.Interaction, session:Session) -> None:
  try:
    session.close.set('yes')
    session.pomodoro_started = False
    message_closed_pomodoro(ctx, session, embed)
  except:
    raise Exception
  return

async def after_30_seconds_close_pomodoro(bindFunc, ctx:nextcord.Interaction, session:Session, logger:logging.Logger) -> bool:
  try:
    session.addTrigger("throwClose")
    bind(bindFunc, "throwClose", ctx, session.ids, session, logger)
    triggerThrowPomodoroStatusClose=execWhen(30, throw_pomodoro_status_close, session, logger)
    triggerThrowPomodoroStatusClose.exec()
    triggerClosePomodoro=execWhen(30, close_pomodoro, ctx, session)
    triggerClosePomodoro.exec()
  except:
    raise Exception
  return True

async def sec30close(ctx:nextcord.Interaction, session:Session, logger:logging.Logger):
  try:
    triggerClosePomodoro=Trigger(30, close_pomodoro, ctx, session)
    triggerClosePomodoro.exec()
  except:
    logger.critical("Error in sec30close")
  return
#---------------------------------------------
#---------------------------------------------
#---------------SESSION-METHODS---------------
async def ch_session(dictio:dict, session:Session) -> bool:
  try:
    if dictio[session] is dictio['Main']:
      return True
    else:
      return False
  except:
    raise Exception 

async def new_session(dictio:dict) -> Session:
  dictio['Session_{number}'.format(number=len(dictio))]=Session()
  session=dictio.get('{Session_{number}}'.format(number=len(dictio)))
  return session

async def gather(dictio:dict) -> Session:
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

async def get_session_pomojoin(ctx:nextcord.Interaction, vChannel:nextcord.VoiceChannel, dictio:dict) -> Session:
  """This function get the current running session for command pomojoin"""
  for session in dictio.values():
    if hasattr(session.vc, 'channel'):
      if session.vc.channel is vChannel:
        return session
  return False #NoSessionRunning_pomojoin(ctx)

async def get_session(guild:nextcord.Guild, session_list:list) -> Session:
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

async def get_session_ps(ctx:nextcord.Interaction, vChannel:nextcord.VoiceChannel, dictio:dict) -> Session:
  """This function get the current running session for command pomostop"""
  for session in dictio.values():
    if hasattr(session.vc, 'channel'):
      if session.vc.channel is vChannel:
          return session
  return False #NoSessionRunning_pomostop(ctx)

async def session_handler(dictio:dict, session:Session):
  try:
    for key, value in dictio.items():
      if session == value:
          return key
  except:
    SM = logging.getLogger("SecurityMessage")
    SM.error("Error in session_handler")
    raise Exception

async def search(guild, session_list) -> int:
  for session in session_list:
    if session.get_guild_name() == guild.name:
      return session.get_index()

async def searchId(dictio:dict, ID:int) -> bool:
    HANDLER=None
    for value in dictio.values():
        for i_d in list(value.ids):
            print(i_d)
            if i_d is ID:
                HANDLER=True
    return HANDLER

async def fetchSession(guild:nextcord.Interaction.guild) -> Session:
  """Returns the session that the guild is binded"""
  index = await get_session(guild, guildList)
  session=guildList[index]
  dictio_session=session.session
  session=dictio_session["Main"]
  return session

async def leader(session:Session, ctx:nextcord.Interaction) -> None:
  """Sets session leader
  Leader joins the session automatically 
  Leader dont need to call pomojoin"""
  response=fetch(ctx)
  author=response[1]
  session.LEADER_ID=author.id
  session.pushleader()
  return
#-----------------------------------------
#-----------------------------------------
#-----------------------------------------
