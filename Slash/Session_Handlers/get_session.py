async def get_session(guild, session_list:list):
  """This function finds the index from the list
    that handles the sessions"""
  guild_name=guild.name
  for index in range(len(session_list)):
    guild_name_session_list=session_list[index].get_guild_name()
    if guild_name_session_list is guild_name:
      return session_list[index].get_index()
  for index in range(len(session_list)+1):
    guild_name_session_list=session_list[index].get_guild_name()
    if guild_name_session_list is guild_name:
      return session_list[index].get_index()