#---------------IMPORTS------------------
from messages import message_closed_pomodoro
from classes import e_when_w_args, exec_repeatedly_functions
from throw_methods import throw_pomodoro_status_close
from bind_methods import bind_status_class_to_mute_all
import configs as cfg
#----------------------------------------
#--------------CLOSE-FUNCTIONS-----------
def close_pomodoro(message):
  cfg.close.set('yes')
  cfg.pomodoro_started = False;
  message_closed_pomodoro(message)
  return

async def after_30_seconds_close_pomodoro(message):
  from close import close_pomodoro
  bind_status_class_to_mute_all(message, cfg.ids)
  class_e = exec_repeatedly_functions(None, throw_pomodoro_status_close, 30)
  class_e.exec_when()
  class_i = e_when_w_args(30, close_pomodoro, message)
  class_i.exec()
  return
  #---------------------------------------