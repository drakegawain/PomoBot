import os
import gc
import Configs.configs as cfg
from Cli_Commands.Print_Padronization.ppadron import prntpdr
from Configs.setup import setup
from Configs.events import events
from Configs.slash import slash
#from replit import db

async def start():
  os.system('clear')
  prntpdr(cfg.black, "collecting garbage")
  gc.collect(0)
  gc.collect(1)
  gc.collect(2)
  prntpdr(cfg.green, "collected")
  prntpdr(cfg.black, "loading files")
  prntpdr(cfg.green, "loaded")
  logger=setup()
  await events(logger)
  await slash(logger)
  return