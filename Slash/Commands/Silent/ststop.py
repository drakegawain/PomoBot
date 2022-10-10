from Slash.Session_Handlers.get_session import get_session
from Slash.Utilitys.fetch_informations import fetch
import Configs.configs as cfg
async def ststop(ctx):
  response=fetch(ctx)
  guild=response[2]
  index=await get_session(guild, cfg.session_guilds)
  session_class=cfg.session_guilds[index]
  dictio_session=session_class.session
  session=dictio_session["Main"]
  session.close.cancel()
  session.class_i.release_future()
  session.restart()
  await ctx.send('stopped')
  return