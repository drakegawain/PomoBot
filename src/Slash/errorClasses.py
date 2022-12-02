import asyncio
import logging
import nextcord
from .classes import SecurityMessage
from .manageVars import fetch
from .manageClasses import fetchSession

class Error(Exception):
    """Base error class"""

class ExecError(Error):
  '''This class raises pomostop command'''
  def __init__(self, func=None, *args):
    if func != None:
      self.func = func
    else:
      self.func = self.__stop()
    self.args = args
    self.__embed = [arg for arg in self.args if arg.__name__ == "embed"][0]
    self.__ctx = [ctx for ctx in self.args if ctx.__name__ == "ctx"][0]
    self.__embed.clear_fields()
    self.__loop = asyncio.get_event_loop()
    message = "Some error ocurred, stopping..."
    self.__embed.add_field(name="Error", value=message)
    self.__loop.run_until_complete(func(*args))
    self.__embed.send(self.__ctx)
  def __stop(self):
    __guild = fetch(self.__ctx)[2]
    __session = self.__loop.run_until_complete(fetchSession(__guild))
    __session.__restart()
    return
  pass

class OneSessionPerVoiceChannel(Error):
    '''This class restrict only one session per voice channel'''
    print('True')
    def __init__(self, ctx):
        response=fetch(ctx)
        author=response[1]
        self.ctx=ctx
        self.N_M=SecurityMessage('pomodoro', ctx, author.id)
        loop=asyncio.get_event_loop()
        loop.run_until_complete(self.N_M.send(271))
        return
    
class UserOutsideSession(Error):
  def __init__(self, ctx):
    response=fetch(ctx)
    author=response[1]
    self.ctx=ctx
    N_M=SecurityMessage('/pomostop', ctx, author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(N_M.send(101))

class MoreThenOneSession(Error):
  """User cant be in more then one session"""
  def __init__(self, ctx):
    response=fetch(ctx)
    author=response[1]
    self.ctx=ctx
    self.N_M=SecurityMessage('pomodoro', ctx, author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(self.N_M.send(201))

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