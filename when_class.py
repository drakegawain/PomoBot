#This file assigns the classes that manipulate variables
#the main class is when, that assigns a variable value to a function
#and sets a variable when_, when the variable value is changed its value to when_, the function is executed.
import asyncio

class when:
  def __init__(self):
    self.value = 0
    self.when_ = 0
    self.functions = None
    self.args = None
  def set(self, value):
    self.value = value;
    if self.value == self.when_:
      asyncio.create_task(self.functions(*self.args))
  def if_when(self, when_):
    self.when_ = when_
  def set_functions(self, function):
    self.functions = function;
  def set_args(self, *args):
    self.args = args
    