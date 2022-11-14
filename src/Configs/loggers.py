import logging

def SMLOG():
  """Error logging handler. Writes the errors in SM.log (SM:SecurityMessage)"""
  SM = logging.getLogger("SecurityMessage")
  SM.setLevel(level = logging.ERROR)
  SM_HANDLER=logging.FileHandler(filename = 'SM.log', mode = 'a')
  SM_FORMAT=logging.Formatter('%(asctime)s - %(message)s')
  SM_HANDLER.setFormatter(SM_FORMAT)
  SM.addHandler(SM_HANDLER)
  return SM

def EVENTLOG():
  """Event logging handler. This file takes all events from the funcionalities from the bot. 
     Example: If a guild call the /pomobot command, this logger will write on file log.log that the guild
     called this command."""
  LOGGER = logging.getLogger("Event")
  LOGGER.setLevel(level = logging.WARNING)
  logging_handler=logging.FileHandler(filename='log.log', mode='a')
  logging_format=logging.Formatter('%(asctime)s - %(message)s')
  logging_handler.setFormatter(logging_format)
  LOGGER.addHandler(logging_handler)
  return LOGGER

def GLDRSRCLOG():
  """Guild resource logging handler. This handler takes all events from guilds that joined or lefted. Writes
     in grsrc.log (guild resource)"""
  LOGGER = logging.getLogger("GuildRsrc")
  LOGGER.setLevel(level = logging.WARNING)
  logging_handler=logging.FileHandler(filename='grsrc.log', mode='a')
  logging_format=logging.Formatter('%(asctime)s - %(message)s')
  logging_handler.setFormatter(logging_format)
  LOGGER.addHandler(logging_handler)
  return LOGGER