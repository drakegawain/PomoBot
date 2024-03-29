import Configs.configs as cfg
from Classes.when_class import when
from Slash.Security.Session_Check.check_for_double_sessions import c_for_doubles
from Slash.Discord_Actions.start import start_session
from Slash.Discord_Actions.start import start_pomodoro
from Slash.Discord_Actions.Messages.messages import msg_slnt
from Slash.Pomodoro.utilitys import srest, sstdy
from Slash.Pomodoro.utilitys import repeatedly_execution
from Slash.Pomodoro.close import sec30close
from Slash.Session_Handlers.get_session import get_session
from Slash.Utilitys.fetch_informations import fetch

async def stpomo(ctx, study_time, rest_time, logger):
  response = fetch(ctx)
  guild = response[2]
  author = response[1]
  index = await get_session(guild, cfg.session_guilds)
  session_class = cfg.session_guilds[index]
  dictio_session = session_class.session
  session_status = dictio_session['Main']
  session_status = await session_status.get('STATUS')
  if session_status is not None:
    await ctx.send('Only one session per guild is allowed in this version.')
    raise Exception
  try:
      doubles = await c_for_doubles(dictio_session, author.id, ctx)
      if doubles is True:
        raise Exception
  except:
      logger.warning("{} double session error".format(guild.name))
  session = await start_session(ctx)
  session_status = 'Running'
  await session.set_status(session_status)
  session.study_time_global=study_time
  session.rest_time_global=rest_time
  session.silent=True
  await start_pomodoro(session);
  await msg_slnt(ctx)
  session.close=when()
  pomoclose=session.close
  pomoclose.set_functions(repeatedly_execution)
  pomoclose.set_args(session.study_time_global, session.rest_time_global, srest, sstdy, ctx, session)
  pomoclose.if_when('yes')
  await sec30close(ctx, session, logger)
  return