#----------------IMPORTs------------------
from Classes.session import Session
import Configs.configs as cfg
#-----------------------------------------
#-----------------SETUPs------------------
NEW_SESSION=Session()
#-----------------------------------------

async def ch_session(dictio:dict, session):
  if dictio[session] is dictio['Main']:
    return True
  else:
    return False
  return

async def new_session(dictio:dict):
  dictio['Session_{number}'.format(number=len(dictio))]=NEW_SESSION
  session=dictio.get('{Session_{number}}'.format(number=len(dictio)))
  return session

async def gather(dictionary:dict):
  #Return last session
  last_session=dictionary.len
  last_session=dictionary[last_session]
  return last_session