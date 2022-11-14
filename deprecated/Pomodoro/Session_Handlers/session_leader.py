#---------------IMPORTs-------------
from Cli_Commands.Print_Padronization.ppadron import prntpdr
import Configs.configs as cfg
#-----------------------------------

async def leader(session, message):
  """Sets session leader
  Leader joins the session automatically 
  Leader dont need to call pomojoin"""
  session.LEADER_ID=message.author.id
  session.pushleader()
  prntpdr(cfg.normal, "leader id:{}".format(session.ids))
  return