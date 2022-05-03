#--------IMPORTS-------------
from Slash.Utilitys.fetch_informations import fetch
#----------------------------
#---------JOINED-OR-NOT------
async def handle_joined(ctx, session):
  """See if the user that try to join already joined"""
  response=fetch(ctx)
  author=response[1]
  ids_get=session.ids_get
  if ids_get.count(author.id)==1:
    session.joined=1
    return
  if ids_get.count(author.id)>1:
    session.joined=2
    return
  

async def joined_function(ctx, session):
  """Handle joined variable"""
  await handle_joined(ctx, session);
  joined = session.joined
  if joined==1:
    return 'Joined'
  if joined==2:
    return 'Already Joined'
#-----------------------------