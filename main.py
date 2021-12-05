import discord
import os
from threading import Timer

client = discord.Client()
c = 0;
pomodoro_started = False;
ids_get = [];

@client.event
async def on_ready():
  print('Logged in as {0.user}' .format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.commands'):
    await message.channel.send('\n<@%s>Every command that need inputs will be interpreted by the bot as minutes.\n.commands - Show the avaible commands \n.pomodoro - Starts a pomodoro counter, example: .pomodoro 25 15\n .regressive -Starts a regressive counter, example: .regressive 10' % message.author.id)
    return

  if message.content.startswith('.pomodoro'):
    async def join(message):
      global pomodoro_started
      pomodoro_started = True
      local = message.author.voice.channel;
      #guild = message.guild.id server ID
      await local.connect();
      channel = client.get_channel(local.id)
      keys = channel.voice_states.keys()
      list_keys = list(keys)
      #member_test = await client.fetch_user(list_keys[0]) members users
      i = len(list_keys)
      ids_mention = [];
      bot_id = client.user.id;
      for index in range(i):
        if list_keys[index] != bot_id:
          ids_mention.append(index);
          ids_mention[index] = '<@%s>' % list_keys[index]
      await message.channel.send('\nPomodoro starts in 30 seconds. The avaible users are:\n%s \nType .join to join pomodoro. ' % ids_mention)
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
    
    #colocar o timer de 30 segundos
    #depois dos 30 segundos, fechar a funcao join_pomodoro e mutar todos

  if message.content.startswith('.join'):
    async def join_pomodoro(message):
     if pomodoro_started == True:
        await message.channel.send('\n<@%s> Joined pomodoro' % message.author.id)
        global c
        c = c + 1;
        return

    async def get_ids(message):
      if pomodoro_started == False:
          await message.channel.send('\n<@%s> No pomodoro was started. Type .pomodoro XX XX (where XX is time in minutes) to start pomodoro and then type .join.' % message.author.id)
          return
      else:
          await join_pomodoro(message)
          global c
          global ids_get
          ids_get.append((c - 1))
          ids_get[(c - 1)] = message.author.id;
          return

    await get_ids(message)

client.run(os.environ['TOKEN'])

