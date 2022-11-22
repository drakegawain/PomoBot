from ....Slash.Discord_Actions.Messages.security_messages import SecurityMessage
from ....Slash.Utilitys.fetch_informations import fetch
import asyncio

class Error(Exception):
  """Base Class for other exceptions"""
    
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
    
async def check_pomodoro(context_vchannel, dictio:dict, ctx):
  check=0
  for session in dictio:
    if dictio["{}".format(session)].vc is context_vchannel:
      print(dictio["{}".format(session)])
      check=True
      raise OneSessionPerVoiceChannel(ctx)
  check=False
  return check