#This file sets functions that executes other functions

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
  #execute function_1 after timeout_1 and function_2 after
  #timeout_2 in loop
  from messages import message_time_to_rest
  from messages import message_time_to_study
  while True:
    if (await timeout_function(timeout_1) == True):
      await function_1(*args_1);
      await message_time_to_rest(args_1[0])
      if (await timeout_function(timeout_2) == True):
        await function_2(*args_1);
        await message_time_to_study(args_1[0])
  return

def _create_task(function, *args):
  #unimplemented
  task = asyncio.create_task(function(*args))
  return task

async def timeout_function(timeout):
  await asyncio.sleep(timeout)
  return True