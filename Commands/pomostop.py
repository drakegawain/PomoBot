#---------------------IMPORTs------------------
import Configs.configs as cfg
from Pomodoro.Session_Handlers.get_session import get_session_ps
from Security.Command_Check.pomostop_check import check_pomostop
from Pomodoro.Session_Handlers.check_session import ch_session
from Pomodoro.Session_Handlers.del_session import delete
from Discord_Actions.connect_disconnect import disconnect_from_voice_channel
from Pomodoro.Session_Handlers.handle_session import session_handler
#----------------------------------------------
async def command_pomostop(message):
    cur_vchan_session=await get_session_ps(message, message.author.voice.channel, cfg.session)
    try:
        TRUE_OR_FALSE=await check_pomostop(message.author.id, message, cur_vchan_session)
        if TRUE_OR_FALSE is False:
            raise Exception
    except:
        print('ERROR IN: .pomostop')
    else:
        try:
            cur_vchan_session.close.cancel()
        except:
              print('ERROR in : .pomostop.else.except')
              print('cur_vchan_session:{}'.format(cur_vchan_session))
              print('cur_vchan_session.class_e:{}'.format(cur_vchan_session.class_e))
              print('releasing futures')
              cur_vchan_session.class_e.release_future()
              cur_vchan_session.class_i.release_future()
              print('futures released')
              try:
                      print('getting in try')
                      try:
                        F_OR_T_VARIABLE=await ch_session(cfg.session, cur_vchan_session)
                        print('FALSEORTRUE:{}'.format(F_OR_T_VARIABLE))
                      except:
                        raise Exception
                      if F_OR_T_VARIABLE is True:
                          cur_vchan_session.restart()
                      if F_OR_T_VARIABLE is False:
                          await delete(cfg.session, cur_vchan_session)
              except:
                      print('FALSEORTRUE:{}'.format(F_OR_T_VARIABLE))
                      print(cur_vchan_session)
                      print('ERROR IN: .pomostop.else.except.try')
              finally:
                      await disconnect_from_voice_channel()
                      await message.channel.send('stopped')
                      return
        else:
          F_or_T=await ch_session(cfg.session, cur_vchan_session)
          if F_or_T is True:
            cur_vchan_session.restart()
          if F_or_T is False:
             await delete(cfg.session, cur_vchan_session)
        finally:
          await disconnect_from_voice_channel()
          await message.channel.send('stopped')
          return