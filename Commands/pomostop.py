#---------------------IMPORTs------------------
import Configs.configs as cfg
from Pomodoro.Session_Handlers.get_session import get_session_ps
from Security.Command_Check.pomostop_check import check_pomostop
from Pomodoro.Session_Handlers.del_session import delete
from Discord_Actions.connect_disconnect import disconnect_from_voice_channel
from Pomodoro.Session_Handlers.handle_session import session_handler
from Discord_Actions.mute_unmute import unmute_all
from Pomodoro.Session_Handlers.get_session import OutsideVoiceChannel, get_session
#---------------------------------------------
async def command_pomostop(message):
    index=await get_session(message, cfg.session_guilds)
    session_class=cfg.session_guilds[index]
    dictio_session=session_class.session
    if not hasattr(message.author.voice, "channel"):
      raise OutsideVoiceChannel(message)
    cur_vchan_session=await get_session_ps(message, message.author.voice.channel, dictio_session)
    session=await session_handler(dictio_session, cur_vchan_session)
    value_session=dictio_session.get(session) # VALUE_SESSION IS THE CURRENT SESSION RUNNING IN THE VC
    try:
        TRUE_OR_FALSE=await check_pomostop(message.author.id, message, value_session)
        if TRUE_OR_FALSE is False:
            raise Exception
    except:
        await message.channel.send('@{} To call pomostop you have to be inside the running session.'.format(message.author.id))
        print('@line 26 ERROR IN: .pomostop')
    else:
        try:
            value_session.close.cancel()
        except:
              print('{} ERROR in : .pomostop.else.except'.format('@Commands/pomostop:line->26'))
              print('releasing futures')
              value_session.class_e.release_future()
              value_session.class_i.release_future()
              print('futures released')
              try:
                      try:
                        F_OR_T_VARIABLE=session
                        print('FALSEORTRUE:{}'.format(F_OR_T_VARIABLE))
                      except:
                        raise Exception
                      if F_OR_T_VARIABLE == "Main":
                          await unmute_all(message, value_session.ids, value_session)
                          value_session.restart()
                      else:
                          await unmute_all(message, value_session.ids, value_session)
                          await delete(dictio_session, session)
              except:
                      print('FALSEORTRUE:{}'.format(F_OR_T_VARIABLE))
                      print(value_session)
                      print('{} ERROR in : .pomostop.else.except.try'.format('@Commands/pomostop:line->47'))
              finally:
                      return
        else:
          F_or_T=session
          if F_or_T == "Main":
            await unmute_all(message, value_session.ids, value_session)
            value_session.restart()
          else:
             await unmute_all(message, value_session.ids, value_session)
             await delete(dictio_session, session)
        finally:
          value_session.restart()
          await disconnect_from_voice_channel(message)
          await message.channel.send('stopped')
          return