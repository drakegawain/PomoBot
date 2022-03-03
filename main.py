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
print('{}loading files'.format(cfg.black))
from Configs.configs import client, create_sessions
from Discord_Actions.Messages.messages import  message_help
from Security.Command_Check.pomostop_check import check_pomostop
from Commands.pomodoro import command_pomodoro
from Commands.pomostop import command_pomostop
from Commands.pomojoin import command_pomojoin
import discord
print('{}loaded'.format(cfg.green))
#-----------------------------------------------
#------------------SETUPs-----------------------
print('{}setting configurations...'.format(cfg.black))
nest_asyncio.apply()
import Configs.configs as cfg
from replit import db
print('{}uploading PomoBot...'.format(cfg.black))

#-----------------------------------------------
#-------------------EVENTs----------------------
@client.event
async def on_ready():
  #db["{command}_{bad_access}".format(command='pomodoro', bad_access='271')] = "{reason}".format(reason='Only one session per voice_channel at the same time')
  print('{}creating sessions...'.format(cfg.black))
  cfg.session_guilds = create_sessions()
  print('{}PomoBot: online'.format(cfg.blue))
  print('{}total guilds:{}{}'.format((cfg.black),cfg.green ,cfg.total_guilds()))
  #print('{}guild name:{}'.format((cfg.green), cfg.guilds_connected()))
  pass

@client.event
async def on_guild_join(guild: discord.Guild):
  print('creating session for :{}'.format(guild.name))
  cfg.session_guilds.append(cfg.SessionGuild(guild.name, cfg.total_guilds() - 1))
  print(guild.name)
  return

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.pomohelp'):
    await message_help(message)
    return

  if message.content.startswith('.pomodoro'):
    print("raising message: {}".format(message.content))
    await command_pomodoro(message)
  
  if message.content.startswith('.pomojoin'):
    await command_pomojoin(message)

  if message.content.startswith('.pomobug'):
    print('Bug on: {}'.format(message.guild.name))
    await message.channel.send('Found a bug? Please, send us a report in the following form : https://forms.gle/ABgZpRq3JPBrurve7')

  if message.content.startswith('.pomostop'):
    await command_pomostop(message)
    
#---------------------------------------------
#---------------LOGGIN-----------------
client.run(os.environ['TOKEN'])
#--------------------------------------