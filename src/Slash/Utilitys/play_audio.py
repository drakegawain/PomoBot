import nextcord

async def play_audio(voice_channel, song):
  source = await nextcord.FFmpegOpusAudio.from_probe(song)
  voice_channel.play(source)
  return