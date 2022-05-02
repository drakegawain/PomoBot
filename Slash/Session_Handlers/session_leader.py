#---------------IMPORTs-------------
from Cli_Commands.Print_Padronization.ppadron import prntpdr
from Slash.Utilitys.fetch_informations import fetch
import Configs.configs as cfg
#-----------------------------------

async def leader(session, ctx):
  """Sets session leader
  Leader joins the session automatically 
  Leader dont need to call pomojoin"""
  response=fetch(ctx)
  author=response[1]
  session.LEADER_ID=author.id
  session.pushleader()
  prntpdr(cfg.normal, "leader id:{}".format(session.ids))
  return