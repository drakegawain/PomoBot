#---------------IMPORTS------------------
from Slash.Discord_Actions.Messages.messages import message_closed_pomodoro
from Classes.classes import e_when_w_args 
from Methods.throw_methods import throw_pomodoro_status_close
from Slash.Methods.bind_methods import bind_status_class_to_mute_all, bind_status_class_silent
#----------------------------------------
#--------------CLOSE-FUNCTIONS-----------
def close_pomodoro(ctx, session):
  session.close.set('yes')
  session.pomodoro_started = False;
  message_closed_pomodoro(ctx, session)
  return

async def after_30_seconds_close_pomodoro(ctx, session):
  try:
    bind_status_class_to_mute_all(ctx, session.ids, session)
    session.class_e=e_when_w_args(30, throw_pomodoro_status_close, session)
    session.class_e.exec()
    session.class_i=e_when_w_args(30, close_pomodoro, ctx, session)
    session.class_i.exec()
  except:
    print('ERROR IN after_30_seconds_close_pomodoro')
  return

async def sec30close(ctx, session, logger):
  try:
    session.class_i=e_when_w_args(30, close_pomodoro, ctx, session)
    session.class_i.exec()
  except:
    logger.critical("Error in sec30close")
  return
  #---------------------------------------