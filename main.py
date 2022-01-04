import os
import nest_asyncio


from configs import client
from close import after_30_seconds_close_pomodoro
from mute_unmute import mute_all, unmute_all;
from time_pomodoro import  handle_study_time, handle_rest_time, study_time, rest_time;
from users_members import avaiable_users_to_join;
from utilitys import repeatedly_execution


#------------------Setups----------------------
nest_asyncio.apply()
import configs as cfg
#-------------------EVENTS--------------------

@client.event
async def on_ready():
  print('Logged in as {0.user}' .format(client))

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.help'):
    from messages import message_help
    await message_help(message)
    return

  if message.content.startswith('.pomodoro'):
    
    #---------------STARTUP--------------------
    from start import startup_e;
    from connect_disconnect import connect_to_voice_channel
    
    await connect_to_voice_channel(message);
    await startup_e()

    #---------------TIME VARIABLES--------------
    
    cfg.study_time_global = await handle_study_time(await study_time(message));
    cfg.rest_time_global = await handle_rest_time(await rest_time(message));

    #----------------OPEN----------------------
    from handle_variables import list_keys, bot_id, get_keys
    from start import start_pomodoro
    
    await start_pomodoro();
    
    from messages import message_avaiable_users_to_join
    
    await message_avaiable_users_to_join(message, await avaiable_users_to_join(await list_keys(await get_keys(message)), await bot_id()));
    
    #---------------CLOSE-----------------------
    pomoclose1 = cfg.close1

    pomoclose1.set_functions(repeatedly_execution)
    pomoclose1.set_args(cfg.study_time_global, cfg.rest_time_global, mute_all, unmute_all, message, cfg.ids)
    
    pomoclose1.if_when('yes')

    await after_30_seconds_close_pomodoro(message);
    
      
  if message.content.startswith('.join'):
    from handle_variables import get_ids
    
    await get_ids(message)

  if message.content.startswith('.mute'):
    await mute_all(message, cfg.ids);

  if message.content.startswith('.unmute'):
    await unmute_all(message, cfg.ids);

  if message.content.startswith('.stop'):
    await message.channel.send('Pomodoro stopped')
    await unmute_all(message, cfg.ids)
    #task_study.cancel()
    #task_rest.cancel()

#---------------IF-EXECUTE------------------

client.run(os.environ['TOKEN'])