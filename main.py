#---------------BASIC-CONFIGs-------------------
import os
import nest_asyncio
import sys
#-----------------------------------------------
#-------------------IMPORTs---------------------
#imports from the project
#you can see more of the functions in the respective files
from Configs.configs import client
from Pomodoro.close import after_30_seconds_close_pomodoro
from Pomodoro.utilitys import exec_mute_all, exec_unmute_all
from Pomodoro.time_pomodoro import  handle_study_time, handle_rest_time, study_time, rest_time;
from Discord_Actions.users_members import avaiable_users_to_join;
from Pomodoro.utilitys import repeatedly_execution
from Discord_Actions.connect_disconnect import disconnect_from_voice_channel, connect_to_voice_channel
from Discord_Actions.Messages.messages import message_stopping_pomostop,message_avaiable_users_to_join, message_help
from Handle_Variables.handle_variables import get_ids, list_keys, bot_id, get_keys
from Discord_Actions.start import start_pomodoro, reset_func, startup_e, start_session
from Classes.when_class import when
from Security.Command_Check.pomostop_check import check_pomostop
from Discord_Actions.mute_unmute import unmute_all
from Security.Session_Check.check_for_double_sessions import c_for_doubles
from Security.Command_Check.pomodoro_check import check_pomodoro

#-----------------------------------------------
#------------------SETUPs-----------------------
nest_asyncio.apply()
os.system('clear')
import Configs.configs as cfg
from replit import db
#-----------------------------------------------
#-------------------EVENTs----------------------
@client.event
async def on_ready():
  db["{command}_{bad_access}".format(command='pomodoro', bad_access='271')] = "{reason}".format(reason='Only one session can exist per v_channel at the same time')
  pass

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.pomohelp'):
    await message_help(message)
    return

  if message.content.startswith('.pomodoro'):
    try:
      doubles=await c_for_doubles(cfg.session, message.author.id, message)
      if doubles is True:
        raise Exception
    except:
      print("ERROR POMODORO 201: USER ALREADY IN A SESSION")
    else:
    #---------------Check------------------------
      try:
        voice_channel_check=await check_pomodoro(message.author.voice.channel,cfg.session, message)
        if voice_channel_check is True:
          raise Exception
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
      
  if message.content.startswith('.pomojoin'):
    await get_ids(message, session)

  if message.content.startswith('.pomotest'):
    try:
      print('pass')
      await check_pomostop(message.author.id, message)
    except TypeError:
      print('Erou')
  if message.content.startswith('.pomostop'):
    session=cfg.session.get('{}'.format('Session1'))
    
    # try:
    #   security_test=await check_pomostop(message.author.id, message)
    #   if security_test is False:
    #     raise Exception('User outside session')
    # except:
    #   print('Error in pomostop')
    # else:
    #   try:
    #     await unmute_all(message, session.ids)
    #     await disconnect_from_voice_channel()
    #   except:
    #     await message.channel.send('User <@{}> isnt in voice channel.\nNo session started. See the documentation for more information ``.pomohelp``'.format(message.author.id))
    #   else:
    #     try:
    #       session.close.cancel()
    #     except:
    #       try:
    #         session.class_e.release_future()
    #         session.class_i.release_future()
    #         await message_stopping_pomostop(message)
    #       except:
    #         await message.channel.send('No session started. See the documentation for more information ``.pomohelp``')
    #     else:
    #       await message_stopping_pomostop(message)
    #     finally:
    #       await disconnect_from_voice_channel()
    #       await reset_func()
    #       await message.channel.send('Stopped')
        
#---------------------------------------------
#---------------LOGGIN-----------------
client.run(os.environ['TOKEN'])
#--------------------------------------