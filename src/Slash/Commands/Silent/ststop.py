from src.Slash.Session_Handlers.get_session import get_session
from src.Slash.Utilitys.fetch_informations import fetch
import src.Configs.configs as cfg
async def ststop(ctx, logger):
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
  await ctx.send('stopped')
  logger.warning("{} stopped".format(guild.name))
  return