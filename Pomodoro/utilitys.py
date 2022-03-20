#This file sets functions that executes other functions
#-----------------IMPORTs---------------------
import asyncio
from Discord_Actions.mute_unmute import mute_all, unmute_all;
from Discord_Actions.Messages.messages import message_time_to_rest, message_time_to_study
from Discord_Actions.play_audio import play_audio
from Cli_Commands.Print_Padronization.ppadron import prntpdr
import Configs.configs as cfg
from Commands.pomostop import command_pomostop
#---------------------------------------------
#------------------Error-Class----------------
class Error(Exception):
  '''This is the base error class'''

class ExecError(Error):
  '''This class raises pomostop command'''
  def __init__(self, message):
    await command_pomostop(message)
    prntpdr(cfg.red, "ExecError:stopping")
  pass
#---------------------------------------------
#-------------------EXEs-----------------------
def exec_mute_all(message, ids, session):
  try:
    loop = asyncio.get_running_loop()
    loop.run_until_complete(mute_all(message, ids, session))
  except:
    prntpdr(cfg.red, "error in exec_mute_all: {}".format(message.guild.name))
    raise ExecError(message)
  return

def exec_unmute_all(message, ids, session):
  try:
    loop = asyncio.get_running_loop()
    loop.run_until_complete(unmute_all(message, ids, session))
  except:
    prntpdr(cfg.red, "error in exec_unmute_all: {}".format(message.guild.name))
    raise ExecError(message)
  return
#----------------------------------------------
#------------------LOOPs------------------------
async def repeatedly_execution(session, timeout_1, timeout_2, function_1, function_2, *args_1):
  """execute function_1 after timeout_1 and function_2 after
  timeout_2 in loop"""
  while True:
    if (await timeout_function(timeout_1) == True):
      function_1(*args_1);
      await message_time_to_rest(args_1[0], session)
      await play_audio(session.vc, 'Sounds/Alarme.mp3')
      if (await timeout_function(timeout_2) == True):
        function_2(*args_1);
        await message_time_to_study(args_1[0], session)
        await play_audio(session.vc, 'Sounds/Close.mp3')
  return
#----------------------------------------------
#------------------SLEEP-----------------------
async def timeout_function(timeout):
    await asyncio.sleep(timeout)
    return True
#----------------------------------------------
#----------------UNIMPLEMENTED-----------------
#----------------------------------------------

