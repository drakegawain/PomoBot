import gc
import logging
from ...Configs import configs as cfg

async def delete(index, list):
  try:
    garbage=list[index].session["Main"].restart()
    garbage=gc.collect()
  except:
    SM = logging.getLogger("SecurityMessage")
    SM.error("Error in deleting guild {}".format(list[index].guild_name))
  return