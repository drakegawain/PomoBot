#This methods binds a function to a class allowing
#a change in this class execute the binded function
#---------------IMPORTS--------------
from Slash.Pomodoro.utilitys import exec_mute_all, sstdy

#------------------------------------
#---------------FUNCTIONS-----------
def bind_status_class_to_mute_all(ctx, ids, session):
  try:
    status_class=session.status_class
    status_class.add_parameters(ctx)
    status_class.bind(exec_mute_all)
  except:
    print('Error in bind_status_class_to_mute_all')
  return

def bind_status_class_silent(ctx, ids, session, logger):
  try:
    status_class=session.status_class
    status_class.add_parameters(ctx)
    status_class.bind(sstdy)
  except:
    logger.critical("Error in bind_status_class_silent")
  return
#-----------------------------------