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

class OutsideVoiceChannel(Error):
  """This class assign the error when user is outside a voice_channel"""
  def __init__(self, message):
    self.message=message
    N_M=SecurityMessage('.pomostop', message, message.author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(N_M.send(141))

class OutsideVoiceChannel_pjoin(Error):
  """This class assign the error when user is outside a voice_channel"""
  def __init__(self, message):
    self.message=message
    N_M=SecurityMessage('.pomojoin', message, message.author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(N_M.send(141))


async def get_session_pomojoin(message, v_channel, dictio:dict):
  """This function get the current running session for command pomojoin"""
  for session in dictio.values():
    if hasattr(session.vc, 'channel'):
      if session.vc.channel is v_channel:
        print(session)
        return session
  raise NoSessionRunning_pomojoin(message)
  return 

async def get_session_ps(message, v_channel, dictio:dict):
  """This function get the current running session for command pomostop"""
  for session in dictio.values():
    if hasattr(session.vc, 'channel'):
      if session.vc.channel is v_channel:
          return session
  raise NoSessionRunning_pomostop(message)
  return