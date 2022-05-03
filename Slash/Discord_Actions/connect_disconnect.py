#-------------IMPORTS-----------------
from Slash.Handle_Variables.handle_joined import joined_function
from Slash.Utilitys.fetch_informations import fetch
import Configs.configs as cfg
#-------------------------------------
#-------------CONNECT-----------------
async def connect_to_voice_channel(ctx, session):
  response=fetch(ctx)
  author=response[1]
  try:
    channel = author.voice.channel;
    session.vc=await channel.connect()
  except:
    await ctx.send('<@%s> ```\nYou have to be on a voice channel to start Pomobot. Enter a voice channel and try again.```' % (author.id))
    session.restart()
  return 

async def disconnect_from_voice_channel(ctx):
  response=fetch(ctx)
  guild=response[2]
  for voice_client in cfg.client.voice_clients:
    if voice_client.guild.name == guild.name:
      await voice_client.guild.voice_client.disconnect()
        
  #channel = cfg.client.voice_clients
  #for chn in channel:
    #await chn.disconnect()
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
