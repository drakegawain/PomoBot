#-----------------IMPORTs-------------------
import logging
#-------------------------------------------
#---------------THROW-----------------------
def throw_pomodoro_status_close(session, logger:logging.Logger):
  """This method is called when the session needs to be closed. Then, a trigger is started
  and the bot mutes everyone that is inside the session"""
  try:
    status_class=session.status_class
    status_class.add_parameters(session.ids)
    status_class.add_parameters(session)
    status_class.set('close')
  except:
    logger.warning("Error in {}".format(__name__))
    raise Exception
  return 
#-------------------------------------------