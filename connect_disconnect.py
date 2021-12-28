from handle_joined import joined_function
import configs as cfg

async def connect_to_voice_channel(message):
  channel = message.author.voice.channel;
  await channel.connect()
  return

async def disconnect_from_voice_channel(message):
  channel = message.author.voice.channel;
  await channel.disconnect()
  return

async def join_pomodoro(message):
  if cfg.pomodoro_started == True:
    x = await joined_function(message)
    await message.channel.send('\n<@%s> %s' % (message.author.id,x))
    return