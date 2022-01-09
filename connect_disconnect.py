#-------------IMPORTS-----------------
from handle_joined import joined_function
import configs as cfg
#-------------------------------------
#-------------CONNECT-----------------
async def connect_to_voice_channel(message):
  try:
    channel = message.author.voice.channel;
    await channel.connect()
  except:
    await message.channel.send('<@%s> ```\nYou have to be on a voice channel to start Pomobot. Enter a voice channel and try again.```' % (message.author.id))
  return

async def disconnect_from_voice_channel():
  channel = cfg.client.voice_clients
  for chn in channel:
    await chn.disconnect()
  return

async def join_pomodoro(message):
  if cfg.pomodoro_started == True:
    x = await joined_function(message)
    await message.channel.send('\n<@%s> %s' % (message.author.id,x))
    return
#------------------------------
