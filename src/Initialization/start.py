import os
import gc
import src.Configs.configs as cfg
import logging
from src.cli.ppadron import prntpdr
from src.Configs.setup import setup
from src.Configs.events import events
from src.Configs.slash import slash

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
  return