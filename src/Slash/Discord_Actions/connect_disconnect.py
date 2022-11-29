#-------------IMPORTS-----------------
import nextcord
import asyncio
import threading
from ...Configs import configs as cfg
from ...Configs.labor import Worker
from ...Configs.loops import loopConnect, loopClient
from ...Slash.Handle_Variables.handle_joined import joined_function
from ...Slash.Utilitys.fetch_informations import fetch
#-------------------------------------
#-------------CONNECT-----------------
async def connect_to_voice_channel(ctx:nextcord.Interaction, session):
  #loop = asyncio.new_event_loop()
  #asyncio.set_event_loop(loop)
  response=fetch(ctx)
  author=response[1]
  channel = author.voice.channel
  asyncio.get_running_loop().set_debug(True)
  try:
    task = asyncio.create_task(channel.connect(), name="connect")
    print(task.done())
  except:
    asyncio.create_task(ctx.send('<@%s> ```\nYou have to be in a voice channel to start Pomobot. Enter a voice channel and try again.```' % (author.id)))
    session.restart()
    raise Exception
  #def employee(loop:asyncio.AbstractEventLoop, ch, parent:threading.Thread):
  #  asyncio.set_event_loop(loop)
  #  try:
  #    loop.run_until_complete(ch.connect())
  ##    parent.join()
  #  except:
  #    raise Exception
  #try:
  #  channel = author.voice.channel
  #  thread = threading.Thread(target = employee, args=[loopConnect, channel, parent])
  #  thread.start()
  #except:
  #  await ctx.send('<@%s> ```\nYou have to be in a voice channel to start Pomobot. Enter a voice channel and try again.```' % (author.id))
  #  session.restart()
  #  raise Exception
  return 

async def disconnect_from_voice_channel(ctx):
  response=fetch(ctx)
  guild=response[2]
  for voice_client in cfg.client.voice_clients:
    if voice_client.guild.name == guild.name:
      await voice_client.guild.voice_client.disconnect()
  return

async def admin_disconnect(guild):
  for voice_client in cfg.client.voice_clients:
    if voice_client.guild.name == guild.name:
      await voice_client.guild.voice_client.disconnect()
  return

async def join_pomodoro(ctx, session):
  response=fetch(ctx)
  author=response[1]
  if session.pomodoro_started is True:
    x = await joined_function(ctx, session)
    await ctx.send('\n<@%s> %s' % (author.id,x))
    return
#------------------------------
