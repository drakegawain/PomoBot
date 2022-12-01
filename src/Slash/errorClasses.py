class ExecError(Error):
  '''This class raises pomostop command'''
  def __init__(self, ctx, SM:logging.Logger):
    LOOP=asyncio.get_event_loop()
    LOOP.run_until_complete(stop(ctx, SM))
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
  """USER CANT BE IN MORE THAN ONE SESSION"""
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