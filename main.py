import os
import asyncio
from .src.Configs.configs import client
from .src.Initialization.start import start

#Tasks:
#Implement a way to load time remaining
#Implement a way to warn when time is up
#Delete the old message oriented implementations

async def main():
  await start()
  token=os.environ['TOKEN']
  client.run(token)
  return
  
if __name__ == "__main__":
  loop=asyncio.new_event_loop()
  loop.run_until_complete(main())