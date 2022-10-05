import nest_asyncio
import Configs.configs as cfg
from Cli_Commands.Print_Padronization.ppadron import prntpdr
import logging

def setup():
  prntpdr(cfg.black, "setting configurations...")
  logger = logging.getLogger(__name__)
  logger.setLevel(level=logging.WARNING)
  logging_handler=logging.FileHandler(filename='log.log', mode='a')
  logging_format=logging.Formatter('%(asctime)s - %(message)s')
  logging_handler.setFormatter(logging_format)
  logger.addHandler(logging_handler)
  nest_asyncio.apply()
  prntpdr(cfg.black, "uploading PomoBot...")
  return logger