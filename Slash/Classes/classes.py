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
    self.FUTURE=None;
  def exec(self):
    loop = asyncio.get_running_loop()
    self.FUTURE=loop.create_future()
    HANDLE=loop.call_later(self.TIMEOUT, self.FUNCTION,  *self.ARGS)
    self.FUTURE.add_done_callback(lambda *args:HANDLE.cancel())
  def release_future(self):
    if not self.FUTURE.done():
      self.FUTURE.set_result(None)