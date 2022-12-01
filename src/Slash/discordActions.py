#-------------IMPORTS-----------------
import nextcord
import asyncio
import threading
import logging
from ..Configs import configs as cfg
from ..Configs.labor import Worker
from ..Configs.loops import loopClient
from .Utilitys.fetch_informations import fetch
#-------------------------------------
#-------------CONNECT-----------------
async def connect_to_voice_channel(ctx:nextcord.Interaction, session):
  #dont understand why this is not working
  response=fetch(ctx)
  author=response[1]
  channel = author.voice.channel
  def employee(loop:asyncio.AbstractEventLoop, ch):
   try: 
     asyncio.set_event_loop(loop) 
     loop.run_until_complete(ch.connect())
     threading.main_thread().join()
   except:
     raise Exception
  try:
   channel = author.voice.channel
   thread = threading.Thread(target = employee, args=[loopClient, channel])
   thread.start()
  except:
   await ctx.send('<@%s> ```\nYou have to be in a voice channel to start Pomobot. Enter a voice channel and try again.```' % (author.id))
   session.restart()
   raise Exception
  return 

async def disconnect_from_voice_channel(ctx):
  response=fetch(ctx)
  guild=response[2]
  for voice_client in cfg.client.voice_clients:
    if voice_client.guild.name == guild.name:
      await voice_client.guild.voice_client.disconnect()
  return

async def admin_disconnect(guild):
  for voice_client in cfg.client.voice_clients:
    if voice_client.guild.name == guild.name:
      await voice_client.guild.voice_client.disconnect()
  return

async def join_pomodoro(ctx, session):
  response=fetch(ctx)
  author=response[1]
  if session.pomodoro_started:
    joined = await joined_function(ctx, session)
    await ctx.send('\n<@%s> %s' % (author.id, joined))
    return
#----------------------------------------
#----------------------------------------
#------------MUTE-UNMUTE-METHODs---------
async def mute_method(member:nextcord.Member):
  asyncio.run_coroutine_threadsafe(member.edit(mute=True), loopClient)
  #w = Worker(loopClient, member.edit, kargs={"mute":True}, parent= threading.main_thread())
  return

async def deafen_method(member:nextcord.Member):
  asyncio.run_coroutine_threadsafe(member.edit(deafen=True), loopClient)
  #w = Worker(loopClient, member.edit, kargs={"deafen":True}, parent=threading.main_thread())
  return

async def unmute_method(member:nextcord.Member):
  asyncio.run_coroutine_threadsafe(member.edit(mute=False), loopClient)
  #w = Worker(loopClient, member.edit, kargs={"mute":False}, parent= threading.main_thread())
  return

async def undeafen_method(member:nextcord.Member):
  asyncio.run_coroutine_threadsafe(member.edit(deafen=False), loopClient)
  #w = Worker(loopClient, member.edit, kargs={"deafen":False}, parent= threading.main_thread())
  return

async def mute_all(ctx:nextcord.Interaction, ids:list, session:Session, logger:logging.Logger):
  response = fetch(ctx)
  guild = response[2].id
  got_guild = client.get_guild(guild)
  i_list = list(session.ids)
  logger.warning("muting:{}".format(i_list))
  for ids in i_list:  
    member = await got_guild.fetch_member(ids)
    #Worker(loopExe, mute_method, args=[member], parent = threading.main_thread())
    #Worker(loopExe2, deafen_method, args=[member], parent = threading.main_thread())
    asyncio.run_coroutine_threadsafe(mute_method(member), loopClient)
    asyncio.run_coroutine_threadsafe(deafen_method(member), loopClient)
  return

async def unmute_all(ctx:nextcord.Interaction, ids:list, session:Session, logger:logging.Logger):
  response = fetch(ctx)
  guild = response[2].id
  gotGuild = client.get_guild(guild)
  iList=list(session.ids)
  logger.warning("unmuting:{}".format(iList))
  for ids in iList:
    member = await gotGuild.fetch_member(ids)
    #Worker(loopExe, unmute_method, args=[member])
    #Worker(loopExe, undeafen_method, args=[member])
    try:
      asyncio.run_coroutine_threadsafe(unmute_method(member), loopClient)
      asyncio.run_coroutine_threadsafe(undeafen_method(member), loopClient)
    except:
      raise Exception
    #await unmute_method(member)
    #await undeafen_method(member)
  return
#-----------------------------
#-------------START-----------
async def start_session(ctx, logger:logging.Logger):
  response=fetch(ctx)
  guild=response[2]
  author=response[1] 
  logger.warning("{} calling from:{} user:{}".format(__name__, guild.name, author.name))
  index=await get_session(guild, cfg.session_guilds)
  session_class=cfg.session_guilds[index]
  dictio_session=session_class.session
  last_session = await gather(dictio_session)
  isMain=await ch_session(dictio_session, last_session)
  if isMain is True:
    session=last_session
  else:
    session=await new_session(dictio_session)
  if type(session) is str:
    name_session=session
    session=dictio_session.get('{}'.format(name_session))
    #reset(session)
    await leader(session, ctx)
  else:
    reset(session)
    await leader(session, ctx)
  return session

