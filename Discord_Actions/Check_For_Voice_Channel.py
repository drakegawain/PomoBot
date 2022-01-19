import Configs.configs as cfg


async def check_for_voice_channel():
  print('Inside function {}' .format(__name__))
  voice_clients=cfg.client.voice_clients
  print('Lenght {}' .format(len(voice_clients)))
  for user in voice_clients:
    print('Users: {}' .format(user.users))
  return

async def is_anyone_connected_to_a_voice_channel():
  channels = cfg.client.voice_clients
  for ch in channels:
    print(ch)
  return