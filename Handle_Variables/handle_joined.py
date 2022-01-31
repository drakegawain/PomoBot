#--------IMPORTS-------------
#----------------------------
#---------JOINED-OR-NOT------
async def handle_joined(message, session):
  """see if the user that try to join already joined"""
  ids_get=session.ids_get
  if ids_get.count(message.author.id)==1:
    session.joined=1
    return
  if ids_get.count(message.author.id)>1:
    session.joined=2
    return
  

async def joined_function(message, session):
  """do something if already joined or not"""
  await handle_joined(message, session);
  joined = session.joined
  if joined==1:
    return 'Joined'
  if joined==2:
    return 'Already Joined'
#-----------------------------