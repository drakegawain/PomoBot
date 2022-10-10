#---------------------IMPORTs------------------
import Configs.configs as cfg
from Slash.Session_Handlers.get_session import get_session_ps
from Slash.Security.Command_Check.pomostop_check import check_pomostop
from Pomodoro.Session_Handlers.del_session import delete
from Slash.Discord_Actions.connect_disconnect import disconnect_from_voice_channel
from Pomodoro.Session_Handlers.handle_session import session_handler
from Slash.Discord_Actions.mute_unmute import unmute_all
from Slash.Session_Handlers.get_session import get_session, OutsideVoiceChannel
from Cli_Commands.Print_Padronization.ppadron import prntpdr
from Slash.Utilitys.fetch_informations import fetch
#---------------------------------------------
async def command_pomostop(ctx):
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
        await ctx.send('<@{}> To call pomostop you have to be inside the running session.'.format(author.id))
        prntpdr(cfg.red, ".pomostop error @check_pomostop")()
    else:
        try:
            value_session.close.cancel()
        except:
              prntpdr(cfg.red, "error in pomostop: couldnt verify value_session.close.cancel")
              prntpdr(cfg.black, "releasing futures")
              value_session.class_e.release_future()
              value_session.class_i.release_future()
              prntpdr(cfg.green, "futures released")
              try:
                      try:
                        F_OR_T_VARIABLE=session
                      except:
                        raise Exception
                      if F_OR_T_VARIABLE == "Main":
                          await unmute_all(ctx, value_session.ids, value_session)
                          value_session.restart()
                      else:
                          await unmute_all(ctx, value_session.ids, value_session)
                          await delete(dictio_session, session)
              except:
                      prntpdr(cfg.red, "error in pomostop: couldnt verify Main session")
              finally:
                      return
        else:
          F_or_T=session
          if F_or_T == "Main":
            await unmute_all(ctx, value_session.ids, value_session)
            value_session.restart()
          else:
             await unmute_all(ctx, value_session.ids, value_session)
             await delete(dictio_session, session)
        finally:
          value_session.restart()
          await disconnect_from_voice_channel(ctx)
          await ctx.send('stopped')
          return