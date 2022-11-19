#---------------IMPORTs----------
from ...Configs.configs import client
from ...Configs import configs as cfg
from ...Slash.Utilitys.fetch_informations import fetch
#-------------------------------
#------------MUTE-UNMUTE-METHODs---------
async def mute_method(member):
  await member.edit(mute=True)
  return

async def deafen_method(member):
  await member.edit(deafen=True)
  return

async def unmute_method(member):
  await member.edit(mute=False)
  return

async def undeafen_method(member):
  await member.edit(deafen=False)
  return

async def mute_all(ctx, ids, session, logger):
  response = fetch(ctx)
  guild = response[2].id
  got_guild = client.get_guild(guild)
  i_list = list(session.ids)
  logger.warning("muting:{}".format(i_list))
  for ids in i_list:  
    member = await got_guild.fetch_member(ids)
    await mute_method(member)
    await deafen_method(member)
  return

async def unmute_all(ctx, ids, session, logger):
  response = fetch(ctx)
  guild = response[2].id
  got_guild = client.get_guild(guild)
  i_list=list(session.ids)
  logger.warning("unmuting:{}".format(i_list))
  for ids in i_list:
    member = await got_guild.fetch_member(ids)
    await unmute_method(member)
    await undeafen_method(member)
  return
#----------------------------------------
