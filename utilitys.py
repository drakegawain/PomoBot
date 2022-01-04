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

async def repeatedly_execution(timeout_1, timeout_2, function_1, function_2, *args_1):
  while True:
    if (await timeout_function(timeout_1) == True):
      await function_1(*args_1);
      if (await timeout_function(timeout_2) == True):
        await function_2(*args_1);
  return

def _create_task(function, *args):
  task = asyncio.create_task(function(*args))
  return task

async def timeout_function(timeout):
  await asyncio.sleep(timeout)
  return True