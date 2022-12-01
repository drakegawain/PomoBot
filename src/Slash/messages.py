#-------------------IMPORTS-------------------------
import asyncio
import nextcord
#---------------------------------------------------
async def message_avaiable_users_to_join(ctx:nextcord.Interaction, ids_mention, embed:nextcord.Embed):
  embed = embed.clear_fields()
  message = "Pomodoro starts in 30 seconds. The avaible users are:\n%s \nType `/pomojoin` to join pomodoro." % ids_mention
  embed.add_field(name = "Avaible users", value = message)
  await ctx.send(embed=embed)
  return

async def msg_slnt(ctx:nextcord.Interaction, embed:nextcord.Embed):
  embed = embed.clear_fields()
  message = "Pomodoro starts in 30 seconds. /pomojoin to join"
  embed.add_field(name = "Avaiable users", value = message)
  await ctx.send(embed=embed)
  return

def message_closed_pomodoro(ctx:nextcord.Interaction, session, embed:nextcord.Embed):
  embed = embed.clear_fields()
  message = "Pomodoro is now closed. Let's study!.\n{} minutes left.".format(int(session.study_time_global/60))
  embed.add_field(name = "Closed", value = message)
  loop = asyncio.get_running_loop()
  loop.run_until_complete(ctx.send(embed=embed))
  return

async def message_help(ctx:nextcord.Interaction, embed:nextcord.Embed):
  embed = embed.clear_fields()
  message = "According to discord new best practices, we are implementing Slash commands. **Try it out!** \n\n:handshake:`/pomodoro` to start a new pomodoro session \n\n:calling:`/pomojoin` to join a session [only necessary with two or more users] \n\n:hand_splayed:`/pomostop` to shut down the current session"
  embed.add_field(name = "Help", value = message)
  await ctx.send(embed=embed)
  return

async def message_time_to_rest(ctx:nextcord.Interaction, session, embed:nextcord.Embed):
  embed = embed.clear_fields()
  message = "\nTime to rest. \nYou have {} minute(s)."  .format(int(session.rest_time_global/60))
  embed.add_field(name = "Rest", value = message)
  await ctx.send(embed=embed)
  return

async def message_time_to_study(ctx:nextcord.Interaction, session, embed:nextcord.Embed):
  embed = embed.clear_fields()
  message = "Time to study/work. You have {} minute(s)."  .format(int(session.rest_time_global/60))
  embed.add_field(name = "Study", value = message)
  await ctx.send(embed=embed)
  return