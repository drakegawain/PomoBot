#----------------IMPORTS-------------
from configs import client
import configs as cfg
#------------------------------------
#----------------MANIPULATEs VARIABLEs-------------
async def get_keys(message):
  #this variable keys will be used to join voice_channel
  #from the message author
  channel = client.get_channel(message.author.voice.channel.id);
  keys = channel.voice_states.keys();
  return keys

async def bot_id():
  #get the bot id
  id_bot = client.user.id;
  return id_bot

async def list_keys(keys):
  #transform keys into a list
  keys_list = list(keys);
  return keys_list;

async def handle_c():
  #manipulates the counter c from the config File
  #c is used to assigns the index in a array to 
  #a id from the author that typed .join
  ##
  #is used in get_ids
  if cfg.pomodoro_started == True:
    cfg.c = cfg.c + 1;

async def get_ids(message):
  from handle_variables import handle_c
  from connect_disconnect import join_pomodoro
  if cfg.pomodoro_started == False:
    #if clock didnt start, send the message
    await message.channel.send("\n<@%s> ```Pomodoro wasn't started. Type .pomodoro XX XX (where XX is time in minutes) to start pomodoro and then type .join.```"  % message.author.id)
    return
  else:
    #assigns a index to a id, wich is a set
    #id is saved in a set because a user cannot
    #enter the pomodoro more than once
    await handle_c();
    cfg.ids_get.append((cfg.c - 1))
    cfg.ids_get[(cfg.c - 1)] = message.author.id;
    total_ids = set(cfg.ids_get)
    cfg.ids = total_ids;
    print(cfg.ids);
    await join_pomodoro(message)
    return
#---------------------------------------------------
#----------------------UNIMPLEMENTED----------------
#async def check_ids(id):
  #global c, ids_get;
 # x = ids_get.index(id);
  #if len(ids_get) == 1:
  #  return
  #if len(ids_get) != 1:
  #  for y in range((x+1), len(ids_get)):
    #  if ids_get[y] == id:
     #   print('Already joined')
      #  ids_get.pop(y);
      #  c = len(ids_get);
#--------------------------------------------------