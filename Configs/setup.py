import nest_asyncio
import Configs.configs as cfg
from Cli_Commands.Print_Padronization.ppadron import prntpdr
from Slash.Utilitys.fetch_informations import fetch
from Slash.Session_Handlers.get_session import get_session
import logging

def setup():
  prntpdr(cfg.black, "setting configurations...")
  LOGGER = logging.getLogger(__name__)
  LOGGER.setLevel(level = logging.WARNING)
  logging_handler=logging.FileHandler(filename='log.log', mode='a')
  logging_format=logging.Formatter('%(asctime)s - %(message)s')
  logging_handler.setFormatter(logging_format)
  LOGGER.addHandler(logging_handler)
  nest_asyncio.apply()
  prntpdr(cfg.black, "uploading PomoBot...")
  return LOGGER
  
async def get_silent(ctx):
  response = fetch(ctx)
  guild = response[2]
  index = await get_session(guild, cfg.session_guilds)
  session_class = cfg.session_guilds[index]
  dictio_session = session_class.session
  session = dictio_session['Main']
  print(session.silent)
  return session.silent