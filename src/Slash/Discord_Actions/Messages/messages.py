#-------------------IMPORTS-------------------------
import asyncio
#---------------------------------------------------

async def message_avaiable_users_to_join(ctx, ids_mention):
  await ctx.send("```\nPomodoro starts in 30 seconds. The avaible users are:```\n%s ```\nType /pomojoin to join pomodoro.```" % ids_mention);
  return

async def msg_slnt(ctx):
  await ctx.send("```\nPomodoro starts in 30 seconds. /pomojoin to join```")
  return

def message_closed_pomodoro(ctx, session):
  loop = asyncio.get_running_loop()
  loop.run_until_complete(ctx.send("```\nPomodoro is now closed. Let's study!.\n{} minutes left.```"  .format(int(session.study_time_global/60))));
  return

async def message_help(ctx):
   await ctx.send(">>> \nAccording to discord new best practices, we are implementing Slash commands. **Try it out!** \n\n:handshake:`/pomodoro` to start a new pomodoro session \n\n:calling:`/pomojoin` to join a session [only necessary with two or more users] \n\n:hand_splayed:`/pomostop` to shut down the current session")
   return

async def message_time_to_rest(ctx, session):
  await ctx.send("```\nTime to rest. \nYou have {} minutes.```"  .format(int(session.rest_time_global/60)))
  return

async def message_time_to_study(ctx, session):
  await ctx.send("`\nTime to study/work. You have {} minutes.`" .format(int(session.study_time_global/60)))
  return