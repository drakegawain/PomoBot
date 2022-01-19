#------------IMPORTs----------
from Classes.classes import startup
import Configs.configs as cfg
#-----------------------------
#-------------START-----------
async def start_pomodoro():
  cfg.pomodoro_started = True;
  return
#-----------------------------
#-------------RESET-----------
async def startup_e():
  class_e = startup()
  class_e.start()
  return
async def reset_func():
  class_e = startup()
  class_e.start()
  return
#-----------------------------