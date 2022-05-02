#-------------------IMPORTS-------------------------
import asyncio
#---------------------------------------------------

async def message_avaiable_users_to_join(ctx, ids_mention):
  await ctx.send("```\nPomodoro starts in 30 seconds. The avaible users are:```\n%s ```\nType .pomojoin to join pomodoro.```" % ids_mention);
  return

def message_closed_pomodoro(ctx, session):
  loop = asyncio.get_running_loop()
  loop.run_until_complete(ctx.send("```\nPomodoro is now closed. The clock is ticking, go do some work/study.\n{} minutes left.```"  .format(int(session.study_time_global/60))));
  return