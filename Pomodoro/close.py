#---------------IMPORTS------------------
from Discord_Actions.Messages.messages import message_closed_pomodoro
from Classes.classes import e_when_w_args, exec_repeatedly_functions
from Methods.throw_methods import throw_pomodoro_status_close
from Methods.bind_methods import bind_status_class_to_mute_all
import Configs.configs as cfg
#----------------------------------------
#--------------CLOSE-FUNCTIONS-----------
def close_pomodoro(message):
  session=cfg.session.get('{}'.format('Session1'))
  session.close.set('yes')
  session.pomodoro_started = False;
  message_closed_pomodoro(message)
  return

async def after_30_seconds_close_pomodoro(message):
  session=cfg.session.get('{}'.format('Session1'))
  bind_status_class_to_mute_all(message, session.ids)
  session.class_e=exec_repeatedly_functions(None, throw_pomodoro_status_close, 30)
  session.class_e.exec_when()
  session.class_i=e_when_w_args(30, close_pomodoro, message)
  session.class_i.exec()
  #cfg.class_e = exec_repeatedly_functions(None, throw_pomodoro_status_close, 30)
  #cfg.class_e.exec_when()
  #cfg.class_i = e_when_w_args(30, close_pomodoro, message)
  #cfg.class_i.exec()
  return
  #---------------------------------------