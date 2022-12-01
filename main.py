import os
import asyncio
import nest_asyncio
import nextcord
import threading
from PomoBot.src.Configs.configs import *
from PomoBot.src.boot.start import start
from PomoBot.src.Configs.configs import db
from PomoBot.src.Configs.loops import loopClient
nest_asyncio.apply()
#Tasks:
#Implement a way to load time remaining
#Implement a way to warn when time is up
#Delete the old message oriented implementations
def main():
    global bootWorker, ws, start, startWorker
    asyncio.set_event_loop(loopClient)
    def bootWorker(ws:nextcord.Client, loop:asyncio.AbstractEventLoop, token):
      asyncio.set_event_loop(loop=loop)
      loop.run_until_complete(ws.start(token))
    def startWorker(loop:asyncio.AbstractEventLoop):
      asyncio.set_event_loop(loop=loop)
      loop.run_until_complete(start())
    auth=os.getenv("TOKEN")
    p1 = threading.Thread(target=bootWorker, args=(client, loopClient, auth,), daemon=True)
    var2 = threading.Thread(target = startWorker, args=(loopClient,))
    if __name__ == '__main__':
        var2.start()
        var2.join()
        p1.start()
        p1.join()
        var2.join()
    return 

if __name__ == '__main__':
  main()