#THIS FILE CHECK IF THE CALLING ID
#ALREADY IS IN ANOTHER SESSION
#IF YES RAISE AN ERROR
#-----------------IMPORTs-----------
from Pomodoro.Session_Handlers.search_session import s_for_id
#-----------------------------------

class Error(Exception):
  """Base Class for other exceptions"""

class MoreThanOneSession(Error):
  """USER CANT BE IN MORE THAN ONE SESSION"""
  pass

async def c_for_doubles(dictio:dict, ID:int):
    print('cfordoubles')
    search=await s_for_id(dictio, ID)
    print("search {}".format(search))
    if search is True:
        raise MoreThanOneSession
    else:
        pass
    return