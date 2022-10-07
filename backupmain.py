#---------------BASIC-CONFIGs-------------------
import os
import nest_asyncio
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
from Slash.Discord_Actions.Messages.messages import message_help
#from Commands.pomodoro import command_pomodoro
#from Commands.pomostop import command_pomostop
#from Commands.pomojoin import command_pomojoin
from Slash.Commands.pomodoro import command_pomodoro as sc_pomodoro
from Slash.Commands.pomostop import command_pomostop as sc_pomostop
from Slash.Commands.pomojoin import command_pomojoin as sc_pomojoin
from Pomodoro.Session_Handlers.search_session import search
from Pomodoro.Session_Handlers.del_session import delete
from Pomodoro.time_pomodoro import handle_rest_time, handle_study_time
import nextcord
import logging
from nextcord.ext import commands as Ncommands
prntpdr(cfg.green, "loaded")
#-----------------------------------------------
#------------------SETUPs-----------------------
prntpdr(cfg.black, "setting configurations...")
logging.basicConfig(filename='log.log', filemode='a', level=logging.WARNING, format='%(asctime)s - %(message)s')
nest_asyncio.apply()
import Configs.configs as cfg
from replit import db
prntpdr(cfg.black, "uploading PomoBot...")
#-----------------------------------------------
#-------------------EVENTs----------------------
@client.event
async def on_ready():
  #db["{command}_{bad_access}".format(command='pomodoro', bad_access='221')] = "{reason}".format(reason='Inputs must be integers => .pomohelp to + information')
  prntpdr(cfg.black, "creating sessions...")
  cfg.session_guilds = create_sessions()
  prntpdr(cfg.blue, "PomoBot:online")
  prntpdr(cfg.black, "total guilds:{}{}".format(cfg.green, cfg.total_guilds()))
  pass

@client.event
async def on_guild_join(guild: nextcord.Guild):
  logging.warning("{} joined".format(guild.name))
  prntpdr(cfg.black, "creating session for:{}".format(guild.name))
  cfg.session_guilds.append(cfg.SessionGuild(guild.name, cfg.total_guilds() - 1))
  return

@client.event
async def on_guild_remove(guild: nextcord.Guild):
  logging.warning("{} left".format(guild.name))
  prntpdr(cfg.red, "leaving:{}".format(guild.name))
  index=await search(guild, cfg.session_guilds)
  await delete(index, cfg.session_guilds)
  return
#------------------SLASH-COMMANDS-------------
@client.slash_command(
  name="pomohelp",
  description="Show all the commands",
  force_global=True,
)
async def pomohelp(ctx: Ncommands.Context):
    await message_help(ctx)
    logging.warning("{} raised pomohelp".format(ctx.guild.name))
    return
  
@client.slash_command(
    name="pomodoro",
    description="This command starts pomodoro",
    force_global=True,
)
async def pomodoro(ctx: Ncommands.Context, 
        study_time: int=nextcord.SlashOption(
          name='study time',
          description='time for study and time for rest',
          required=True,
    ),
        rest_time: int=nextcord.SlashOption(
          name='rest time',
          description='time to rest',
          required=True,
    ),
        silent: bool=nextcord.SlashOption(
          name='silent mode',
          description="Only text reminders",
          required=False,
          default=True,
        )
  ):
    logging.warning("{} raised pomodoro".format(ctx.guild.name))
    study_time=await handle_study_time(study_time)
    rest_time=await handle_rest_time(rest_time)
    await sc_pomodoro(ctx,study_time,rest_time, silent)
    return

@client.slash_command(
  name="pomostop",
  description="Stops the current pomodoro's session",
  force_global=True,
)
async def pomostop(ctx: Ncommands.Context):
  logging.warning("{} raised pomostop".format(ctx.guild.name))
  await sc_pomostop(ctx)
  return

@client.slash_command(
  name="pomojoin",
  description="Join the current pomodoro's session",
  force_global=True,
)
async def pomojoin(ctx: Ncommands.Context):
  logging.warning("{} raised pomojoin".format(ctx.guild.name))
  await sc_pomojoin(ctx)
  return

@client.slash_command(
  name="pomobug",
  description="Found a bug? Send to us!",
  force_global=True,
)
async def pomobug(ctx: Ncommands.Context):
  await ctx.send('Found a bug? Please, send us a report in the following form : https://forms.gle/ABgZpRq3JPBrurve7')
  logging.warning("Bug on {}".format(ctx.guild.name))
  return
#---------------------------------------------
#---------------LOGGIN-----------------
token=os.environ['TOKEN']
client.run(token)
#--------------------------------------