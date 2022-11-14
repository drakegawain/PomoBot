import src.Configs.configs as cfg
from src.Slash.Session_Handlers.get_session import get_session
from src.Slash.Handle_Variables.handle_variables import get_ids
from src.Slash.Utilitys.fetch_informations import fetch

async def stjoin(ctx, logger):
  response=fetch(ctx)
  author=response[1]
  guild=response[2]
  logger.warning("Guild {} user {} joined session".format(guild.name, author.name))
  index = await get_session(guild, cfg.session_guilds)
  session=cfg.session_guilds[index]
  dictio_session=session.session
  session=dictio_session["Main"]
  await get_ids(ctx, session)
  return