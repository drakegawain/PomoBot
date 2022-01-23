#------------IMPORTs----------
import Configs.configs as cfg
from Pomodoro.Session_Handlers.check_session import gather, ch_session, new_session
from Pomodoro.Session_Handlers.session_leader import leader
#-----------------------------
#-------------START-----------

async def start_session():
  last_session = await gather(cfg.session)
  isMain= await ch_session(cfg.session, last_session)
  if isMain is True:
    session=last_session
  else:
    session=await new_session
  return session

async def start_pomodoro(session):
  session.pomodoro_started=True
  return session
#-----------------------------
#-------------RESET-----------
async def startup_e(session):
  #session=cfg.session.get('{}'.format('Session1'))
  session.restart()
  return
async def reset_func(session):
  #session=cfg.session.get('{}'.format('Session1'))
  session.restart()
  return
#-----------------------------