async def start_pomodoro(session):
  session.pomodoro_started=True
  return session
#-----------------------------
#-------------RESET-----------
async def startup_e(session):
  session.restart()
  return
async def reset_func(session):
  session.restart()
  return
def reset(session):
  session.restart()
  return
#-----------------------------

async def mention_ids(session):
  IDS_MENTION = []
  IDS_MENTION=list(session.ids)
  for INDEX, ID in enumerate(IDS_MENTION):
    IDS_MENTION[INDEX] = "<@%s>" % IDS_MENTION[INDEX]
  return IDS_MENTION

async def avaiable_users_to_join(list_keys, bot_id):
  """This function finds the avaiable users to participate the study/work"""
  ids_mention = []
  i = len(list_keys)
  for index in range(i):
    if list_keys[index] != bot_id:
      ids_mention.append(index)
      ids_mention[index] = '<@%s>' % list_keys[index]
      return ids_mention

#----------------------------------------------
#-------------------EXE------------------------
#----------------------------------------------
def exec_mute_all(ctx, ids, session):
  response=fetch(ctx)
  guild=response[2]
  logger = logging.getLogger("Event")
  try:
    asyncio.run_coroutine_threadsafe(mute_all(ctx, ids, session, logger), loop=loopClient)
    #LOOP = asyncio.get_running_loop()
    #LOOP.run_until_complete(mute_all(ctx, ids, session, logger))
  except:
    SM = logging.getLogger("SecurityMessage")
    SM.error("Error in {}: {}".format(__name__, guild.name))
    raise ExecError(ctx, SM)
  return

def exec_unmute_all(ctx, ids, session):
  response=fetch(ctx)
  guild=response[2]
  logger = logging.getLogger("Event")
  try:
    asyncio.run_coroutine_threadsafe(unmute_all(ctx, ids, session, logger), loop=loopClient)
    #LOOP = asyncio.get_running_loop()
    #LOOP.run_until_complete(unmute_all(ctx, ids, session, logger))
  except:
    SM = logging.getLogger("SecurityMessage")
    SM.error("Error in {}: {}".format(__name__, guild.name))
    raise ExecError(ctx, SM)
  return

def srest(ctx, session):
  LOOP=asyncio.get_running_loop()
  IDS_MENTION=LOOP.run_until_complete(mention_ids(session))
  LOOP.run_until_complete(
    ctx.send("Time to rest. \n%s \n`%i minutes`"%(IDS_MENTION, session.rest_time_global/60))  
  )
  return

def sstdy(ctx, session):
  LOOP=asyncio.get_running_loop()
  IDS_MENTION=LOOP.run_until_complete(mention_ids(session))
  LOOP.run_until_complete(
    ctx.send("Time to work/study. \n%s \n`%i minutes`" %(IDS_MENTION, session.rest_time_global/60)) 
  )
  return

async def timeout_function(timeout):
    await asyncio.sleep(timeout)
    return True

async def repeatedly_execution(timeout_1, timeout_2, function_1, function_2, *args_1):
  """execute function_1 after timeout_1 and function_2 after
  timeout_2 in loop"""
  while True:
    if (await timeout_function(timeout_1) == True):
      function_1(*args_1)
      if (await timeout_function(timeout_2) == True):
        function_2(*args_1)
  return

async def repeatedly_execution_with_sounds(session, timeout_1, timeout_2, function_1, function_2, *args_1):
  """execute function_1 after timeout_1 and function_2 after
  timeout_2 in loop"""
  #have to fix the play function, current not working
  funcArgs = list(args_1)
  funcArgs.pop(len(args_1)-1)
  funcArgs.pop(len(args_1)-2)
  while True:
    if (await timeout_function(timeout_1) == True):
      try:
        function_1(*funcArgs)
        asyncio.run_coroutine_threadsafe(message_time_to_rest(args_1[0], session, args_1[len(args_1)-1]), loopClient)
        #asyncio.run_coroutine_threadsafe(play(session.vc, "...Sounds\Alarme.mp3"), loopClient)
      except:
        raise Exception
      if (await timeout_function(timeout_2) == True):
        #asyncio.run_coroutine_threadsafe(play(session.vc, "...Sounds/Close.mp3"), loopClient)
        #loopClient.call_later(2.5, function_2, *funcArgs)??
        function_2(*funcArgs)
        asyncio.run_coroutine_threadsafe(message_time_to_study(args_1[0], session, args_1[len(args_1)-1]), loopClient)
#--------------------------------------------------
#-----------------------PLAY-----------------------
#--------------------------------------------------
async def play_audio(voice_channel, song):
  try:
    source = await nextcord.FFmpegOpusAudio.from_probe(song)
    voice_channel.play(source)
  except:
    raise Exception
  return