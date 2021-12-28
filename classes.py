import asyncio
import configs as cfg
import time

class class_mute_all:
  def __init__(self, status):
    self.status = status;
    self.commands = [];
    self.parameters = [];
  def add_parameters(self, parameter):
    self.parameters.append(parameter)
    return 
  def set(self, status):
    self.status = status
    for x in self.commands:
      x(self.parameters[0], self.parameters[1])
  def bind(self, commands):
    self.commands.append(commands)

class exec_repeatedly_functions:
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
  def add_args(self, args):
    self.args.append(args)

class startup:
  def start(self):
    cfg.c = 0;
    cfg.pomodoro_started = False;
    cfg.ids_get = [];
    cfg.joined = 0;
    cfg.ids = set();
    cfg.study_time_global = 0;
    cfg.rest_time_global = 0;
    cfg.status_class = class_mute_all('none') 
    