#---------------IMPORTs-------------------
import src.Configs.configs as cfg
#-----------------------------------------

def guilds_names():
  for guild in cfg.client.guilds:
    print(guild.name)
  return