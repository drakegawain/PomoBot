#---------------IMPORTs----------
import nextcord
import logging
import threading
import asyncio
from ..Classes.session import Session
from ...Configs import configs as cfg
from ...Configs.labor import Worker
from ...Configs.configs import client
from ...Configs.loops import loopMute, loopUnmute, loopExe, loopExe2, loopClient
from ...Slash.Utilitys.fetch_informations import fetch
#-------------------------------
#------------MUTE-UNMUTE-METHODs---------
async def mute_method(member:nextcord.Member):
  asyncio.set_event_loop(loopClient)
  asyncio.create_task(member.edit(mute=True))
  #w = Worker(loopClient, member.edit, kargs={"mute":True}, parent= threading.main_thread())
  return

async def deafen_method(member:nextcord.Member):
  asyncio.set_event_loop(loopClient)
  asyncio.create_task(member.edit(deafen=True))
  #w = Worker(loopClient, member.edit, kargs={"deafen":True}, parent=threading.main_thread())
  return

async def unmute_method(member:nextcord.Member):
  asyncio.set_event_loop(loopClient)
  asyncio.create_task(member.edit(mute=False))
  #w = Worker(loopClient, member.edit, kargs={"mute":False}, parent= threading.main_thread())
  return

async def undeafen_method(member:nextcord.Member):
  asyncio.set_event_loop(loopClient)
  asyncio.create_task(member.edit(deafen=False))
  #w = Worker(loopClient, member.edit, kargs={"deafen":False}, parent= threading.main_thread())
  return

async def mute_all(ctx:nextcord.Interaction, ids:list, session:Session, logger:logging.Logger):
  asyncio.set_event_loop(loopClient)
  response = fetch(ctx)
  guild = response[2].id
  got_guild = client.get_guild(guild)
  i_list = list(session.ids)
  logger.warning("muting:{}".format(i_list))
  for ids in i_list:  
    member = await got_guild.fetch_member(ids)
    #Worker(loopExe, mute_method, args=[member], parent = threading.main_thread())
    #Worker(loopExe2, deafen_method, args=[member], parent = threading.main_thread())
    asyncio.create_task(mute_method(member))
    asyncio.create_task(deafen_method(member))
  return

async def unmute_all(ctx:nextcord.Interaction, ids:list, session:Session, logger:logging.Logger):
  asyncio.set_event_loop(loopClient)
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
      asyncio.create_task(unmute_method(member))
      asyncio.create_task(undeafen_method(member))
    except:
      raise Exception
    #await unmute_method(member)
    #await undeafen_method(member)
  return
#----------------------------------------
