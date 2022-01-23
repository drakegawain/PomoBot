async def delete(
  DICT, LAST_SESSION
):
  if DICT[LAST_SESSION] is not DICT['Main']:
    del DICT[LAST_SESSION]
  else:
    raise Exception('Cannot delete Main session')
  return