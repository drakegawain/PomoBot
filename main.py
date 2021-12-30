import os
import asyncio
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
    await message.channel.send('\n<@%s>Every command that need inputs will be interpreted by the bot as minutes.\n.help - Show the avaible commands \n.pomodoro - Starts a pomodoro counter, example: .pomodoro 25 15\n.stop - stop pomodoro counter' % message.author.id)
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
    from utilitys import _create_task
    
    cfg.close.set_function(Task01 = repeatedly_execution).set_args(cfg.study_time_global, unmute_all, message, cfg.ids);
    cfg.close.set_function(Task02 = repeatedly_execution).set_args(cfg.rest_time_global + cfg.study_time_global, unmute_all, message, cfg.ids);
    cfg.close.if_when('yes')
    await after_30_seconds_close_pomodoro(message);
    
      #task_study = asyncio.create_task(repeatedly_execution(cfg.study_time_global, unmute_all, message, cfg.ids));
      #task_rest = asyncio.create_task(repeatedly_execution(cfg.rest_time_global + cfg.study_time_global, mute_all, message, cfg.ids));
      
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
