import logging
import nextcord
from ....Slash.Session_Handlers.get_session import get_session
from ....Slash.Utilitys.fetch_informations import fetch
from ....Configs import configs as cfg

async def ststop(ctx:nextcord.Interaction, logger:logging.Logger, embed:nextcord.Embed):
  response=fetch(ctx)
  guild=response[2]
  index=await get_session(guild, cfg.session_guilds)
  session_class=cfg.session_guilds[index]
  dictio_session=session_class.session
  session=dictio_session["Main"]
  session.class_i.release_future()
  try:
    session.close.cancel()
  except:
    logger.warning("Exception in session.close.cancel")
    pass
  session.restart()
  await ctx.send('stopped', embed=embed)
  logger.warning("{} stopped".format(guild.name))
  return