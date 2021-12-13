import discord
import os
from threading import Timer

#-----------------Discord Configurations--------

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#-----------------Initial Variables-------------
c = 0;
pomodoro_started = False;
ids_get = [];
joined = 0;
ids = set();
study_time = 0;
rest_time = 0;

#------------------FUNCTIONS-------------------

#------------------Messages--------------------

async def message_avaiable_users_to_join(message, ids_mention):
  await message.channel.send('\nPomodoro starts in 30 seconds. The avaible users are:\n%s \nType .join to join pomodoro. ' % ids_mention);
  return

#------------------Users/Members---------------

async def avaiable_users_to_join(list_keys, bot_id):
  ids_mention = [];
  i = len(list_keys);
  for index in range(i):
    if list_keys[index] != bot_id:
      ids_mention.append(index);
      ids_mention[index] = '<@%s>' % list_keys[index]
      return ids_mention

#------------------Handle variables------------

async def start_pomodoro():
  global pomodoro_started;
  pomodoro_started = True;
  return

async def get_keys(message):
  channel = client.get_channel(message.author.voice.channel.id);
  keys = channel.voice_states.keys();
  return keys

async def bot_id():
  id_bot = client.user.id;
  return id_bot

async def list_keys(keys):
  keys_list = list(keys);
  return keys_list;

#------------------Mute/unmute-----------------

async def mute_method(member):
  await member.edit(mute=True);
  return

async def deafen_method(member):
  await member.edit(deafen=True);
  return

async def unmute_method(member):
  await member.edit(mute=False);
  return

async def undeafen_method(member):
  await member.edit(deafen=False);
  return

async def mute_all(message, ids):
  guild = message.author.voice.channel.guild.id;
  got_guild = client.get_guild(guild);
  ids_list = list(ids)
  for ids in ids_list:
    member = got_guild.get_member(ids);
    await mute_method(member);
    await deafen_method(member);
  return
  
async def unmute_all(message, ids):
  guild = message.author.voice.channel.guild.id;
  got_guild = client.get_guild(guild);
  ids_list = list(ids);
  for ids in ids_list:
    member = got_guild.get_member(ids);
    await unmute_method(member)
    await undeafen_method(member);
  return

#---------------Time------------------

async def handle_study_time(study_time):
  study_time = study_time * 60;
  return study_time

async def handle_rest_time(rest_time):
  rest_time = rest_time * 60;
  return rest_time;

async def study_time(message):
  pomodoro = message.content;
  study_time = ''
  for char in pomodoro[9:12:1]:
    study_time = study_time + char;
  return int(study_time)

async def rest_time(message):
  pomodoro = message.content;
  rest_time = ''
  for char in pomodoro[12:15:1]:
    rest_time = rest_time + char;
  return int(rest_time)

#--------------Connect/Join-----------

async def connect_to_voice_channel(message):
  channel = message.author.voice.channel;
  await channel.connect()
  return

#-------------------EVENTS--------------------

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
    global study_time, rest_time;
    study_time = await handle_study_time(first_time)
    rest_time = await handle_rest_time(second_time)
    print(study_time)
    print(rest_time)
    await join(message);
    
    #colocar o timer de 30 segundos
    #depois dos 30 segundos, fechar a funcao join_pomodoro e mutar todos

  if message.content.startswith('.join'):

    async def handle_joined(message):
      global joined;
      global ids_get;
      if ids_get.count(message.author.id) == 1:
        joined = 1;
        return
      if ids_get.count(message.author.id) > 1:
        joined = 2;
        return

    async def joined_function(message):
      global joined;
      await handle_joined(message);
      if joined == 1:
        return 'Joined'
      if joined == 2:
        return 'Already Joined'

    async def handle_c():
      global c;
      global pomodoro_started;
      if pomodoro_started == True:
        c = c + 1;

    async def join_pomodoro(message):
      
     if pomodoro_started == True:
        x = await joined_function(message)
        await message.channel.send('\n<@%s> %s' % (message.author.id,x))
        return

    async def check_ids(id):
      global c, ids_get;
      x = ids_get.index(id);
      if len(ids_get) == 1:
        return
      if len(ids_get) != 1:
        for y in range((x+1), len(ids_get)):
          if ids_get[y] == id:
            print('Already joined')
            ids_get.pop(y);
            c = len(ids_get);

    async def get_ids(message):
      if pomodoro_started == False:
          await message.channel.send('\n<@%s> Pomodoro wasnt started. Type .pomodoro XX XX (where XX is time in minutes) to start pomodoro and then type .join.' % message.author.id)
          return
      else:
          await handle_c();
          global c
          global ids_get
          global ids
          ids_get.append((c - 1))
          ids_get[(c - 1)] = message.author.id;
          #await check_ids(message.author.id);
          total_ids = set(ids_get)
          ids = total_ids;
          print(ids);
          await join_pomodoro(message)
          return 
  
    await get_ids(message)

  if message.content.startswith('.mute'):
    await mute_all(message, ids);

  if message.content.startswith('.unmute'):
    await unmute_all(message, ids);

client.run(os.environ['TOKEN'])

