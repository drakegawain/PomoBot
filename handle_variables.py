from configs import client
import configs as cfg

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

async def handle_c():
  if cfg.pomodoro_started == True:
    cfg.c = cfg.c + 1;

async def get_ids(message):
  from handle_variables import handle_c
  from connect_disconnect import join_pomodoro
  if cfg.pomodoro_started == False:
    await message.channel.send("\n<@%s> ```Pomodoro wasn't started. Type .pomodoro XX XX (where XX is time in minutes) to start pomodoro and then type .join.```"  % message.author.id)
    return
  else:
    await handle_c();
    cfg.ids_get.append((cfg.c - 1))
    cfg.ids_get[(cfg.c - 1)] = message.author.id;
    total_ids = set(cfg.ids_get)
    cfg.ids = total_ids;
    print(cfg.ids);
    await join_pomodoro(message)
    return

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