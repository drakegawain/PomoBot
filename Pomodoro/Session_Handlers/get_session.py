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

async def get_session(message, session_list:list):
  """This function finds the index from the list
    that handles the sessions"""
  guild_name=message.guild.name
  for index in range(len(session_list)):
    guild_name_session_list=session_list[index].get_guild_name()
    if guild_name_session_list is guild_name:
      return session_list[index].get_index()
  for index in range(len(session_list)+1):
    guild_name_session_list=session_list[index].get_guild_name()
    if guild_name_session_list is guild_name:
      return session_list[index].get_index()
#async def get_session(message, dictio:dict):
  #"""This function get the guild's session"""
  #guild_name = message.guild.name
  #session=None
  #for name in dictio.keys():
    #if name is guild_name:
      #session=dictio["{guild_name}".format(guild_name=name)]
  #return session

#async def get_dictio_session(session_name, dictio:dict):
  #"""This fuction returns the dictionary session from a session name"""
  #for name in dictio.keys():
    #if name is session_name:
      #dictio_session=dictio["{name}".format(name=name)]
  #return dictio_session