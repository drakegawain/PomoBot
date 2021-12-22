import discord
import os
import threading
import asyncio
import nest_asyncio

#-----------------Discord Configurations--------
nest_asyncio.apply()
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#-----------------Classes----------------------

class class_mute_all:
  def __init__(self, status):
    self.status = status;
    self.commands = [];
    self.parameters = [];
  def add_parameters(self, parameter):
    self.parameters.append(parameter)
    return 
  def set(self, status):
    self.status = status
    for x in self.commands:
      x(self.parameters[0], self.parameters[1])
  def bind(self, commands):
    self.commands.append(commands)


#-----------------Global Variables-------------
c = 0;
pomodoro_started = False;
ids_get = [];
joined = 0;
ids = set();
study_time_global = 0;
rest_time_global = 0;
status = 'none';
status_class = class_mute_all('none')

#------------------FUNCTIONS-------------------

#------------------Utilitys-------------------

def exec_mute_all(message, ids):
  loop = asyncio.get_running_loop()
  loop.run_until_complete(mute_all(message, ids))
  return

def exec_unmute_all(message, ids):
  loop = asyncio.get_running_loop()
  loop.run_until_complete(unmute_all(message, ids))
  return

#------------------Setups----------------------

def throw_pomodoro_status_close():
  global status_class
  status_class.add_parameters(ids)
  status_class.set('close')
  print(status_class.status)
  return 

def throw_after_study_time_finished(message):
  global ids
  class_e = bind_class_after_study_time(message)
  class_e.set('finish')
  loop = asyncio.get_running_loop()
  loop.run_until_complete(message_time_to_rest(message))
  return

def bind_status_class_to_mute_all(message, ids):
  global status_class
  status_class.add_parameters(message)
  status_class.bind(exec_mute_all)
  return

def bind_class_after_study_time(message):
  after_study_time_class = class_mute_all('none');
  after_study_time_class.bind(exec_unmute_all);
  after_study_time_class.add_parameters(message);
  after_study_time_class.add_parameters(ids);
  return after_study_time_class

async def after_30_seconds_close_pomodoro(message):
  global status_class
  global ids
  bind_status_class_to_mute_all(message, ids)
  loop = asyncio.get_running_loop()
  loop.call_later(30, throw_pomodoro_status_close)
  loop.call_later(30, close_pomodoro, message)
  loop.call_later(study_time_global, throw_after_study_time_finished, message);
  return 

#-----------------STARTUPS---------------------


#------------------Messages--------------------

async def message_avaiable_users_to_join(message, ids_mention):
  await message.channel.send('\nPomodoro starts in 30 seconds. The avaible users are:\n%s \nType .join to join pomodoro. ' % ids_mention);
  return

def message_closed_pomodoro(message):
  global study_time_global
  loop = asyncio.get_running_loop()
  loop.run_until_complete(message.channel.send('\nPomodoro is now closed. The clock is ticking, go do some work/study.\n{} minutes left.' .format(int(study_time_global/60))));
  return

async def message_time_to_rest(message):
  global rest_time_global
  await message.channel.send('\nTime to rest. \nYou have {} minutes.' .format(int(rest_time_global/60)));
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

def close_pomodoro(message):
  global pomodoro_started;
  pomodoro_started = False;
  message_closed_pomodoro(message)
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
          total_ids = set(ids_get)
          ids = total_ids;
          print(ids);
          await join_pomodoro(message)
          return

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

def sinc_mute_all(message, ids):
  guild = message.author.voice.channel.guild.id;
  got_guild = client.get_guild(guild);
  ids_list = list(ids);
  new_client_loop = asyncio.get_running_loop()
  for ids in ids_list:
    member = got_guild.get_member(ids);
    new_client_loop.run_until_complete(member.edit(mute=True))
    new_client_loop.run_until_complete(member.edit(deafen=True))
  return print('pass')

def sinc_unmute_all(message, ids):
  guild = message.author.voice.channel.guild.id;
  got_guild = client.get_guild(guild);
  ids_list = list(ids);
  new_client_loop = asyncio.get_running_loop()
  for ids in ids_list:
    member = got_guild.get_member(ids);
    new_client_loop.run_until_complete(member.edit(mute=False))
    new_client_loop.run_until_complete(member.edit(deafen=False))
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
  time_study = ''
  for char in pomodoro[9:12:1]:
    time_study = time_study + char;
  return int(time_study);

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

async def disconnect_from_voice_channel(message):
  channel = message.author.voice.channel;
  await channel.disconnect()
  return

async def join_pomodoro(message):
  if pomodoro_started == True:
    x = await joined_function(message)
    await message.channel.send('\n<@%s> %s' % (message.author.id,x))
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

    #---------------TIME VARIABLES--------------
    global study_time_global, rest_time_global;
    study_time_global = await handle_study_time(await study_time(message));
    rest_time_global = await handle_rest_time(await rest_time(message));

    #----------------START----------------------
    await start_pomodoro();
    await connect_to_voice_channel(message);
    await message_avaiable_users_to_join(message, await avaiable_users_to_join(await list_keys(await get_keys(message)), await bot_id())); 

    #---------------CLOSE-----------------------
    await after_30_seconds_close_pomodoro(message);


  if message.content.startswith('.join'):
    await get_ids(message)

  if message.content.startswith('.mute'):
    await mute_all(message, ids);

  if message.content.startswith('.unmute'):
    await unmute_all(message, ids);

#---------------IF-EXECUTE------------------


client.run(os.environ['TOKEN'])

