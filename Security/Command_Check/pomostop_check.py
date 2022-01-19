#--------This-file-checks-if-the-user-that-----
#--------called-the-command-pomostop-is-in-----
#--------the-actual-session--------------------

#--------IMPORTs-----------
import Configs.configs as cfg
from Discord_Actions.Messages.security_messages import SecurityMessage
#--------------------------

async def check_pomostop(calling_id, message):
  try:
    list_ids=list(cfg.ids)
    if list_ids == []:
      raise Exception('TypeError')
    for id in list_ids:
      if id==calling_id:
        return True
  except:
    N_M=SecurityMessage('.pomostop', message, message.author.id)
    await N_M.send(101)
    return False
  return