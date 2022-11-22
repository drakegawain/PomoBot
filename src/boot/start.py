import os
import gc
import logging
import asyncio
from ..Configs import configs as cfg
from ..cli.ppadron import prntpdr
from ..Configs.setup import setup
from ..Configs.events import events
from ..Configs.slash import slash

async def start():
  os.system('clc')
  prntpdr(cfg.black, "collecting garbage")
  gc.collect(0)
  gc.collect(1)
  gc.collect(2)
  prntpdr(cfg.green, "collected")
  prntpdr(cfg.black, "loading files")
  setup()
  SM = logging.getLogger("SecurityMessage")
  logger = logging.getLogger("Event")
  grsrc = logging.getLogger("GuildRsrc")
  await events(grsrc)
  await slash(logger, SM)
  prntpdr(cfg.green, "loaded")
  return True