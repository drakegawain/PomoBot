#-----------------IMPORTs-----------------
import asyncio
import configs as cfg
from bind_methods import bind_class_after_study_time, bind_class_after_rest_time
from messages import message_time_to_rest, message_ask_for_restart
#-------------------------------------------
#This methods assigns functions that handle status_class

#---------------THROW--------------------
def throw_pomodoro_status_close():
  status_class = cfg.status_class
  status_class.add_parameters(cfg.ids)
  status_class.set('close')
  print(status_class.status)
  return 

def throw_after_study_time_finished(message):
  global ids
  class_e = bind_class_after_study_time(message)
  class_e.set('finish')
  loop = asyncio.get_running_loop()
  loop.run_until_complete(message_time_to_rest(message))
  return

def throw_after_rest_time_finished(message):
  class_e = bind_class_after_rest_time(message)
  class_e.set('rest_time_finish')
  loop = asyncio.get_running_loop()
  loop.run_until_complete(message_ask_for_restart(message))
  return
#----------------------------------------