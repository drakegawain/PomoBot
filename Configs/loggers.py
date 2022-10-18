import logging

def SMLOG():
  SM = logging.getLogger("SecurityMessage")
  SM.setLevel(level = logging.ERROR)
  SM_HANDLER=logging.FileHandler(filename = 'SM.log', mode = 'a')
  SM_FORMAT=logging.Formatter('%(asctime)s - %(message)s')
  SM_HANDLER.setFormatter(SM_FORMAT)
  SM.addHandler(SM_HANDLER)
  return SM