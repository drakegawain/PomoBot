#---------------IMPORTS------------------
import logging
from src.Slash.Discord_Actions.Messages.messages import message_closed_pomodoro
from src.Slash.Classes.classes import e_when_w_args 
from src.Slash.Methods.throw_methods import throw_pomodoro_status_close
from src.Slash.Methods.bind_methods import bind_status_class_to_mute_all, bind_status_class_silent
#----------------------------------------
#--------------CLOSE-FUNCTIONS-----------
def close_pomodoro(ctx, session):
  try:
    session.close.set('yes')
    session.pomodoro_started = False
    message_closed_pomodoro(ctx, session)
  except:
    raise Exception
  return

async def after_30_seconds_close_pomodoro(ctx, session, logger:logging.Logger):
  try:
    bind_status_class_to_mute_all(ctx, session.ids, session, logger)
    session.class_e=e_when_w_args(30, throw_pomodoro_status_close, session, logger)
    session.class_e.exec()
    session.class_i=e_when_w_args(30, close_pomodoro, ctx, session)
    session.class_i.exec()
  except:
    logger.warning("Error in {}".format(__name__))
  return

async def sec30close(ctx, session, logger):
  try:
    session.class_i=e_when_w_args(30, close_pomodoro, ctx, session)
    session.class_i.exec()
  except:
    logger.critical("Error in sec30close")
  return
  #---------------------------------------