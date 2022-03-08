#--------------------IMPORTs-----------------
import Configs.configs as cfg
from Pomodoro.Session_Handlers.get_session import get_session_pomojoin, OutsideVoiceChannel_pjoin, get_session
from Handle_Variables.handle_variables import get_ids
#--------------------------------------------

async def command_pomojoin(message, list_of_guilds:list):
  index = await get_session(message, cfg.session_guilds)
  session=cfg.session_guilds[index]
  if not hasattr(message.author.voice, 'channel'):
    raise OutsideVoiceChannel_pjoin(message)
  cur_vchan_session=await get_session_pomojoin(message, message.author.voice.channel, session)
  await get_ids(message, cur_vchan_session)
  return