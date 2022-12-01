#------------IMPORTs---------------
import logging
import nextcord
import asyncio
from .classes import When
from ..Configs import configs as cfg
from ..Configs.loops import loopClient
from ..Slash.Session_Handlers.get_session import get_session, get_session_pomojoin, get_session_ps, OutsideVoiceChannel_pjoin, OutsideVoiceChannel
from ..Slash.Utilitys.fetch_informations import fetch
from ..Slash.Security.Command_Check.pomodoro_check import check_pomodoro
from ..Slash.Security.Command_Check.pomostop_check import check_pomostop
from ..Slash.Discord_Actions.connect_disconnect import connect_to_voice_channel, disconnect_from_voice_channel
from ..Slash.Handle_Variables.handle_variables import list_keys, get_keys, bot_id, get_ids
from ..Slash.Discord_Actions.Messages.messages import message_avaiable_users_to_join, msg_slnt
from ..Slash.Discord_Actions.user_members import avaiable_users_to_join

from ..Slash.Pomodoro.utilitys import exec_unmute_all, exec_mute_all, repeatedly_execution_with_sounds, repeatedly_execution, srest, sstdy
from ..Slash.Pomodoro.close import after_30_seconds_close_pomodoro, sec30close
from ..Slash.Session_Handlers.del_session import delete
from ..Slash.Session_Handlers.handle_session import session_handler
from ..Slash.Discord_Actions.mute_unmute import unmute_all
from ..Slash.Security.Session_Check.check_for_double_sessions import c_for_doubles
from ..Slash.Discord_Actions.start import start_session, start_pomodoro
#----------------------------------
async def command_pomodoro(ctx:nextcord.Interaction, study_time, rest_time, SM:logging.Logger, logger:logging.Logger, embed:nextcord.Embed):
  #---GETtING_INFOS--
  response = fetch(ctx)
  guild = response[2]
  author = response[1]
  index = await get_session(guild, cfg.session_guilds)
  logger.warning("{} id:{}".format(__name__, index))
  session_class = cfg.session_guilds[index]
  dictio_session = session_class.session
  #---CHECKING-STATUS-OF-CURRENT-SESSION-MAIN--
  session_status=dictio_session['Main']
  session_status=await session_status.get('STATUS')
  logger.warning("{} {} status:{}".format(__name__, guild.name, session_status))
  if session_status is not None:
    message = 'Only one session per guild is allowed in this version. We are working to improve! If you are a developer and want to help, checkout our github page! https://github.com/drakegawain/PomoBot'
    embed.add_field(name = "Error", value=message)
    await ctx.send(embed)
    raise Exception
  try:
      doubles=await c_for_doubles(dictio_session, author.id, ctx)
      if doubles is True:
        raise Exception
  except:
      SM.error("{} 201 user already in a session").format(guild.name)
  else:
    #---------------Check------------------------
      try:
        if hasattr(author, "voice.channel"):
          voice_channel_check=await check_pomodoro(author.voice.channel,dictio_session,ctx)
          if voice_channel_check:
            raise Exception
        else:
          pass
      except:
        SM.error("{} 271 only one session per guild").format(guild.name)
      else:
    #--------------------------------------------
    #---------------START-UP---------------------
        session=await start_session(ctx, logger)
        session_status='Running'
        await session.set_status(session_status)
        asyncio.run_coroutine_threadsafe(connect_to_voice_channel(ctx, session), loop=loopClient) 
    #-------------------------------------------
    #---------------TIME VARIABLEs--------------
        session.silent=False
        session.study_time_global=study_time
        session.rest_time_global=rest_time
    #-------------------------------------------
    #----------------OPEN-CLOCK-----------------
        await start_pomodoro(session)
        await message_avaiable_users_to_join(ctx, await avaiable_users_to_join(await list_keys(await get_keys(ctx)), await bot_id()), embed)
    #-------------------------------------------
    #---------------CLOSE-----------------------
        try:
          session.close=When()
          pomoclose=session.close
          pomoclose.set_functions(repeatedly_execution_with_sounds)
          pomoclose.set_args(
            session, session.study_time_global, session.rest_time_global, exec_unmute_all, exec_mute_all, 
            ctx, session.ids, session, logger, embed
            )
          pomoclose.if_when('yes')
          await after_30_seconds_close_pomodoro(ctx, session, logger)
        except:
          raise Exception
    #-------------------------------------------
  return

