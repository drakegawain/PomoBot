import configs as cfg

async def handle_joined(message):
  if cfg.ids_get.count(message.author.id) == 1:
    cfg.joined = 1;
    return
  if cfg.ids_get.count(message.author.id) > 1:
    cfg.joined = 2;
    return

async def joined_function(message):
  await handle_joined(message);
  if cfg.joined == 1:
    return 'Joined'
  if cfg.joined == 2:
    return 'Already Joined'