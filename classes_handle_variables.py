#This file asigns the classes that manipulate variables
import asyncio

class when:
  def __init__(self, function):
    self.value = 0
    self.when_ = 0
    self.functions = function 
  def set(self, value):
    self.value = value;
    if self.value == self.when_:
      self.set_tasks()
  def if_when(self, when_):
    self.when_ = when_
  class set_function:
    def __init__(self, **function):
      self.alambrado = function
      print(self.alambrado)
    class set_args:
      def __init__(self, *args):
        self.args = args
  def set_tasks(self):
      for key, value in self.set_function.alambrado.items():
        asyncio.create_task(value, *self.set_functions.set_args.args)