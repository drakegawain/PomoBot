import nextcord

async def play_audio(voice_channel, song):
  try:
    source = await nextcord.FFmpegOpusAudio.from_probe(song)
    voice_channel.play(source)
  except:
    raise Exception
  return