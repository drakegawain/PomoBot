#--------------------IMPORTs-----------------
import Configs.configs as cfg
from Pomodoro.Session_Handlers.get_session import get_session_pomojoin, OutsideVoiceChannel_pjoin
from Handle_Variables.handle_variables import get_ids
#--------------------------------------------

async def command_pomojoin(message):
  if not hasattr(message.author.voice, 'channel'):
    raise OutsideVoiceChannel_pjoin(message)
  cur_vchan_session=await get_session_pomojoin(message, message.author.voice.channel, cfg.session)
  await get_ids(message, cur_vchan_session)
  return