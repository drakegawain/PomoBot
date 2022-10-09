async def mention_ids(session):
  IDS_MENTION = []
  IDS_MENTION=list(session.ids)
  for INDEX, ID in enumerate(IDS_MENTION):
    IDS_MENTION[INDEX] = "<@%s>" % IDS_MENTION[INDEX]
  return IDS_MENTION