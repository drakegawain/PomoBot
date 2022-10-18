#--------------------IMPORTs-----------------
import Configs.configs as cfg
from Slash.Session_Handlers.get_session import get_session, get_session_pomojoin, OutsideVoiceChannel_pjoin
from Slash.Handle_Variables.handle_variables import get_ids
from Cli_Commands.Print_Padronization.ppadron import prntpdr
from Slash.Utilitys.fetch_informations import fetch
from Slash.Discord_Actions.Messages.security_messages import SecurityMessage
#--------------------------------------------

async def command_pomojoin(ctx):
  print("command_pomojoin")
  N_M=SecurityMessage('/pomojoin', ctx, 1324675)
  await N_M.send(141)
  response=fetch(ctx)
  author=response[1]
  guild=response[2]
  prntpdr(cfg.black, "raising command_pomojoin from:{} user:{}".format(guild.name, author.name))
  index = await get_session(guild, cfg.session_guilds)
  session=cfg.session_guilds[index]
  dictio_session=session.session
  if not hasattr(author.voice, 'channel'):
    raise OutsideVoiceChannel_pjoin(ctx)
  cur_vchan_session=await get_session_pomojoin(ctx, author.voice.channel, dictio_session)
  await get_ids(ctx, cur_vchan_session)
  return