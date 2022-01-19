#---------IMPORTs--------
import discord
#------------------------

#------------PLAY-SOME-AUDIO--------
async def play_audio(voice_channel, song):
  source = await discord.FFmpegOpusAudio.from_probe(song)
  voice_channel.play(source)
  return
#-----------------------------------