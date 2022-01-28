#---------------BASIC-CONFIGs-------------------
import os
import nest_asyncio
import sys
os.system('clear')
import gc
import Configs.configs as cfg
#-----------------------------------------------
print('{}collecting garbage'.format(cfg.black))
gc.collect(0)
gc.collect(1)
gc.collect(2)
print('{}collected'.format(cfg.green))
#-------------------IMPORTs---------------------
#imports from the project
#you can see more of the functions in the respective files
print('{}loading files'.format(cfg.black))
from Configs.configs import client
from Discord_Actions.Messages.messages import  message_help
from Handle_Variables.handle_variables import get_ids
from Security.Command_Check.pomostop_check import check_pomostop
from Pomodoro.Session_Handlers.get_session import get_session_pomojoin
from Commands.pomodoro import command_pomodoro
from Commands.pomostop import command_pomostop
print('{}loaded'.format(cfg.green))
#-----------------------------------------------
#------------------SETUPs-----------------------
print('{}setting configurations...'.format(cfg.black))
nest_asyncio.apply()
import Configs.configs as cfg
from replit import db
print('Sessions:{key}{value}'.format(key=cfg.session.keys(),value=cfg.session.values()))
print('{}uploading PomoBot...'.format(cfg.black))
#-----------------------------------------------
#-------------------EVENTs----------------------
@client.event
async def on_ready():
  #db["{command}_{bad_access}".format(command='pomostop', bad_access='121')] = "{reason}".format(reason='No session running in this v_channel.')
  print('{}online'.format(cfg.blue))
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
#---------------------------------------------
#---------------LOGGIN-----------------
client.run(os.environ['TOKEN'])

#--------------------------------------