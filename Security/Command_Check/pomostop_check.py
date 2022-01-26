#--------This-file-checks-if-the-user-that-----
#--------called-the-command-pomostop-is-in-----
#--------the-actual-session--------------------

#--------IMPORTs-----------
import Configs.configs as cfg
from Discord_Actions.Messages.security_messages import SecurityMessage
import asyncio
#--------------------------

class Error(Exception):
  """Base error class"""

class UserOutsideSession(Error):
  def __init__(self, message):
    self.message=message
    N_M=SecurityMessage('.pomostop', message, message.author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(N_M.send(101))


async def check_pomostop(calling_id, message, session):
  try:
    list_ids=list(session.ids)#cfg.ids)
    if list_ids == []:
      raise Exception(TypeError)
    for id in list_ids:
      if id==calling_id:
        HANDLER=True
  except:
    raise UserOutsideSession(message)
    print('Error in: check_pomostop')
    HANDLER=False
  return HANDLER