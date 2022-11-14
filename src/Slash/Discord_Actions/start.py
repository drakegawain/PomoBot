#------------IMPORTs----------
import src.Configs.configs as cfg
import logging
from src.Slash.Session_Handlers.check_session import gather, ch_session, new_session
from src.Slash.Session_Handlers.session_leader import leader
from src.Slash.Session_Handlers.get_session import  get_session
from src.Slash.Utilitys.fetch_informations import fetch
#-----------------------------
#-------------START-----------
async def start_session(ctx, logger:logging.Logger):
  response=fetch(ctx)
  guild=response[2]
  author=response[1]
  logger.warning("{} calling from:{} user:{}".format(__name__, guild.name, author.name))
  index=await get_session(guild, cfg.session_guilds)
  session_class=cfg.session_guilds[index]
  dictio_session=session_class.session
  last_session = await gather(dictio_session)
  isMain=await ch_session(dictio_session, last_session)
  if isMain is True:
    session=last_session
  else:
    session=await new_session(dictio_session)
  if type(session) is str:
    name_session=session
    session=dictio_session.get('{}'.format(name_session))
    reset(session)
    await leader(session, ctx)
  else:
    reset(session)
    await leader(session, ctx)
  return session

async def start_pomodoro(session):
  session.pomodoro_started=True
  return session
#-----------------------------
#-------------RESET-----------
async def startup_e(session):
  session.restart()
  return
async def reset_func(session):
  session.restart()
  return
def reset(session):
  session.restart()
  return
#-----------------------------