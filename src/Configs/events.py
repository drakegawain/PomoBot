import src.Configs.configs as cfg
from src.Configs.configs import client, create_sessions
from src.Slash.Session_Handlers.search_session import search
from src.Slash.Session_Handlers.del_session import delete
import nextcord

async def events(logger):
  @client.event
  async def on_ready():
    cfg.session_guilds = create_sessions()
    pass

  @client.event
  async def on_guild_join(guild: nextcord.Guild):
    logger.warning("{} new guild!".format(guild.name))
    cfg.session_guilds.append(cfg.SessionGuild(guild.name, cfg.total_guilds() - 1))
    pass

  @client.event
  async def on_guild_remove(guild: nextcord.Guild):
    logger.warning("{} left".format(guild.name))
    prntpdr(cfg.red, "leaving:{}".format(guild.name))
    index=await search(guild, cfg.session_guilds)
    await delete(index, cfg.session_guilds)
    pass
  pass