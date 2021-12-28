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

  #async def after_30_seconds_close_pomodoro(message):
 # global status_class
  #global ids
  #bind_status_class_to_mute_all(message, ids)
  #loop = asyncio.get_running_loop()
  #loop.call_later(30, throw_pomodoro_status_close)
#  loop.call_later(30, close_pomodoro, message)
 # loop.call_later((study_time_global + 30), throw_after_study_time_finished, message);
  #loop.call_later((study_time_global + rest_time_global + 30), throw_after_rest_time_finished, message);
  #return 
