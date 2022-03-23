import gc
from Cli_Commands.Print_Padronization.ppadron import prntpdr
import Configs.configs as cfg

async def delete(index, list):
  try:
    garbage=list[index].session["Main"].restart()
    garbage=gc.collect()
  except:
    prntpdr(cfg.red, "Error in delete guild {} session".format(list[index].guild_name))
  return