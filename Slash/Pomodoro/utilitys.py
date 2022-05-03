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