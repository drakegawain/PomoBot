async def check_pomodoro(context_vchannel, dictio:dict, ctx):
  check=0
  for session in dictio:
    if dictio["{}".format(session)].vc is context_vchannel:
      print(dictio["{}".format(session)])
      check=True
      raise OneSessionPerVoiceChannel(ctx)
  check=False
  return check

async def check_pomostop(calling_id, ctx, session):
  try:
    list_ids=list(session.ids)#cfg.ids)
    if list_ids == []:
      raise Exception(TypeError)
    for id in list_ids:
      if id==calling_id:
        HANDLER=True
  except:
    raise UserOutsideSession(ctx)
    print('Error in: check_pomostop')
    HANDLER=False
  return HANDLER

async def doubleSession(dictio:dict, ID:int, ctx):
    search=await s_for_id(dictio, ID)
    if search is True:
        raise await MoreThenOneSession(ctx)
        return True
    else:
        return False
    return