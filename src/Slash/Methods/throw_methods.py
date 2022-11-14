#-----------------IMPORTs-------------------
import logging
#-------------------------------------------
#---------------THROW--------------------
def throw_pomodoro_status_close(session, logger:logging.Logger):
  """This methods assigns functions that handle status_class"""
  try:
    status_class=session.status_class
    status_class.add_parameters(session.ids)
    status_class.add_parameters(session)
    status_class.set('close')
  except:
    logger.warning("Error in {}".format(__name__))
    raise Exception
  return 
#----------------------------------------