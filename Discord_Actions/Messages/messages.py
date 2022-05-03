#-----------------IMPORTs-----------
import asyncio
import Configs.configs as cfg
#-----------------------------------
#---------------MESSAGES--------------------
async def message_avaiable_users_to_join(message, ids_mention):
  await message.channel.send("```\nPomodoro starts in 30 seconds. The avaible users are:```\n%s ```\nType .pomojoin to join pomodoro.```" % ids_mention);
  return

def message_closed_pomodoro(message, session):
  loop = asyncio.get_running_loop()
  loop.run_until_complete(message.channel.send("```\nPomodoro is now closed. The clock is ticking, go do some work/study.\n{} minutes left.```"  .format(int(session.study_time_global/60))));
  return

async def message_time_to_rest(message, session):
  await message.channel.send("```\nTime to rest. \nYou have {} minutes.```"  .format(int(session.rest_time_global/60)));
  return

async def message_help(message):
   await message.channel.send(">>> <@%s> \n:man_mage: Hello! This is Pomobot. **Let's start?**\nCommands:\n \n:tools:`.pomohelp` - Show avaiable commands \n\n:handshake:`.pomodoro XX YY` - Starts pomodoro, Where XX is study time and YY is rest time => example: `.pomodoro 25 15`\n\n:calling:`.pomojoin` - Join current pomodoro's session \n\n:hand_splayed:`.pomostop` - Unmute's everyone and stop the current session. \n\n:cold_face:`.pomobug` - Found a bug? Report to us! \n\nAccording to discord new best practices, we are implementing Slash commands. **Try it out!** \n\n:handshake:`/pomodoro` \n\n:calling:`/pomojoin` \n\n:hand_splayed:`/pomostop`"  % message.author.id)
   return

async def message_time_to_study(message, session):
  await message.channel.send("```\nTime to study/work. \nYou have {} minutes.```" .format(int(session.study_time_global/60)))
  return

async def message_stopping_pomostop(message):
  await message.channel.send('\nStopping...\n\nYou can start a new session typing ``.pomodoro XX YY``.\nTo see the orientations: ``.pomohelp``')
  return
#--------------------------------------------
#-----------------UNIMPLEMENTED--------------
async def message_ask_for_restart(message):
  await message.channel.send("```\nPomodoro is finished. Do you want to restart pomodoro? \n.yes or .no ```" );
  return
#--------------------------------------------
