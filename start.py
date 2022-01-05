#------------IMPORTs----------
from classes import startup
#-----------------------------
#-------------START-----------
async def start_pomodoro():
  import configs as cfg
  cfg.pomodoro_started = True;
  return
#-----------------------------
#-------------RESET-----------
async def startup_e():
  class_e = startup()
  class_e.start()
  return
#-----------------------------