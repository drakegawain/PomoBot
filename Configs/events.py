import Configs.configs as cfg
from Cli_Commands.Print_Padronization.ppadron import prntpdr
from Configs.configs import client, create_sessions
from Pomodoro.Session_Handlers.search_session import search
from Pomodoro.Session_Handlers.del_session import delete
import nextcord

async def events(logger):
  @client.event
  async def on_ready():
    #db["{command}_{bad_access}".format(command='pomodoro', bad_access='221')] =   "{reason}".format(reason='Inputs must be integers => .pomohelp to + information')
    prntpdr(cfg.black, "creating sessions...")
    cfg.session_guilds = create_sessions()
    prntpdr(cfg.blue, "PomoBot:online")
    prntpdr(cfg.black, "total guilds:{}{}".format(cfg.green, cfg.total_guilds()))
    pass

  @client.event
  async def on_guild_join(guild: nextcord.Guild):
    logger.warning("{} joined".format(guild.name))
    prntpdr(cfg.black, "creating session for:{}".format(guild.name))
    cfg.session_guilds.append(cfg.SessionGuild(guild.name, cfg.total_guilds() - 1))
    return

  @client.event
  async def on_guild_remove(guild: nextcord.Guild):
    logger.warning("{} left".format(guild.name))
    prntpdr(cfg.red, "leaving:{}".format(guild.name))
    index=await search(guild, cfg.session_guilds)
    await delete(index, cfg.session_guilds)
    return
    
  return