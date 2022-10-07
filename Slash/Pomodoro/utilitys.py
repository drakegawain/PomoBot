#----IMPORTS----
import asyncio
import Configs.configs as cfg
from Slash.Discord_Actions.mute_unmute import mute_all, unmute_all
from Slash.Utilitys.fetch_informations import fetch
from Cli_Commands.Print_Padronization.ppadron import prntpdr
from Commands.admin.pomostop_admin import admin_pomostop
#---------------

class Error(Exception):
  '''This is the base error class'''

class ExecError(Error):
  '''This class raises pomostop command'''
  def __init__(self, ctx):
    loop=asyncio.get_event_loop()
    loop.run_until_complete(admin_pomostop(ctx))
    prntpdr(cfg.red, "ExecError:stopping")
    return
  pass
  
def exec_mute_all(ctx, ids, session):
  response=fetch(ctx)
  guild=response[2]
  try:
    loop = asyncio.get_running_loop()
    loop.run_until_complete(mute_all(ctx, ids, session))
  except:
    prntpdr(cfg.red, "error in exec_mute_all: {}".format(guild.name))
    raise ExecError(ctx)
  return

def exec_unmute_all(ctx, ids, session):
  response=fetch(ctx)
  guild=response[2]
  try:
    loop = asyncio.get_running_loop()
    loop.run_until_complete(unmute_all(ctx, ids, session))
  except:
    prntpdr(cfg.red, "error in exec_unmute_all: {}".format(guild.name))
    raise ExecError(ctx)
  return

def srest(ctx, ids, rest_time):
  ctx.send("Time to rest. <@{ids}> [{rest}] minutes".format(ids=ids, rest=rest_time/60))
  return

def sstdy(ctx, ids, study_time):
  ctx.send("Time to work/study. <@{ids}> [{study}] minutes".format(ids=ids, study=study_time/60))
  return

async def timeout_function(timeout):
    await asyncio.sleep(timeout)
    return True

async def repeatedly_execution(session, timeout_1, timeout_2, function_1, function_2, *args_1):
  """execute function_1 after timeout_1 and function_2 after
  timeout_2 in loop"""
  argmt1=args_1.append(timeout_1)
  argmt2=args_1.append(timeout_2)
  while True:
    if (await timeout_function(timeout_1) == True):
      function_1(argmt1);
      if (await timeout_function(timeout_2) == True):
        function_2(argmt2);
  return