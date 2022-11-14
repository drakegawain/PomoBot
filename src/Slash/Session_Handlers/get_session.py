from src.Slash.Discord_Actions.Messages.security_messages import SecurityMessage
from src.Slash.Utilitys.fetch_informations import fetch
import asyncio

class Error(Exception):
  '''Base error class'''

class OutsideVoiceChannel(Error):
  """This class assign the error when user is outside a voice_channel"""
  def __init__(self, ctx):
    response=fetch(ctx)
    author=response[1]
    self.ctx=ctx
    N_M=SecurityMessage('/pomostop', ctx, author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(N_M.send(141))

class OutsideVoiceChannel_pjoin(Error):
  """This class assign the error when user is outside a voice_channel"""
  def __init__(self, ctx):
    response=fetch(ctx)
    author=response[1]
    self.ctx=ctx
    N_M=SecurityMessage('/pomojoin', ctx, author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(N_M.send(141))

class NoSessionRunning_pomojoin(Error):
  """This class assign the error when there is no session running(.pomojoin)"""
  def __init__(self, ctx):
    response=fetch(ctx)
    author=response[1]
    self.ctx=ctx
    self.N_M=SecurityMessage('/pomojoin', ctx, author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(self.N_M.send(301))
    
class NoSessionRunning_pomostop(Error):
  """This class assign the error when there is no session running(.pomostop)"""
  def __init__(self, ctx):
    response=fetch(ctx)
    author=response[1]
    self.ctx=ctx
    self.N_M=SecurityMessage('/pomostop', ctx, author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(self.N_M.send(121))


async def get_session_pomojoin(ctx, v_channel, dictio:dict):
  """This function get the current running session for command pomojoin"""
  for session in dictio.values():
    if hasattr(session.vc, 'channel'):
      if session.vc.channel is v_channel:
        return session
  raise NoSessionRunning_pomojoin(ctx)
  return 

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
  return

