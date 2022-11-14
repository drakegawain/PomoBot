#----------------IMPORTs-------------------
from Discord_Actions.Messages.security_messages import SecurityMessage
import asyncio
from Commands.pomostop import command_pomostop
#------------------------------------------
#--------------Exception-------------------
class Error(Exception):
  '''Base error class'''
  
class InputsMustBeInteger(Error):
  def __init__(self, message):
    self.message=message
    self.N_M=SecurityMessage('pomodoro', message, message.author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(self.N_M.send(221))
    loop.run_until_complete(command_pomostop(message))

class MustHaveTwoInputs(Error):
  def __init__(self, message):
    self.message=message
    self.N_M=SecurityMessage('pomodoro', message, message.author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(self.N_M.send(251))
    loop.run_until_complete(command_pomostop(message))
#------------------------------------------
#------------HANDLE-TIME-VARIABLES---------
async def handle_study_time(study_time):
  study_time = study_time * 60
  return study_time

async def handle_rest_time(rest_time):
  rest_time = rest_time * 60
  return rest_time
#------------------------------------------
#-------------GET-TIME-VARIABLES-----------
async def study_time(message):
  pomodoro = message.content
  time_study = ''
  for char in pomodoro[9:12:1]:
    time_study = time_study + char
  try:
    final_time=int(time_study)
  except:
    raise InputsMustBeInteger(message)
  return final_time

async def rest_time(message):
  pomodoro = message.content
  rest_time = ''
  for char in pomodoro[12:15:1]:
    rest_time = rest_time + char
  if rest_time == '':
    raise MustHaveTwoInputs(message)
  try:
    rest_time=int(rest_time)
  except:
    raise InputsMustBeInteger(message)
  return rest_time
#--------------------------------------------
  