import logging

def SMLOG():
  SM = logging.getLogger("SecurityMessage")
  SM.setLevel(level = logging.ERROR)
  SM_HANDLER=logging.FileHandler(filename = 'SM.log', mode = 'a')
  SM_FORMAT=logging.Formatter('%(asctime)s - %(message)s')
  SM_HANDLER.setFormatter(SM_FORMAT)
  SM.addHandler(SM_HANDLER)
  return SM

def EVENTLOG():
  LOGGER = logging.getLogger("Event")
  LOGGER.setLevel(level = logging.WARNING)
  logging_handler=logging.FileHandler(filename='log.log', mode='a')
  logging_format=logging.Formatter('%(asctime)s - %(message)s')
  logging_handler.setFormatter(logging_format)
  LOGGER.addHandler(logging_handler)
  return LOGGER