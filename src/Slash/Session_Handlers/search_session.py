async def search(guild, session_list):
  for session in session_list:
    if session.get_guild_name() == guild.name:
      return session.get_index()

async def s_for_id(dictio:dict, ID:int):
    HANDLER=None
    for value in dictio.values():
        for i_d in list(value.ids):
            print(i_d)
            if i_d is ID:
                HANDLER=True
    return HANDLER
