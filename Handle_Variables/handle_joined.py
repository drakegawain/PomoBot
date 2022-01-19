#--------IMPORTS-------------
import Configs.configs as cfg
#----------------------------
#---------JOINED-OR-NOT------
async def handle_joined(message):
  #see if the user that try to join already joined
  if cfg.ids_get.count(message.author.id) == 1:
    cfg.joined = 1;
    return
  if cfg.ids_get.count(message.author.id) > 1:
    cfg.joined = 2;
    return

async def joined_function(message):
  #do something if already joined or not
  await handle_joined(message);
  if cfg.joined == 1:
    return 'Joined'
  if cfg.joined == 2:
    return 'Already Joined'
#-----------------------------