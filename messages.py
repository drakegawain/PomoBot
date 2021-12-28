import asyncio
import configs as cfg

async def message_avaiable_users_to_join(message, ids_mention):
  await message.channel.send('\nPomodoro starts in 30 seconds. The avaible users are:\n%s \nType .join to join pomodoro. ' % ids_mention);
  return

def message_closed_pomodoro(message):
  loop = asyncio.get_running_loop()
  loop.run_until_complete(message.channel.send('\nPomodoro is now closed. The clock is ticking, go do some work/study.\n{} minutes left.' .format(int(cfg.study_time_global/60))));
  return

async def message_time_to_rest(message):
  await message.channel.send('\nTime to rest. \nYou have {} minutes.' .format(int(cfg.rest_time_global/60)));
  return

async def message_ask_for_restart(message):
  await message.channel.send('\nPomodoro is finished. Do you want to restart pomodoro? \n.yes or .no' );
  return