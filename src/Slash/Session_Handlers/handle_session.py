import logging

async def session_handler(dictio:dict, session):
  try:
    for key, value in dictio.items():
      if session == value:
          found_key = key
          break
  except:
    raise Exception
    SM = logging.getLogger("SecurityMessage")
    SM.error("Error in session_handler")
  return found_key