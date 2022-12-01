import tracemalloc
import nextcord
from ..Configs import configs as cfg
from .configs import cursor, db, extract
from ..Configs.configs import client, create_sessions
from ..Slash.manageClasses import search, delete

async def events(logger):
  @client.event
  async def on_ready():
    cfg.session_guilds = create_sessions()
    try:
        cursor.execute("insert into botstatus (status, total, memory_usage) values ('Online', '{total}', '{memory_usage}');".format(
        total = cfg.total_guilds(), memory_usage = tracemalloc.get_traced_memory()[0]))
        db.commit()
        cursor.reset(True)
        #search = cursor.execute("select status from botstatus")
        #print(search)
        #print(cursor.fetchone()[0])
        #print(extract(cursor))
    except:
      raise Exception
    pass

  @client.event
  async def on_guild_join(guild: nextcord.Guild):
    logger.warning("{} new guild!".format(guild.name))
    cfg.session_guilds.append(cfg.SessionGuild(guild.name, cfg.total_guilds() - 1))
    pass

  @client.event
  async def on_guild_remove(guild: nextcord.Guild):
    logger.warning("{} left".format(guild.name))
    index=await search(guild, cfg.session_guilds)
    await delete(index, cfg.session_guilds)
    pass
  pass