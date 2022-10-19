import os
import gc
import Configs.configs as cfg
from Cli_Commands.Print_Padronization.ppadron import prntpdr
from Configs.setup import setup
from Configs.events import events
from Configs.slash import slash
import logging
#from replit import db

async def start():
  os.system('clear')
  prntpdr(cfg.black, "collecting garbage")
  gc.collect(0)
  gc.collect(1)
  gc.collect(2)
  prntpdr(cfg.green, "collected")
  prntpdr(cfg.black, "loading files")
  setup()
  logger=logging.getLogger("Event")
  await events(logger)
  await slash(logger)
  prntpdr(cfg.green, "loaded")
  return