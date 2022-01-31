#This methods binds a function to a class allowing
#a change in this class execute the binded function
#---------------IMPORTS--------------
from Pomodoro.utilitys import exec_mute_all
#------------------------------------
#---------------FUNCTIONS-----------
def bind_status_class_to_mute_all(message, ids, session):
  try:
    status_class=session.status_class
    status_class.add_parameters(message)
    status_class.bind(exec_mute_all)
  except:
    print('ERROR IN bind_status_class_to_mute_all')
  return
#-----------------------------------