#--------This-file-checks-if-the-user-that-----
#--------called-the-command-pomostop-is-in-----
#--------the-actual-session--------------------

#--------IMPORTs-----------
from Slash.Discord_Actions.Messages.security_messages import SecurityMessage
from Slash.Utilitys.fetch_informations import fetch
import asyncio
#--------------------------

class Error(Exception):
  """Base error class"""

class UserOutsideSession(Error):
  def __init__(self, ctx):
    response=fetch(ctx)
    author=response[1]
    self.ctx=ctx
    N_M=SecurityMessage('.pomostop', ctx, author.id)
    loop=asyncio.get_event_loop()
    loop.run_until_complete(N_M.send(101))


async def check_pomostop(calling_id, ctx, session):
  try:
    list_ids=list(session.ids)#cfg.ids)
    if list_ids == []:
      raise Exception(TypeError)
    for id in list_ids:
      if id==calling_id:
        HANDLER=True
  except:
    raise UserOutsideSession(ctx)
    print('Error in: check_pomostop')
    HANDLER=False
  return HANDLER