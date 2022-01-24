#THIS FILE CHECK IF THE CALLING ID
#ALREADY IS IN ANOTHER SESSION
#IF YES RAISE AN ERROR
#-----------------IMPORTs-----------
from Pomodoro.Session_Handlers.search_session import s_for_id
from Discord_Actions.Messages.security_messages import SecurityMessage
import asyncio
#-----------------------------------

class Error(Exception):
  """Base Class for other exceptions"""

class MoreThanOneSession(Error):
  """USER CANT BE IN MORE THAN ONE SESSION"""
  def __init__(self, message):
    self.message=message
    self.N_M=SecurityMessage('pomodoro', message, message.author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(self.N_M.send(201))


async def c_for_doubles(dictio:dict, ID:int, message):
    search=await s_for_id(dictio, ID)
    if search is True:
        raise await MoreThanOneSession(message)
        return True
    else:
        return False
    return