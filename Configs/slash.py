from Slash.Discord_Actions.Messages.messages import message_help
from Slash.Commands.pomodoro import command_pomodoro as sc_pomodoro
from Slash.Commands.pomostop import command_pomostop as sc_pomostop
from Slash.Commands.pomojoin import command_pomojoin as sc_pomojoin
from Pomodoro.time_pomodoro import handle_rest_time, handle_study_time
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
    logger.warning("{} raised pomodoro".format(ctx.guild.name))
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
    logger.warning("{} raised pomostop".format(ctx.guild.name))
    await sc_pomostop(ctx)
    return

  @client.slash_command(
    name="pomojoin",
    description="Join the current pomodoro's session",
    force_global=True,
  )
  async def pomojoin(ctx: Ncommands.Context):
    logger.warning("{} raised pomojoin".format(ctx.guild.name))
    await sc_pomojoin(ctx)
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