#---------------IMPORTs----------
from Configs.configs import client
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

async def mute_all(message, ids, session):
  guild = message.author.voice.channel.guild.id;
  got_guild = client.get_guild(guild);
  i_list=list(session.ids)
  print(i_list)
  for ids in i_list:  
    member = got_guild.get_member(ids);
    await mute_method(member);
    await deafen_method(member);
  return

async def unmute_all(message, ids, session):
  guild = message.author.voice.channel.guild.id;
  got_guild = client.get_guild(guild);
  i_list=list(session.ids)
  for ids in i_list:
    member = got_guild.get_member(ids);
    await unmute_method(member)
    await undeafen_method(member);
  return
#----------------------------------------
