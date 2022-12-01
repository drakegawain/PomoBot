import nest_asyncio
from ..Configs import configs as cfg
from ..cli.ppadron import prntpdr
from ..Slash.manageClasses import fetch, get_session
from ..Configs.loggers import EVENTLOG, SMLOG, GLDRSRCLOG

def setup():
  prntpdr(cfg.black, "setting configurations...")
  EVENTLOG()
  SMLOG()
  GLDRSRCLOG()
  nest_asyncio.apply()
  prntpdr(cfg.black, "uploading PomoBot...")
  return 
  
async def get_silent(ctx):
  response = fetch(ctx)
  guild = response[2]
  index = await get_session(guild, cfg.session_guilds)
  session_class = cfg.session_guilds[index]
  dictio_session = session_class.session
  session = dictio_session['Main']
  print(session.silent)
  return session.silent