#---------------------IMPORTs------------------
import Configs.configs as cfg
import asyncio
from Pomodoro.Session_Handlers.get_session import get_session_ps, get_session
from Pomodoro.Session_Handlers.del_session import delete
from Discord_Actions.connect_disconnect import disconnect_from_voice_channel
from Pomodoro.Session_Handlers.handle_session import session_handler
from Discord_Actions.mute_unmute import unmute_all
from Cli_Commands.Print_Padronization.ppadron import prntpdr
#---------------------------------------------

class Error(Exception):
  '''Base error class'''

class LeftVC(Error):
    def __init__(self, message, dictio_session):
      loop=asyncio.get_event_loop()
      dictio_session["Main"].class_e.release_future()
      dictio_session["Main"].class_i.release_future()
      dictio_session["Main"].clear()
      dictio_session["Main"].restart()
      loop.run_until_complete(disconnect_from_voice_channel(message))
      prntpdr(cfg.red, "raising LeftVoiceChannel:{}".format(message.guild.name))
      return

async def admin_pomostop(message):
    index=await get_session(message, cfg.session_guilds)
    session_class=cfg.session_guilds[index]
    dictio_session=session_class.session
    if not hasattr(message.author.voice, "channel"):
      raise LeftVC(message, dictio_session)
      return
    cur_vchan_session=await get_session_ps(message, message.author.voice.channel, dictio_session)
    session=await session_handler(dictio_session, cur_vchan_session)
    value_session=dictio_session.get(session) # VALUE_SESSION IS THE CURRENT SESSION RUNNING IN THE VC
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
                      await unmute_all(message, value_session.ids, value_session)
                      value_session.restart()
                  else:
                      await unmute_all(message, value_session.ids, value_session)
                      await delete(dictio_session, session)
          except:
                  prntpdr(cfg.red, "error in pomostop: couldnt verify Main session")
          finally:
              value_session.restart()
              await disconnect_from_voice_channel(message)
              await message.channel.send('stopped')
              return