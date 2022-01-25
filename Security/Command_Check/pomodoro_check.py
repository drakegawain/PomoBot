from Discord_Actions.Messages.security_messages import SecurityMessage
import asyncio

class Error(Exception):
  """Base Class for other exceptions"""
    
class OneSessionPerVoiceChannel(Error):
    '''This class restrict only one session per voice channel'''
    print(True)
    def __init__(self, message):
        print('OneSessionPerVoiceChannel')
        self.message=message
        self.N_M=SecurityMessage('pomodoro', message, message.author.id)
        loop=asyncio.get_event_loop()
        loop.run_until_complete(self.N_M.send(271))
        return
    
async def check_pomodoro(context_vchannel, dictio:dict, message):
  check=None
  for session in dictio:
    if dictio[session].vc is context_vchannel:
      check=True
      raise OneSessionPerVoiceChannel(message)
    else:
      print('@check_pomodoro:false{}'.format('pass'))
      check=False
  return check