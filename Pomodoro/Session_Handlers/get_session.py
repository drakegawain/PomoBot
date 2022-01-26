#--------------IMPORTs---------------
from Discord_Actions.Messages.security_messages import SecurityMessage
import asyncio
#------------------------------------

class Error(Exception):
  '''Base error class'''

class NoSessionRunning_pomojoin(Error):
  """This class assign the error when there is no session running(.pomojoin)"""
  def __init__(self, message):
    self.message=message
    self.N_M=SecurityMessage('pomojoin', message, message.author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(self.N_M.send(301))

class NoSessionRunning_pomostop(Error):
  """This class assign the error when there is no session running(.pomostop)"""
  def __init__(self, message):
    self.message=message
    self.N_M=SecurityMessage('pomostop', message, message.author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(self.N_M.send(121))
    
async def get_session_pomojoin(message, v_channel, dictio:dict):
  """This function get the current running session for command pomojoin"""
  SESSION=None
  for session in dictio:
    if dictio[session].vc is v_channel:
      SESSION=session
  if SESSION is None:
    raise NoSessionRunning_pomojoin(message)
  return SESSION

async def get_session_ps(message, v_channel, dictio:dict):
  """This function get the current running session for command pomostop"""
  for session in dictio.values():
    print(dictio[session])
    print(v_channel)
    if session.vc is v_channel:
        return session
  raise NoSessionRunning_pomostop(message)
  return