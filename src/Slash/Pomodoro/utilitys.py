#----IMPORTS----
import asyncio
import src.Configs.configs as cfg
import logging
from src.Slash.Discord_Actions.mute_unmute import mute_all, unmute_all
from src.Slash.Utilitys.play_audio import play_audio as play
from src.Slash.Utilitys.fetch_informations import fetch
from src.Slash.Session_Handlers.get_session import get_session
from src.Slash.Discord_Actions.user_members import mention_ids
from src.Slash.Commands.admin.pomostop_admin import stop
from src.Slash.Discord_Actions.Messages.messages import message_time_to_rest, message_time_to_study
#---------------

class Error(Exception):
  '''This is the base error class'''

class ExecError(Error):
  '''This class raises pomostop command'''
  def __init__(self, ctx, SM:logging.Logger):
    LOOP=asyncio.get_event_loop()
    LOOP.run_until_complete(stop(ctx, SM))
    return
  pass
  
def exec_mute_all(ctx, ids, session):
  response=fetch(ctx)
  guild=response[2]
  logger = logging.getLogger("Event")
  try:
    LOOP = asyncio.get_running_loop()
    #LOOP.run_until_complete(play(session.vc, "Sounds\Close.mp3"))
    LOOP.run_until_complete(mute_all(ctx, ids, session, logger))
  except:
    SM = logging.getLogger("SecurityMessage")
    SM.error("Error in {}: {}".format(__name__, guild.name))
    raise ExecError(ctx, SM)
  return

def exec_unmute_all(ctx, ids, session):
  response=fetch(ctx)
  guild=response[2]
  logger = logging.getLogger("Event")
  try:
    LOOP = asyncio.get_running_loop()
    LOOP.run_until_complete(unmute_all(ctx, ids, session, logger))
  except:
    SM = logging.getLogger("SecurityMessage")
    SM.error("Error in {}: {}".format(__name__, guild.name))
    raise ExecError(ctx, SM)
  return

def srest(ctx, session):
  LOOP=asyncio.get_running_loop()
  IDS_MENTION=LOOP.run_until_complete(mention_ids(session))
  LOOP.run_until_complete(
    ctx.send("Time to rest. \n%s \n`%i minutes`"%(IDS_MENTION, session.rest_time_global/60))  
  )
  return

def sstdy(ctx, session):
  LOOP=asyncio.get_running_loop()
  IDS_MENTION=LOOP.run_until_complete(mention_ids(session))
  LOOP.run_until_complete(
    ctx.send("Time to work/study. \n%s \n`%i minutes`" %(IDS_MENTION, session.rest_time_global/60)) 
  )
  return

async def timeout_function(timeout):
    await asyncio.sleep(timeout)
    return True

async def repeatedly_execution(timeout_1, timeout_2, function_1, function_2, *args_1):
  """execute function_1 after timeout_1 and function_2 after
  timeout_2 in loop"""
  while True:
    if (await timeout_function(timeout_1) == True):
      function_1(*args_1)
      if (await timeout_function(timeout_2) == True):
        function_2(*args_1)
  return

async def repeatedly_execution_with_sounds(session, timeout_1, timeout_2, function_1, function_2, *args_1):
  """execute function_1 after timeout_1 and function_2 after
  timeout_2 in loop"""
  while True:
    if (await timeout_function(timeout_1) == True):
      function_1(*args_1)
      await message_time_to_rest(args_1[0], session)
      await play(session.vc, "Sounds/Alarme.mp3")
      if (await timeout_function(timeout_2) == True):
        function_2(*args_1)
        await message_time_to_study(args_1[0], session)
  return