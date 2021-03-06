#--------------IMPORTS---------------
import asyncio
#------------------------------------
#--------------MUTE-CLASS------------
class class_mute_all:
  """this class is used to bind a function to a variable
  when the variable is changed, the function binded is executed
  the variable is changed with the method set"""
  def __init__(self, status):
    self.status = status;
    self.commands = [];
    self.parameters = [];
  def add_parameters(self, parameter):
    """this method handles the parameters of the binded function"""
    self.parameters.append(parameter)
    return 
  def set(self, status):
    self.status = status
    for x in self.commands:
      x(self.parameters[0], self.parameters[1], self.parameters[2])
  def bind(self, commands):
    self.commands.append(commands)
#-------------------------------------
#-------------UNIMPLEMENTED-----------
class exec_repeatedly_functions:
  """this class executes a function every interval (in seconds)"""
  def __init__(self, interval, function, break_when):
    self.interval = interval;
    self.function = function;
    self.logical = True
    self.break_when = break_when;
    self.args = [];
    self.FUTURE=None
  def exec(self):
    loop = asyncio.get_running_loop()
    while True:
      loop.run_until_complete(self.function(self.args[0], self.args[1]))
      loop.sleep(self.interval)
  def exec_when(self):
    loop = asyncio.get_running_loop()
    self.FUTURE = loop.create_future()
    HANDLE = loop.call_later(self.break_when, self.function)
    self.FUTURE.add_done_callback(lambda *args:HANDLE.cancel())
  def stop(self):
    self.logical = False;
  def add_args(self, *args):
    for arg in args:
      self.args.append(arg)
  def release_future(self):
    if not self.FUTURE.done():
      self.FUTURE.set_result(None)
#--------------------------------------
#---------------RESET------------------

#--------------------------------------
#------------------TIME----------------
class e_when_w_args:
  """this class executes a function after a timeout"""
  def __init__(
    self, TIMEOUT, FUNCTION, *ARGS
  ):
    self.TIMEOUT=TIMEOUT
    self.FUNCTION=FUNCTION
    self.ARGS=ARGS
    self.FUTURE=None;
  def exec(self):
    loop = asyncio.get_running_loop()
    self.FUTURE=loop.create_future()
    HANDLE=loop.call_later(self.TIMEOUT, self.FUNCTION,  *self.ARGS)
    self.FUTURE.add_done_callback(lambda *args:HANDLE.cancel())
  def release_future(self):
    if not self.FUTURE.done():
      self.FUTURE.set_result(None)
#---------------------------------------
