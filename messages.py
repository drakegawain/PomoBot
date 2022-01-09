#-----------------IMPORTs-----------
import asyncio
import configs as cfg
#-----------------------------------
#---------------MESSAGES--------------------
async def message_avaiable_users_to_join(message, ids_mention):
  await message.channel.send("```\nPomodoro starts in 30 seconds. The avaible users are:```\n%s ```\nType .join to join pomodoro.```" % ids_mention);
  return

def message_closed_pomodoro(message):
  loop = asyncio.get_running_loop()
  loop.run_until_complete(message.channel.send("```\nPomodoro is now closed. The clock is ticking, go do some work/study.\n{} minutes left.```"  .format(int(cfg.study_time_global/60))));
  return

async def message_time_to_rest(message):
  await message.channel.send("```\nTime to rest. \nYou have {} minutes.```"  .format(int(cfg.rest_time_global/60)));
  return

async def message_help(message):
   await message.channel.send("\n<@%s>```Every command that need inputs will be interpreted by the bot as minutes.\nCommands: \n.pomohelp - Show the avaible commands \n.pomodoro - Starts pomodoro, example: .pomodoro 25 15\n.pomojoin - Join the current pomodoro's session \n.pomostop - Unmute's everyone and stop the current session. ```"  % message.author.id)
   return

async def message_time_to_study(message):
  await message.channel.send("```\nTime to study/work. \nYou have {} minutes.```" .format(int(cfg.study_time_global/60)))
  return

async def message_error_pomostop(message):
  await message.channel.send('```\nBe sure you are in a voice channel and already started a pomodoro session using the command > .pomodoro (see the instructions in .pomohelp). \nIf you need help, type .pomohelp```')
  return
#--------------------------------------------
#-----------------UNIMPLEMENTED--------------
async def message_ask_for_restart(message):
  await message.channel.send("```\nPomodoro is finished. Do you want to restart pomodoro? \n.yes or .no ```" );
  return
#--------------------------------------------
