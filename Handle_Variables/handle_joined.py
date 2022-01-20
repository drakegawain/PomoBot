#--------IMPORTS-------------
import Configs.configs as cfg
#----------------------------
#---------JOINED-OR-NOT------
async def handle_joined(message):
  session=cfg.session.get('{}'.format('SESSION1'))
  #see if the user that try to join already joined
  ids_get=session.get('ids_get')
  if ids_get.count(message.author.id)==1:
    session.set_global_variable('joined',1)
    return
  #if cfg.ids_get.count(message.author.id) == 1:
    #cfg.joined = 1;
    #return
  if ids_get.count(message.author.id)>1:
    session.set_global_variable('joined', 1)
    return
  #if cfg.ids_get.count(message.author.id) > 1:
    #cfg.joined = 2;
    #return

async def joined_function(message):
  #do something if already joined or not
  session=cfg.session.get('{}'.format('SESSION1'))
  await handle_joined(message);
  joined = session.get('joined')
  if joined==1:
    return 'Joined'
  #if cfg.joined == 1:
    #return 'Joined'
  if joined==2:
    return 'Already Joined'
  #if cfg.joined == 2:
    #return 'Already Joined'
#-----------------------------