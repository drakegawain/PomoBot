import logging
import nextcord
from nextcord.ext import commands as Ncommands
from ..Slash.messages import message_help
from ..Slash.errorClasses import NoSessionRunning_pomojoin, NoSessionRunning_pomostop
from ..Slash.commands import command_pomodoro as sc_pomodoro
from ..Slash.commands import command_pomostop as sc_pomostop
from ..Slash.commands import command_pomojoin as sc_pomojoin
from ..Slash.commands import silentPomo, silentStop, silentJoin
from ..Slash.manageVars import handle_rest_time, handle_study_time
from ..Configs.setup import get_silent
from ..Configs.configs import client

async def slash(logger:logging.Logger, SM:logging.Logger, embed:nextcord.Embed):
  @client.slash_command(
    name="pomohelp",
    description="Show all the commands",
    force_global=True,
  )
  async def pomohelp(ctx:nextcord.Interaction):
    try:
      await message_help(ctx, embed)
      logger.warning("{} raised pomohelp".format(ctx.guild.name))
    except:
      raise Exception
      return
  
  @client.slash_command(
      name="pomodoro",
      description="This command starts pomodoro",
      force_global=True,
  )
  async def pomodoro(ctx:nextcord.Interaction, 
          study_time: int=nextcord.SlashOption(
          name='study_time',
          description='Time to study',
          required=True,
    ),
        rest_time: int=nextcord.SlashOption(
          name='rest_time',
          description='Time to rest',
          required=True,
    ),
        silent: bool=nextcord.SlashOption(
          name='silent_mode',
          description="Only text reminders",
          required=True,
          default=True,
        )
  ):
    logger.warning("{} raised pomodoro".format(ctx.guild.name))
    study_time = await handle_study_time(study_time)
    rest_time = await handle_rest_time(rest_time)
    if silent == False:
      await sc_pomodoro(ctx, study_time, rest_time, SM, logger, embed)
    if silent == True:
      await silentPomo(ctx, study_time, rest_time, logger, embed)
    return

  @client.slash_command(
    name="pomostop",
    description="Stops the current pomodoro's session",
    force_global=True,
  )
  async def pomostop(ctx:nextcord.Interaction):
    logger.warning("{} raised pomostop".format(ctx.guild.name))
    silent=await get_silent(ctx)
    if silent == True:
      await silentStop(ctx, logger, embed)
    if silent == False:
      await sc_pomostop(ctx, SM, embed)
    if str(silent) == "None":
      raise NoSessionRunning_pomostop(ctx)
    return

  @client.slash_command(
    name="pomojoin",
    description="Join the current pomodoro's session",
    force_global=True,
  )
  async def pomojoin(ctx:nextcord.Interaction):
    logger.warning("{} raised pomojoin".format(ctx.guild.name))
    silent=await get_silent(ctx)
    if silent == True:
      await silentJoin(ctx, logger)
    if silent == False:
      await sc_pomojoin(ctx, logger, SM, embed)
    if str(silent) == "None":
      raise NoSessionRunning_pomojoin(ctx)
    return

  @client.slash_command(
    name="pomobug",
    description="Found a bug? Send to us!",
    force_global=True,
  )
  async def pomobug(ctx:nextcord.Interaction):
    await ctx.send('Found a bug? Please, send us a report in the following form : https://forms.gle/ABgZpRq3JPBrurve7 or in https://github.com/drakegawain/PomoBot/issues', embed=embed)
    logger.warning("Bug on {}".format(ctx.guild.name))
    return
    
  return