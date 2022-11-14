#This methods binds a function to a class allowing
#a change in this class execute the binded function
#---------------IMPORTS--------------
import logging
from src.Slash.Pomodoro.utilitys import exec_mute_all, sstdy
#------------------------------------
#---------------FUNCTIONS-----------
def bind_status_class_to_mute_all(ctx, ids, session, logger:logging.Logger):
  try:
    status_class=session.status_class
    status_class.add_parameters(ctx)
    status_class.bind(exec_mute_all)
  except:
    logger.warning("Error in {}".format(__name__))
    raise Exception
  return

def bind_status_class_silent(ctx, ids, session, logger:logging.Logger):
  try:
    status_class=session.status_class
    status_class.add_parameters(ctx)
    status_class.bind(sstdy)
  except:
    logger.critical("Error in bind_status_class_silent")
  return
#-----------------------------------