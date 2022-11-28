#---------------------IMPORTs------------------
import logging
import nextcord
from ...Configs import configs as cfg
from ...Slash.Session_Handlers.get_session import get_session_ps
from ...Slash.Security.Command_Check.pomostop_check import check_pomostop
from ...Slash.Session_Handlers.del_session import delete
from ...Slash.Discord_Actions.connect_disconnect import disconnect_from_voice_channel
from ...Slash.Session_Handlers.handle_session import session_handler
from ...Slash.Discord_Actions.mute_unmute import unmute_all
from ...Slash.Session_Handlers.get_session import get_session, OutsideVoiceChannel
from ...Slash.Utilitys.fetch_informations import fetch
#---------------------------------------------
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