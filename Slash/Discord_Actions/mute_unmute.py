#---------------IMPORTs----------
from Configs.configs import client
from Cli_Commands.Print_Padronization.ppadron import prntpdr
import Configs.configs as cfg
from Discord_Actions.mute_unmute import mute_method, deafen_method, unmute_method, undeafen_method
from Slash.Utilitys.fetch_informations import fetch
#-------------------------------
#------------MUTE-UNMUTE-METHODs---------

async def mute_all(ctx, ids, session):
  response=fetch(ctx)
  guild=response[2].id
  got_guild = client.get_guild(guild);
  i_list=list(session.ids)
  prntpdr(cfg.blue, "muting:{}".format(i_list))
  for ids in i_list:  
    member = got_guild.get_member(ids);
    await mute_method(member);
    await deafen_method(member);
  return

async def unmute_all(ctx, ids, session):
  response=fetch(ctx)
  guild=response[2].id
  got_guild=client.get_guild(guild);
  i_list=list(session.ids)
  prntpdr(cfg.blue, "unmuting:{}".format(i_list))
  for ids in i_list:
    member=got_guild.get_member(ids);
    await unmute_method(member)
    await undeafen_method(member);
  return
#----------------------------------------
