#------------IMPORTs----------
from Classes.classes import startup
import Configs.configs as cfg
#-----------------------------
#-------------START-----------
async def start_pomodoro():
  session=cfg.session.get('{}'.format('Session1'))
  session.pomodoro_started=True
  #cfg.pomodoro_started = True;
  return
#-----------------------------
#-------------RESET-----------
async def startup_e():
  session=cfg.session.get('{}'.format('Session1'))
  session.restart()
  #class_e = startup()
  #class_e.start()
  return
async def reset_func():
  session=cfg.session.get('{}'.format('Session1'))
  session.restart()
  #class_e = startup()
  #class_e.start()
  return
#-----------------------------