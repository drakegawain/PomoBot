#This find asigns the classes that will be used in the bot
#More details inside the classes

import asyncio
import configs as cfg

class class_mute_all:
  #this class is used to bind a function to a variable
  #when the variable is changed, the function binded is executed
  #the variable is changed with the method set
  def __init__(self, status):
    self.status = status;
    self.commands = [];
    self.parameters = [];
  def add_parameters(self, parameter):
    #this method handles the parameters of the binded function
    self.parameters.append(parameter)
    return 
  def set(self, status):
    self.status = status
    for x in self.commands:
      x(self.parameters[0], self.parameters[1])
  def bind(self, commands):
    self.commands.append(commands)

class exec_repeatedly_functions:
  #this class executes a function every interval (in seconds)
  #unimplemented
  def __init__(self, interval, function, break_when):
    self.interval = interval;
    self.function = function;
    self.logical = True
    self.break_when = break_when;
    self.args = [];
  def exec(self):
    loop = asyncio.get_running_loop()
    while True:
      loop.run_until_complete(self.function(self.args[0], self.args[1]))
      loop.sleep(self.interval)
  def exec_when(self):
    loop = asyncio.get_running_loop()
    loop.call_later(self.break_when, self.function)
  def stop(self):
    self.logical = False;
  def add_args(self, *args):
    for arg in args:
      self.args.append(arg)

class startup:
  #this class sets the global variables from file configs
  def start(self):
    cfg.c = 0;
    cfg.pomodoro_started = False;
    cfg.ids_get = [];
    cfg.joined = 0;
    cfg.ids = set();
    cfg.study_time_global = 0;
    cfg.rest_time_global = 0;
    cfg.status_class = class_mute_all('none')
    
class e_when_w_args:
  #this class executes a function after a timeout
  def __init__(self, timeout, function, *args):
    self.timeout= timeout
    self.function = function
    self.args = args
  def exec(self):
    loop = asyncio.get_running_loop()
    loop.call_later(self.timeout, self.function,  *self.args)

