import os
import asyncio
from Configs.configs import client
from Initialization.start import start

#Errors:
#It seems to work
#Implement a way to load time remaining

async def main():
  await start()
  token=os.environ['TOKEN']
  client.run(token)
  return
  
if __name__ == "__main__":
  loop=asyncio.new_event_loop()
  loop.run_until_complete(main())