async def command_pomojoin(ctx:nextcord.Interaction, logger:logging.Logger, SM:logging.Logger, embed:nextcord.Embed):
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

async def command_pomostop(ctx:nextcord.Interaction, SM:logging.Logger, embed = nextcord.Embed):
    response=fetch(ctx)
    guild=response[2]
    author=response[1]
    index=await get_session(guild, cfg.session_guilds)
    session_class=cfg.session_guilds[index]
    dictio_session=session_class.session
    if not hasattr(author.voice, "channel"):
      raise OutsideVoiceChannel(ctx)
    cur_vchan_session=await get_session_ps(ctx, author.voice.channel, dictio_session)
    session=await session_handler(dictio_session, cur_vchan_session)
    value_session=dictio_session.get(session) 
    try:
        TRUE_OR_FALSE=await check_pomostop(author.id, ctx, value_session)
        if TRUE_OR_FALSE is False:
            raise Exception
    except:
        await ctx.send('<@{}> To call pomostop you have to be inside the running session.'.format(author.id), embed=embed)
        SM.error("{} {} user outside voice_channel".format(__name__, guild.name))
    else:
        try:
            value_session.close.cancel()
        except:
              SM.error("{} {} could not verify value_session.close.cancel -> releasing futures".format(__name__, guild.name))
              value_session.class_e.release_future()
              value_session.class_i.release_future()
              try:
                      try:
                        F_OR_T_VARIABLE=session
                      except:
                        raise Exception
                      if F_OR_T_VARIABLE == "Main":
                          await unmute_all(ctx, value_session.ids, value_session, SM)
                          value_session.restart()
                      else:
                          await unmute_all(ctx, value_session.ids, value_session, SM)
                          await delete(dictio_session, session)
              except:
                      SM.error("{} {} could not verify main session".format(__name__, guild.name))
              finally:
                      return
        else:
          F_or_T=session
          if F_or_T == "Main":
            await unmute_all(ctx, value_session.ids, value_session, SM)
            value_session.restart()
          else:
             await unmute_all(ctx, value_session.ids, value_session, SM)
             await delete(dictio_session, session)
        finally:
          value_session.restart()
          await disconnect_from_voice_channel(ctx)
          await ctx.send('stopped', embed=embed)
          return

async def silentJoin(ctx:nextcord.Interaction, logger:logging.Logger):
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

async def silentpomo(ctx:nextcord.Interaction, study_time:int, rest_time:int, logger:logging.Logger, embed:nextcord.Embed):
  response = fetch(ctx)
  guild = response[2]
  author = response[1]
  index = await get_session(guild, cfg.session_guilds)
  session_class = cfg.session_guilds[index]
  dictio_session = session_class.session
  session_status = dictio_session['Main']
  session_status = await session_status.get('STATUS')
  if session_status is not None:
    await ctx.send('Only one session per guild is allowed in this version.', embed=embed)
    raise Exception
  try:
      doubles = await c_for_doubles(dictio_session, author.id, ctx)
      if doubles is True:
        raise Exception
  except:
      logger.warning("{} double session error".format(guild.name))
  session = await start_session(ctx, logger)
  session_status = 'Running'
  await session.set_status(session_status)
  session.study_time_global=study_time
  session.rest_time_global=rest_time
  session.silent=True
  await start_pomodoro(session)
  await msg_slnt(ctx, embed)
  session.close=When()
  pomoclose=session.close
  pomoclose.set_functions(repeatedly_execution)
  pomoclose.set_args(session.study_time_global, session.rest_time_global, srest, sstdy, ctx, session)
  pomoclose.if_when('yes')
  await sec30close(ctx, session, logger)
  return

async def silentstop(ctx:nextcord.Interaction, logger:logging.Logger, embed:nextcord.Embed):
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

async def stop(ctx:nextcord.Interaction, SM):
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(command_pomostop(ctx, SM))
    return