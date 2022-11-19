#-------------IMPORTs------------
import asyncio
#--------------------------------
class e_when_w_args:
  """this class executes a function after a timeout"""
  def __init__(
    self, TIMEOUT, FUNCTION, *ARGS
  ):
    self.TIMEOUT=TIMEOUT
    self.FUNCTION=FUNCTION
    self.ARGS=ARGS
    self.FUTURE=None
  def exec(self):
    loop = asyncio.get_running_loop()
    self.FUTURE=loop.create_future()
    HANDLE=loop.call_later(self.TIMEOUT, self.FUNCTION,  *self.ARGS)
    self.FUTURE.add_done_callback(lambda *args:HANDLE.cancel())
  def release_future(self):
    if not self.FUTURE.done():
      self.FUTURE.set_result(None)
  
class class_mute_all:
  """This class is used to bind a function to a variable.
  When this variable is changed, the function binded is executed and
  the variable is changed with the method set"""
  def __init__(self, status):
    self.status = status
    self.commands = []
    self.parameters = []
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