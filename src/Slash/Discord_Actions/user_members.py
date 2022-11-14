async def mention_ids(session):
  IDS_MENTION = []
  IDS_MENTION=list(session.ids)
  for INDEX, ID in enumerate(IDS_MENTION):
    IDS_MENTION[INDEX] = "<@%s>" % IDS_MENTION[INDEX]
  return IDS_MENTION

async def avaiable_users_to_join(list_keys, bot_id):
  """This function finds the avaiable users to participate the study/work"""
  ids_mention = []
  i = len(list_keys)
  for index in range(i):
    if list_keys[index] != bot_id:
      ids_mention.append(index)
      ids_mention[index] = '<@%s>' % list_keys[index]
      return ids_mention