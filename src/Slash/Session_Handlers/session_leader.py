#---------------IMPORTs-------------
from src.Slash.Utilitys.fetch_informations import fetch
#-----------------------------------

async def leader(session, ctx):
  """Sets session leader
  Leader joins the session automatically 
  Leader dont need to call pomojoin"""
  response=fetch(ctx)
  author=response[1]
  session.LEADER_ID=author.id
  session.pushleader()
  return