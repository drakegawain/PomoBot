def fetch(ctx):
  """This function gather all usefull information from context interactions"""
  message=ctx.message
  guild=ctx.guild
  author=ctx.user
  return_array=[message, author, guild]
  return return_array