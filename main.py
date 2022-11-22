import os
import nest_asyncio
from multiprocessing import Process
from .src.Configs.configs import client
from .src.boot.start import start


nest_asyncio.apply()
#Tasks:
#Implement a way to load time remaining
#Implement a way to warn when time is up
#Delete the old message oriented implementations



def main():
  token = os.environ['TOKEN']
  p1 = Process(target = start)
  p2 = Process(target = client.run, args=[token])
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  
  pass 
  
#if __name__ == "__main__":
#  loop=asyncio.get_event_loop()
#  loop.run_until_complete(main())