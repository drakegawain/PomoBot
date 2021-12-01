import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('Logged in as {0.user}' .format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.commands'):
    await message.channel.send('.commands - Show the avaible commands /n')

client.run(os.environ['TOKEN'])

