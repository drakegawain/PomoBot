#------------IMPORTs----------
import Configs.configs as cfg
from Pomodoro.Session_Handlers.check_session import gather, ch_session, new_session
from Pomodoro.Session_Handlers.session_leader import leader
from Pomodoro.Session_Handlers.get_session import  get_session
from Cli_Commands.Print_Padronization.ppadron import prntpdr
#-----------------------------
#-------------START-----------
async def start_session(message):
  prntpdr(cfg.blue, "calling from:{} user:{}".format(message.guild.name, message.author))
  index=await get_session(message, cfg.session_guilds)
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
    await leader(session, message)
  else:
    reset(session)
    await leader(session, message)
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