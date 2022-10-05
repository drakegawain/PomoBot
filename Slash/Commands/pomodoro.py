#------------IMPORTs---------------
import Configs.configs as cfg
from Slash.Security.Session_Check.check_for_double_sessions import c_for_doubles
from Slash.Security.Command_Check.pomodoro_check import check_pomodoro
from Slash.Discord_Actions.connect_disconnect import connect_to_voice_channel
from Slash.Discord_Actions.start import start_session
#from Pomodoro.time_pomodoro import study_time, rest_time,handle_study_time, handle_rest_time
from Slash.Handle_Variables.handle_variables import list_keys, get_keys, bot_id
from Slash.Discord_Actions.start import start_pomodoro
from Slash.Discord_Actions.Messages.messages import message_avaiable_users_to_join
from Discord_Actions.users_members import avaiable_users_to_join
from Classes.when_class import when
from Slash.Pomodoro.utilitys import exec_unmute_all, exec_mute_all
from Pomodoro.utilitys import repeatedly_execution
from Slash.Pomodoro.close import after_30_seconds_close_pomodoro
from Slash.Session_Handlers.get_session import get_session
from Cli_Commands.Print_Padronization.ppadron import prntpdr
from Slash.Utilitys.fetch_informations import fetch
#----------------------------------

async def command_pomodoro(ctx, study_time, rest_time):
  #---GETtING_INFOS--
  response=fetch(ctx)
  guild=response[2]
  author=response[1]
  index=await get_session(guild, cfg.session_guilds)
  prntpdr(cfg.yellow, ("id:{}".format(index)))
  session_class=cfg.session_guilds[index]
  dictio_session=session_class.session
  #---CHECKING-STATUS-OF-CURRENT-SESSION-MAIN--
  session_status=dictio_session['Main']
  session_status=await session_status.get('STATUS')
  prntpdr(cfg.black, "status:{}".format(session_status))
  if session_status is not None:
    await ctx.send('Only one session per guild is allowed in this version. We are working to improve! If you are a developer and want to help, checkout our github page! https://github.com/drakegawain/PomoBot')
    raise Exception
  #session_guild=await get_session(message, cfg.session_guilds)
  #print(session_guild)
  try:
      doubles=await c_for_doubles(dictio_session, author.id, ctx)
      if doubles is True:
        raise Exception
  except:
      prntpdr(cfg.red, "ERROR POMODORO 201: USER ALREADY IN A SESSION")
  else:
    #---------------Check------------------------
      try:
        if hasattr(author, 'voice.channel'):
          voice_channel_check=await check_pomodoro(author.voice.channel,dictio_session,ctx)
          if voice_channel_check is True:
            raise Exception
        else:
          pass
      except:
        prntpdr(cfg.red, "ERROR POMODORO 271: ONLY ONE SESSION PER VC")
      else:
    #--------------------------------------------
    #---------------START-UP---------------------
        session=await start_session(ctx)
        prntpdr(cfg.green, "starting command_pomodoro's session")
        session_status='Running'
        await session.set_status(session_status)
        prntpdr(cfg.green, "session status set to {}".format(session_status))
        await connect_to_voice_channel(ctx, session)
    #-------------------------------------------
    #---------------TIME VARIABLEs--------------
        session.study_time_global=study_time
        session.rest_time_global=rest_time
    #-------------------------------------------
    #----------------OPEN-CLOCK-----------------
        await start_pomodoro(session);
        await message_avaiable_users_to_join(ctx, await avaiable_users_to_join(await list_keys(await get_keys(ctx)), await bot_id()));
    #-------------------------------------------
    #---------------CLOSE-----------------------
        session.close=when()
        pomoclose=session.close
        pomoclose.set_functions(repeatedly_execution)
        pomoclose.set_args(session, session.study_time_global, session.rest_time_global, exec_unmute_all, exec_mute_all, ctx, session.ids, session)
        pomoclose.if_when('yes')
        await after_30_seconds_close_pomodoro(ctx, session);
    #-------------------------------------------
  return