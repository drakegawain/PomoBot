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
    await message.channel.send('\nEvery command that need inputs will be interpreted by the bot in minutes.\n.commands - Show the avaible commands \n.pomodoro - Starts a pomodoro counter, example: .pomodoro 25 15\n .regressive -Starts a regressive counter, example: .regressive 10')

  if message.content.startswith('.pomodoro'):
    
    async def join(message):
      local = message.author.voice.channel;
      await message.author.voice.channel.connect();
    pomodoro = message.content;
    first_time = '';
    second_time = '';
    for char in pomodoro[9:12:1]:
      first_time = first_time + char;
    for char in pomodoro[12:15:1]:
      second_time = second_time + char;
  first_time = int(first_time)
  second_time = int(second_time)
  await join(message);


client.run(os.environ['TOKEN'])

