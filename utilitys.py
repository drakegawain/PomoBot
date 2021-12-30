import asyncio
from mute_unmute import mute_all, unmute_all;

def exec_mute_all(message, ids):
  loop = asyncio.get_running_loop()
  loop.run_until_complete(mute_all(message, ids))
  return

def exec_unmute_all(message, ids):
  loop = asyncio.get_running_loop()
  loop.run_until_complete(unmute_all(message, ids))
  return

async def repeatedly_execution(timeout, function, *args):
  while True:
    await asyncio.sleep(timeout)
    await function(*args);
  return

def _create_task(function, *args):
  task = asyncio.create_task(function(*args))
  #def _cancel_task():
   # _v.cancel()
    #return
  return task

