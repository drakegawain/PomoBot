#---------------BASIC-CONFIGs-------------------
import os
import nest_asyncio
import sys
os.system('clear')
import gc
import Configs.configs as cfg
from Cli_Commands.Print_Padronization.ppadron import prntpdr
#-----------------------------------------------
prntpdr(cfg.black, "collecting garbage")
gc.collect(0)
gc.collect(1)
gc.collect(2)
prntpdr(cfg.green, "collected")
#-------------------IMPORTs---------------------
prntpdr(cfg.black, "loading files")
from Configs.configs import client, create_sessions
from Discord_Actions.Messages.messages import  message_help
from Security.Command_Check.pomostop_check import check_pomostop
from Commands.pomodoro import command_pomodoro
from Commands.pomostop import command_pomostop
from Commands.pomojoin import command_pomojoin
import discord
prntpdr(cfg.green, "loaded")
#-----------------------------------------------
#------------------SETUPs-----------------------
prntpdr(cfg.black, "setting configurations...")
nest_asyncio.apply()
import Configs.configs as cfg
from replit import db
prntpdr(cfg.black, "uploading PomoBot...")
#-----------------------------------------------
#-------------------EVENTs----------------------
@client.event
async def on_ready():
  #db["{command}_{bad_access}".format(command='pomodoro', bad_access='271')] = "{reason}".format(reason='Only one session per voice_channel at the same time')
  prntpdr(cfg.black, "creating sessions...")
  cfg.session_guilds = create_sessions()
  prntpdr(cfg.blue, "PomoBot: online")
  prntpdr(cfg.black, "total guilds:{}{}".format(cfg.green, cfg.total_guilds()))
  pass

@client.event
async def on_guild_join(guild: discord.Guild):
  prntpdr(cfg.black, "creating session for :{}'.format(guild.name)")
  return

@client.event
async def on_guild_remove(guild: discord.Guild):
  prntpdr(cfg.red, "leaving:{}".format(guild.name))
  return

@client.event 
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('.pomohelp'):
    await message_help(message)
    return

  if message.content.startswith('.pomodoro'):
    prntpdr(cfg.black, "raising message: {}".format(message.content))
    await command_pomodoro(message)
  
  if message.content.startswith('.pomojoin'):
    await command_pomojoin(message)

  if message.content.startswith('.pomobug'):
    prntpdr(cfg.red, "Bug on: {}".format(message.guild.name))
    await message.channel.send('Found a bug? Please, send us a report in the following form : https://forms.gle/ABgZpRq3JPBrurve7')

  if message.content.startswith('.pomostop'):
    await command_pomostop(message)
    
#---------------------------------------------
#---------------LOGGIN-----------------
client.run(os.environ['TOKEN'])
#--------------------------------------