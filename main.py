#---------------BASIC-CONFIGs-------------------
import os
import nest_asyncio
#-----------------------------------------------
#-------------------IMPORTs---------------------
#imports from the project
#you can see more of the functions in the respective files
from configs import client
from close import after_30_seconds_close_pomodoro
from mute_unmute import mute_all, unmute_all;
from time_pomodoro import  handle_study_time, handle_rest_time, study_time, rest_time;
from users_members import avaiable_users_to_join;
from utilitys import repeatedly_execution
from connect_disconnect import disconnect_from_voice_channel
from messages import message_error_pomostop
from handle_variables import get_ids
from handle_variables import list_keys, bot_id, get_keys
from start import start_pomodoro
from messages import message_avaiable_users_to_join
from start import startup_e;
from connect_disconnect import connect_to_voice_channel
#-----------------------------------------------
#------------------SETUPs-----------------------
nest_asyncio.apply()
import configs as cfg
#-----------------------------------------------
#------------------HOW-MANY-SVs-----------------
#-----------------------------------------------
#-------------------EVENTs----------------------
@client.event
async def on_ready():
  pass

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.pomohelp'):
    from messages import message_help
    await message_help(message)
    return

  if message.content.startswith('.pomodoro'):
    
    #---------------START-UP---------------------
    await connect_to_voice_channel(message);
    await startup_e() #reset the variables
    #-------------------------------------------
    #---------------TIME VARIABLES--------------
    cfg.study_time_global = await handle_study_time(await study_time(message));
    cfg.rest_time_global = await handle_rest_time(await rest_time(message));
    #-------------------------------------------
    #----------------OPEN-CLOCK-----------------
    await start_pomodoro();
    
    await message_avaiable_users_to_join(message, await avaiable_users_to_join(await list_keys(await get_keys(message)), await bot_id()));
    #-------------------------------------------
    #---------------CLOSE-----------------------
    pomoclose = cfg.close

    pomoclose.set_functions(repeatedly_execution)
    pomoclose.set_args(cfg.study_time_global, cfg.rest_time_global, unmute_all, mute_all, message, cfg.ids)
    
    pomoclose.if_when('yes')

    await after_30_seconds_close_pomodoro(message);
    #-------------------------------------------
      
  if message.content.startswith('.pomojoin'):
    await get_ids(message)

  if message.content.startswith('.pomostop'):
    await unmute_all(message, cfg.ids)
    await disconnect_from_voice_channel()
    try:
      cfg.close.cancel()
    except:
      await message_error_pomostop(message)
      cfg.class_e.release_future()
      cfg.class_i.release_future()
    finally:
      await message.channel.send('Stopped')
#---------------------------------------------
#---------------LOGGIN-----------------
client.run(os.environ['TOKEN'])
#--------------------------------------