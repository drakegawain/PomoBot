#---------------BASIC-CONFIGs-------------------
import os
import nest_asyncio
#-----------------------------------------------
#-------------------IMPORTs---------------------
#imports from the project
#you can see more of the functions in the respective files
from Configs.configs import client
from Pomodoro.close import after_30_seconds_close_pomodoro
from Discord_Actions.mute_unmute import mute_all, unmute_all;
from Pomodoro.time_pomodoro import  handle_study_time, handle_rest_time, study_time, rest_time;
from Discord_Actions.users_members import avaiable_users_to_join;
from Pomodoro.utilitys import repeatedly_execution
from Discord_Actions.connect_disconnect import disconnect_from_voice_channel, connect_to_voice_channel
from Discord_Actions.Messages.messages import message_stopping_pomostop,message_avaiable_users_to_join, message_help
from Handle_Variables.handle_variables import get_ids, list_keys, bot_id, get_keys
from Discord_Actions.start import start_pomodoro, reset_func, startup_e
from Classes.when_class import when
#-----------------------------------------------
#------------------SETUPs-----------------------
nest_asyncio.apply()
import Configs.configs as cfg
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
    cfg.close = when()
    pomoclose = cfg.close

    pomoclose.set_functions(repeatedly_execution)
    pomoclose.set_args(cfg.study_time_global, cfg.rest_time_global, unmute_all, mute_all, message, cfg.ids)
    
    pomoclose.if_when('yes')

    await after_30_seconds_close_pomodoro(message);
    #-------------------------------------------
      
  if message.content.startswith('.pomojoin'):
    await get_ids(message)

  if message.content.startswith('.pomostop'):
    try:
      await unmute_all(message, cfg.ids)
      await disconnect_from_voice_channel()
    except:
      await message.channel.send('User <@{}> isnt in a voice channel.\nNo session started. See the documentation for more information ``.pomohelp``'.format(message.author.id))
    else:
      try:
        cfg.close.cancel()
      except:
        try:
          cfg.class_e.release_future()
          cfg.class_i.release_future()
          await message_stopping_pomostop(message)
        except:
          await message.channel.send('No session started. See the documentation for more information ``.pomohelp``')
      else:
        await message_stopping_pomostop(message)
      finally:
        await reset_func()
        await message.channel.send('Stopped')
#---------------------------------------------
#---------------LOGGIN-----------------
client.run(os.environ['TOKEN'])
#--------------------------------------