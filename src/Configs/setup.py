import nest_asyncio
import src.Configs.configs as cfg
from src.cli.ppadron import prntpdr
from src.Slash.Utilitys.fetch_informations import fetch
from src.Slash.Session_Handlers.get_session import get_session
from src.Configs.loggers import EVENTLOG, SMLOG, GLDRSRCLOG

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