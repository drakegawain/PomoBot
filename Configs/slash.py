from Slash.Discord_Actions.Messages.messages import message_help
from Slash.Session_Handlers.get_session import NoSessionRunning_pomojoin, NoSessionRunning_pomostop
from Slash.Commands.pomodoro import command_pomodoro as sc_pomodoro
from Slash.Commands.pomostop import command_pomostop as sc_pomostop
from Slash.Commands.pomojoin import command_pomojoin as sc_pomojoin
from Slash.Commands.Silent.stpomo import stpomo
from Slash.Commands.Silent.ststop import ststop
from Slash.Commands.Silent.stjoin import stjoin
from Pomodoro.time_pomodoro import handle_rest_time, handle_study_time
from Configs.setup import get_silent
from Configs.configs import client
import nextcord
from nextcord.ext import commands as Ncommands

async def slash(logger):
  @client.slash_command(
    name="pomohelp",
    description="Show all the commands",
    force_global=True,
  )
  async def pomohelp(ctx: Ncommands.Context):
      await message_help(ctx)
      logger.warning("{} raised pomohelp".format(ctx.guild.name))
      return
  
  @client.slash_command(
      name="pomodoro",
      description="This command starts pomodoro",
      force_global=True,
  )
  async def pomodoro(ctx: Ncommands.Context, 
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
      await sc_pomodoro(ctx, study_time, rest_time)
    if silent == True:
      await stpomo(ctx, study_time, rest_time, logger)
    return

  @client.slash_command(
    name="pomostop",
    description="Stops the current pomodoro's session",
    force_global=True,
  )
  async def pomostop(ctx: Ncommands.Context):
    logger.warning("{} raised pomostop".format(ctx.guild.name))
    silent=await get_silent(ctx)
    if silent == True:
      await ststop(ctx, logger)
    if silent == False:
      await sc_pomostop(ctx)
    if str(silent) == "None":
      raise NoSessionRunning_pomostop(ctx)
    return

  @client.slash_command(
    name="pomojoin",
    description="Join the current pomodoro's session",
    force_global=True,
  )
  async def pomojoin(ctx: Ncommands.Context):
    logger.warning("{} raised pomojoin".format(ctx.guild.name))
    silent=await get_silent(ctx)
    if silent == True:
      await stjoin(ctx, logger)
    if silent == False:
      await sc_pomojoin(ctx)
    if str(silent) == "None":
      raise NoSessionRunning_pomojoin(ctx)
    return

  @client.slash_command(
    name="pomobug",
    description="Found a bug? Send to us!",
    force_global=True,
  )
  async def pomobug(ctx: Ncommands.Context):
    await ctx.send('Found a bug? Please, send us a report in the following form : https://forms.gle/ABgZpRq3JPBrurve7')
    logger.warning("Bug on {}".format(ctx.guild.name))
    return
    
  return