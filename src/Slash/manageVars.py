import logging
import nextcord
from ..Configs import configs as cfg
from ..Configs.configs import client
from .classes import Session

def fetch(ctx:nextcord.Interaction) -> list:
  """This function gather all usefull information from context interactions"""
  message=ctx.message
  guild=ctx.guild
  author=ctx.user
  return [message, author, guild]

async def get_keys(ctx:nextcord.Interaction):
  response=fetch(ctx)
  author=response[1]
  """this variable keys will be used to join voice_channel"""
  """from the message author"""
  channel = client.get_channel(author.voice.channel.id)
  keys = channel.voice_states.keys()
  return keys

async def bot_id():
  """get the bot id"""
  id_bot = client.user.id
  return id_bot

async def list_keys(keys):
  """transform keys into a list"""
  return list(keys)

async def handle_c(session:Session):
  """Manipulates the counter c from the config File
  C is used to assign the index in an array to 
  an id from the author that typed .join.
  It is used in get_ids"""
  if session.pomodoro_started is True:
    session.c=session.c+1
  

async def get_ids(ctx:nextcord.Interaction, session:Session, logger:logging.Logger):
  response=fetch(ctx)
  author=response[1]
  guild=response[2]
  if session.pomodoro_started is False:
    await ctx.send("\n<@%s> ```Pomodoro wasn't started. Type .pomodoro XX XX (where XX is time in minutes) to start pomodoro and then type .join.```"  % author.id)
  else:
    """assigns a index to a id, wich is a set
    id is saved in a set because a user cannot
    enter pomodoro more than once"""
    await handle_c(session)
    session.ids_get.append(session.c - 1)
    session.ids_get[session.c - 1]=author.id
    total_ids=set(session.ids_get)
    session.ids=total_ids
    logger.warning("{} ids:{} just joined {} session".format(__name__, session.ids, guild.name))
    await join_pomodoro(ctx, session)
    return
#---------------------------------------------------
#--------IMPORTS-------------
#----------------------------
#---------JOINED-OR-NOT------
async def join_pomodoro(ctx:nextcord.Interaction, session:Session):
  response=fetch(ctx)
  author=response[1]
  if session.pomodoro_started:
    joined = await joined_function(ctx, session)
    await ctx.send('\n<@%s> %s' % (author.id, joined))
    return

async def handle_joined(ctx:nextcord.Interaction, session:Session):
  """See if the user that try to join already joined"""
  response=fetch(ctx)
  author=response[1]
  ids_get=session.ids_get
  if ids_get.count(author.id)==1:
    session.joined=1
    return
  if ids_get.count(author.id)>1:
    session.joined=2
    return
  
async def joined_function(ctx:nextcord.Interaction, session:Session) -> str:
  """Handle joined variable"""
  await handle_joined(ctx, session)
  joined = session.joined
  if joined==1:
    return 'Joined'
  if joined==2:
    return 'Already Joined'
#------------------------------------------
#------------HANDLE-TIME-VARIABLES---------
async def handle_study_time(study_time) -> int:
  study_time = study_time * 60
  return study_time

async def handle_rest_time(rest_time) -> int:
  rest_time = rest_time * 60
  return rest_time
#------------------------------------------