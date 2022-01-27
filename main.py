#---------------BASIC-CONFIGs-------------------
import os
import nest_asyncio
import sys
os.system('clear')
import gc
#-----------------------------------------------
print('collecting garbage')
gc.collect(0)
gc.collect(1)
gc.collect(2)
print('collected')
#-------------------IMPORTs---------------------
#imports from the project
#you can see more of the functions in the respective files
print('loading files')
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
from Pomodoro.Session_Handlers.get_session import get_session_pomojoin, get_session_ps
from Pomodoro.Session_Handlers.check_session import ch_session
from Pomodoro.Session_Handlers.del_session import delete
from Commands.pomodoro import command_pomodoro
from Commands.pomostop import command_pomostop
print('loaded')
#-----------------------------------------------
#------------------SETUPs-----------------------
print('setting configurations...')
nest_asyncio.apply()
import Configs.configs as cfg
from replit import db
print('Sessions:{key}{value}'.format(key=cfg.session.keys(),value=cfg.session.values()))
print('upping the bot...')
#-----------------------------------------------
#-------------------EVENTs----------------------
@client.event
async def on_ready():
  #db["{command}_{bad_access}".format(command='pomostop', bad_access='121')] = "{reason}".format(reason='No session running in this v_channel.')
  print('online')
  pass

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.pomohelp'):
    await message_help(message)
    return

  if message.content.startswith('.pomodoro'):
    print('Sessions:{key}{value}'.format(key=cfg.session.keys(),value=cfg.session.values()))
    await command_pomodoro(message)
  
  if message.content.startswith('.pomojoin'):
    try:
      cur_vchan_session=await get_session_pomojoin(message, message.author.voice.channel, cfg.session)
    except:
      print('ERROR IN: .POMOJOIN')
      raise Exception
    else:
      await get_ids(message, cur_vchan_session)

  if message.content.startswith('.pomotest'):
    try:
      print('pass')
      await check_pomostop(message.author.id, message)
    except TypeError:
      print('Erou')

  if message.content.startswith('.pomostop'):
    print('Sessions:{key}{value}'.format(key=cfg.session.keys(),value=cfg.session.values()))
    await command_pomostop(message)
      # cur_vchan_session=await get_session_ps(message, message.author.voice.channel, cfg.session)
      # try:
      #     TRUE_OR_FALSE=await check_pomostop(message.author.id, message, cur_vchan_session)
      #     if TRUE_OR_FALSE is False:
      #       raise Exception
      # except:
      #     print('ERROR IN: .pomostop')
      # else:
      #     try:
      #           cur_vchan_session.close.cancel()
      #     except:
      #           print('ERROR in : .pomostop.else.except')
      #           cur_vchan_session.class_e.release_future()
      #           cur_vchan_session.class_i.release_future()
      #           try:
      #               FALSEORTRUE=await ch_session(cur_vchan_session)
      #               if FALSEORTRUE is True:
      #                   cur_vchan_session.restart()
      #               if FALSEORTRUE is False:
      #                   await delete(cfg.session, cur_vchan_session)
      #           except:
      #               print('ERROR IN: .pomostop.else.except.try')
      #           finally:
      #               await disconnect_from_voice_channel()
      #               await message.channel.send('stopped')
      #     else:
      #           F_or_T=await ch_session(cur_vchan_session)
      #           if F_or_T is True:
      #               cur_vchan_session.restart()
      #           if F_or_T is False:
      #               await delete(cfg.session, cur_vchan_session)
      #     finally:
      #       await disconnect_from_voice_channel()
      #       await message.channel.send('stopped')

      
    #session=cfg.session.get('{}'.format('Session1'))
    
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