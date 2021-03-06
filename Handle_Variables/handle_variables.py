#----------------IMPORTS-------------
from Configs.configs import client
from Discord_Actions.connect_disconnect import join_pomodoro
from Cli_Commands.Print_Padronization.ppadron import prntpdr
import Configs.configs as cfg
#------------------------------------
#----------------MANIPULATEs VARIABLEs-------------
async def get_keys(message):
  """this variable keys will be used to join voice_channel"""
  """from the message author"""
  channel = client.get_channel(message.author.voice.channel.id);
  keys = channel.voice_states.keys();
  return keys

async def bot_id():
  """get the bot id"""
  id_bot = client.user.id;
  return id_bot

async def list_keys(keys):
  """transform keys into a list"""
  keys_list = list(keys);
  return keys_list;

async def handle_c(session):
  """manipulates the counter c from the config File
  c is used to assign the index in an array to 
  an id from the author that typed .join
  is used in get_ids"""
  if session.pomodoro_started is True:
    session.c=session.c+1
  

async def get_ids(message, session):
  if session.pomodoro_started is False:
    await message.channel.send("\n<@%s> ```Pomodoro wasn't started. Type .pomodoro XX XX (where XX is time in minutes) to start pomodoro and then type .join.```"  % message.author.id)
  else:
    """assigns a index to a id, wich is a set
    id is saved in a set because a user cannot
    enter the pomodoro more than once"""
    await handle_c(session);
    session.ids_get.append(session.c - 1)
    session.ids_get[session.c - 1]=message.author.id
    total_ids=set(session.ids_get)
    session.ids=total_ids
    prntpdr(cfg.normal, "ids:{} just joined {} session".format(session.ids, message.guild.name))
    await join_pomodoro(message, session)
    return
#---------------------------------------------------
#----------------------UNIMPLEMENTED----------------
#--------------------------------------------------