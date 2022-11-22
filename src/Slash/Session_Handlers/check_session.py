#----------------IMPORTs------------------
from ...Slash.Classes.session import Session
#-----------------------------------------
#-----------------SETUPs------------------
#-----------------------------------------
async def ch_session(dictio:dict, session):
  try:
    if dictio[session] is dictio['Main']:
      return True
    else:
      return False
  except:
    raise Exception 
  return 

async def new_session(dictio:dict):
  dictio['Session_{number}'.format(number=len(dictio))]=Session()
  session=dictio.get('{Session_{number}}'.format(number=len(dictio)))
  return session

async def gather(dictio:dict):
  """Return last session"""
  last_session=len(dictio)
  keys=list(dictio.keys())
  l_session=keys[last_session-1]
  return l_session