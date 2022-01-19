#This methods binds a function to a class allowing
#a change in this class execute the binded function
#---------------IMPORTS--------------
import Configs.configs as cfg
from Pomodoro.utilitys import exec_mute_all, exec_unmute_all
from Classes.classes import class_mute_all
#------------------------------------
#---------------FUNCTIONS-----------
def bind_status_class_to_mute_all(message, ids):
  status_class = cfg.status_class
  status_class.add_parameters(message)
  status_class.bind(exec_mute_all)
  return

def bind_class_after_study_time(message):
  global ids
  after_study_time_class = class_mute_all('none');
  after_study_time_class.bind(exec_unmute_all);
  after_study_time_class.add_parameters(message);
  after_study_time_class.add_parameters(ids);
  return after_study_time_class

def bind_class_after_rest_time(message):
  after_rest_time_class = class_mute_all('none');
  after_rest_time_class.bind(exec_mute_all);
  after_rest_time_class.add_parameters(message);
  after_rest_time_class.add_parameters(ids);
  return after_rest_time_class
#-----------------------------------