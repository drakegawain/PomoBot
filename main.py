import os
import asyncio
import nest_asyncio
import nextcord
import threading
from PomoBot.src.Configs.configs import *
from PomoBot.src.boot.start import start
from PomoBot.src.Configs.configs import db
from PomoBot.src.Configs.loops import loopBoot, loopClient, loopMain
nest_asyncio.apply()
#Tasks:
#Implement a way to load time remaining
#Implement a way to warn when time is up
#Delete the old message oriented implementations
def main():
    global worker, ws, start
    #asyncio.set_event_loop(loopMain)
    def worker(ws:nextcord.Client, loop:asyncio.AbstractEventLoop, token):
      asyncio.set_event_loop(loop=loop)
      loop.run_until_complete(ws.start(token))
    def wrker(loop:asyncio.AbstractEventLoop):
      asyncio.set_event_loop(loop=loop)
      loop.run_until_complete(start())
      loop.close()
    auth=os.getenv("TOKEN")
    p1 = threading.Thread(target=worker, args=(client, loopClient, auth,), daemon=True)
    var2 = threading.Thread(target = wrker, args=(loopBoot,))
    if __name__ == '__main__':
        var2.start()
        var2.join()
        p1.start()
        p1.join()
        var2.join()
    return 

if __name__ == '__main__':
  main()