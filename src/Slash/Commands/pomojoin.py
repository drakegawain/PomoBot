#--------------------IMPORTs-----------------
from ...Configs import configs as cfg
from ...Slash.Session_Handlers.get_session import get_session, get_session_pomojoin, OutsideVoiceChannel_pjoin
from ...Slash.Handle_Variables.handle_variables import get_ids
from ...Slash.Utilitys.fetch_informations import fetch
from ...Slash.Discord_Actions.Messages.security_messages import SecurityMessage
from ...cli.ppadron import prntpdr
import logging
import nextcord
#--------------------------------------------

async def command_pomojoin(ctx:nextcord.Interaction, logger:logging.Logger, SM:logging.Logger):
  response=fetch(ctx)
  author=response[1]
  guild=response[2]
  logger.warning("{} from:{} user:{}".format(__name__,guild.name, author.name))
  index = await get_session(guild, cfg.session_guilds)
  session=cfg.session_guilds[index]
  dictio_session=session.session
  if not hasattr(author.voice, 'channel'):
    raise OutsideVoiceChannel_pjoin(ctx)
  cur_vchan_session=await get_session_pomojoin(ctx, author.voice.channel, dictio_session)
  await get_ids(ctx, cur_vchan_session)
  return