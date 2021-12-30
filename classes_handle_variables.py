#This file asigns the classes that manipulate variables

class when:
  def __init__(self, function):
    self.value = 0
    self.when_ = 0
    self.functions = function 
  def set(self, value):
    self.value = value;
    if self.value == self.when_:
      for function in self.functions:
        function()
  def if_when(self, when_):
    self.when_ = when_
  def set_functions(self, *function):
    self.functions = function