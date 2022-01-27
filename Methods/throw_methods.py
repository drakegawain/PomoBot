#-----------------IMPORTs-----------------
#-------------------------------------------


#---------------THROW--------------------
def throw_pomodoro_status_close(session):
  """This methods assigns functions that handle status_class"""
  try:
    status_class=session.status_class
    status_class.add_parameters(session.ids)
    status_class.add_parameters(session)
    status_class.set('close')
  except:
    raise Exception('ERROR IN: throw_pomodoro_status_close')
  return 
#----------------------------------------