#-----------------IMPORTs-----------------
#-------------------------------------------
#This methods assigns functions that handle status_class

#---------------THROW--------------------
def throw_pomodoro_status_close(session):
  try:
    print('throw_pomodoro_status_close')
    status_class=session.status_class
    status_class.add_parameters(session.ids)
    status_class.add_parameters(session)
    print(status_class.commands)
    print(status_class.parameters)
    status_class.set('close')
    print(status_class.status)
  except:
    raise Exception('ERROR IN: throw_pomodoro_status_close')
  return 

#----------------------------------------