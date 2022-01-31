#------------IMPORTs---------------
import Configs.configs as cfg
from Security.Session_Check.check_for_double_sessions import c_for_doubles
from Security.Command_Check.pomodoro_check import check_pomodoro
from Discord_Actions.connect_disconnect import connect_to_voice_channel
from Discord_Actions.start import start_session
from Pomodoro.time_pomodoro import study_time, rest_time,handle_study_time, handle_rest_time
from Handle_Variables.handle_variables import list_keys, get_keys, bot_id
from Discord_Actions.start import start_pomodoro
from Discord_Actions.Messages.messages import message_avaiable_users_to_join
from Discord_Actions.users_members import avaiable_users_to_join
from Classes.when_class import when
from Pomodoro.utilitys import repeatedly_execution, exec_unmute_all, exec_mute_all
from Pomodoro.close import after_30_seconds_close_pomodoro
#----------------------------------

async def command_pomodoro(message):
  try:
      doubles=await c_for_doubles(cfg.session, message.author.id, message)
      if doubles is True:
        raise Exception
  except:
      print("ERROR POMODORO 201: USER ALREADY IN A SESSION")
  else:
    #---------------Check------------------------
      try:
        if hasattr(message, 'author.voice.channel'):
          voice_channel_check=await check_pomodoro(message.author.voice.channel,cfg.session,message)
          if voice_channel_check is True:
            raise Exception
        else:
          pass
      except:
        print("ERROR POMODORO 271: ONLY ONE SESSION PER VC")
      else:
    #--------------------------------------------
    #---------------START-UP---------------------
        session = await start_session(message)
        await connect_to_voice_channel(message, session);
    #-------------------------------------------
    #---------------TIME VARIABLEs--------------
        session.study_time_global = await handle_study_time(await study_time(message));
        session.rest_time_global = await handle_rest_time(await rest_time(message));
    #-------------------------------------------
    #----------------OPEN-CLOCK-----------------
        await start_pomodoro(session);
    
        await message_avaiable_users_to_join(message, await avaiable_users_to_join(await list_keys(await get_keys(message)), await bot_id()));
    #-------------------------------------------
    #---------------CLOSE-----------------------
        session.close=when()
        pomoclose=session.close
    

        pomoclose.set_functions(repeatedly_execution)
        pomoclose.set_args(session, session.study_time_global, session.rest_time_global, exec_unmute_all, exec_mute_all, message, session.ids, session)
    
        pomoclose.if_when('yes')

        await after_30_seconds_close_pomodoro(message, session);
    #-------------------------------------------
  return