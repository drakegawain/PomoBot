import asyncio
import threading
import types
from typing import Optional

#threading.Thread.

class Worker:
    def __init__(self, loop:asyncio.AbstractEventLoop, func:types.CoroutineType, args:Optional[tuple] = (), kargs:Optional[dict] = {}, parent: threading.Thread = threading.current_thread()) -> None:
        self.loop = loop
        self.func = func
        self.args = args
        self.kargs = kargs
        self.parent = parent
        self.t = None
        print(threading.current_thread())
        self.__tool()
        pass
    def labor(self, *args, **kargs):
        asyncio.set_event_loop(self.loop)
        if args != ():
            if kargs != {}:
                self.loop.run_until_complete(self.func(*args, **kargs))
                self.parent.join()
                return
            print("inside if 2")
            self.loop.run_until_complete(self.func(*args))
            self.parent.join()
            return
        if kargs != {}:
            print("inside if 3")
            #print(**kargs)
            self.loop.run_until_complete(self.func(**kargs))
            self.parent.join()
            return
        self.parent.join()
        return 
    def __tool(self):
        self.t = threading.Thread(target = self.labor, args=self.args, kwargs=self.kargs)
        self.t.start()
        # if self.args != ():
        #     if self.kargs != {}:
        #         t = threading.Thread(target = self.labor, args=self.args, kwargs=self.kargs)
        #         t.start()
        #     t = threading.Thread(target=self.labor, args=self.args)
        #     t.start()
        # if self.kargs != {}:
        #     t = threading.Thread(target=self.labor, kwargs=self.kargs)
        #     t.start()
