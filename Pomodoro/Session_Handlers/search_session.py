#---------------------IMPORTs------------------
#import Configs.configs as cfg
#from Pomodoro.Session_Handlers.get_session import get_session
#from Cli_Commands.Print_Padronization.ppadron import prntpdr
#----------------------------------------------

async def search(guild, session_list):
  guild_name=guild.name
  for index in range(len(session_list)):
    guild_name_session_list=session_list[index].get_guild_name()
    if guild_name_session_list is guild_name:
      return session_list[index].get_index()
  for index in range(len(session_list)+1):
    guild_name_session_list=session_list[index].get_guild_name()
    if guild_name_session_list is guild_name:
      return session_list[index].get_index()

async def s_for_id(dictio:dict, ID:int):
    HANDLER=None
    for value in dictio.values():
        for i_d in list(value.ids):
            print(i_d)
            if i_d is ID:
                HANDLER=True
    return HANDLER
