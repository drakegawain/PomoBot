#---------------IMPORTs----------
from configs import client
import configs as cfg
#-------------------------------
#------------MUTE-UNMUTE-METHODs---------
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
  cfg.ids_list = list(cfg.ids)
  for ids in cfg.ids_list:
    member = got_guild.get_member(ids);
    await mute_method(member);
    await deafen_method(member);
  return
  
async def unmute_all(message, ids):
  guild = message.author.voice.channel.guild.id;
  got_guild = client.get_guild(guild);
  cfg.ids_list = list(cfg.ids);
  for ids in cfg.ids_list:
    member = got_guild.get_member(ids);
    await unmute_method(member)
    await undeafen_method(member);
  return
#----------------------------------------
#---------------UNIMPLEMENTED-------------
  #def sinc_mute_all(message, ids):
#  guild = message.author.voice.channel.guild.id;
#  got_guild = client.get_guild(guild);
#  ids_list = list(ids);
#  new_client_loop = asyncio.get_running_loop()
#  for ids in ids_list:
#    member = got_guild.get_member(ids);
#    new_client_loop.run_until_complete(member.edit(mute=True))
 #   new_client_loop.run_until_complete(member.edit(deafen=True))
#  return print('pass')

#def sinc_unmute_all(message, ids):
  #guild = message.author.voice.channel.guild.id;
  #got_guild = client.get_guild(guild);
  #ids_list = list(ids);
 # new_client_loop = asyncio.get_running_loop()
  #for ids in ids_list:
    ##member = got_guild.get_member(ids);
   # new_client_loop.run_until_complete(member.edit(mute=False))
   # new_client_loop.run_until_complete(member.edit(deafen=False))
 # return
 #--------------------------------------