#-------------IMPORTs------------
import asyncio
#--------------------------------
#--------------WHEN-CLASS--------
class when:
  """#This file assigns the classes that manipulate variables
  the main class is when, that assigns a variable value to a function
  and sets a variable when_, when the variable value is changed its value to when_, the function is executed."""
  def __init__(self):
    self.value = 0
    self.when_ = 0
    self.functions = None
    self.args = None
    self.task = None
  def set(self, value):
    self.value = value
    if self.value == self.when_:
      self.task = asyncio.create_task(self.functions(*self.args))
  def if_when(self, when_):
    self.when_ = when_
  def set_functions(self, function):
    self.functions = function
  def set_args(self, *args):
    self.args = args
  def cancel(self):
    self.task.cancel()
#--------------------------------