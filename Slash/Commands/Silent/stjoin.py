import Configs.configs as cfg
from Slash.Session_Handlers.get_session import get_session
from Slash.Handle_Variables.handle_variables import get_ids
from Slash.Utilitys.fetch_informations import fetch
from Slash.Discord_Actions.Messages.security_messages import SecurityMessage

async def stjoin(ctx, logger):
  print("silent_pomojoin")
  N_M=SecurityMessage('/pomojoin', ctx, 1324675)
  await N_M.send(141)
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