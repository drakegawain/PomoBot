#-------------IMPORTS-----------------
from Handle_Variables.handle_joined import joined_function
import Configs.configs as cfg
#-------------------------------------
#-------------CONNECT-----------------
async def connect_to_voice_channel(message, session):
  try:
    channel = message.author.voice.channel;
    session.vc=await channel.connect()
  except:
    await message.channel.send('<@%s> ```\nYou have to be on a voice channel to start Pomobot. Enter a voice channel and try again.```' % (message.author.id))
    session.restart()
  return 

async def disconnect_from_voice_channel(message):
  for voice_client in cfg.client.voice_clients:
    if voice_client.guild.name == message.guild.name:
      await voice_client.guild.voice_client.disconnect()
        
  #channel = cfg.client.voice_clients
  #for chn in channel:
    #await chn.disconnect()
  return

async def join_pomodoro(message, session):
  if session.pomodoro_started is True:
    x = await joined_function(message, session)
    await message.channel.send('\n<@%s> %s' % (message.author.id,x))
    return
#------------------------------
