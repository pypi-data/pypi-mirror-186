# This file is placed in the Public Domain.


"threads"


import queue
import threading
import time


from bot.objects import Object
from bot.utility import name


def __dir__():
    return (
            'Thread',
            'Timer',
            'Repeater',
            'launch',
            'name'
           )


__all__ = __dir__()


class Thread(threading.Thread):

    "basic thread class"

    def __init__(self, func, thrname, *args, daemon=True):
        ""
        super().__init__(None, self.run, name, (), {}, daemon=daemon)
        self._exc = None
        self._evt = None
        self._result = None
        self.name = thrname or name(func)
        self.queue = queue.Queue()
        self.queue.put_nowait((func, args))
        self.sleep = None
        self.state = Object()

    def __iter__(self):
        return self

    def __next__(self):
        for k in dir(self):
            yield k

    def join(self, timeout=None):
        "join this thread"
        super().join(timeout)
        return self._result

    def run(self) -> None:
        "fetch job and arguments from the queue and execute job with these arguments"
        func, args = self.queue.get()
        if args:
            self._evt = args[0]
            if "txt" in self._evt:
                self.name = self._evt.txt
        self.state.starttime = time.time()
        self._result = func(*args)

class Timer:

    "run a job x seconds from now"

    def __init__(self, sleep, func, *args, thrname=None):
        super().__init__()
        self.args = args
        self.func = func
        self.sleep = sleep
        self.name = thrname or name(self.func)
        self.state = {}
        self.timer = None

    def run(self):
        "run the timed job in a seperate thread"
        self.state["latest"] = time.time()
        launch(self.func, *self.args)

    def start(self):
        "start the timer"
        timer = threading.Timer(self.sleep, self.run)
        timer.name = self.name
        timer.daemon = True
        timer.sleep = self.sleep
        timer.state = self.state
        timer.state["starttime"] = time.time()
        timer.state["latest"] = time.time()
        timer.func = self.func
        timer.start()
        self.timer = timer
        return timer

    def stop(self):
        "stop the timer"
        if self.timer:
            self.timer.cancel()


class Repeater(Timer):

    "repeat job every x seconds"

    def run(self):
        "run the repeated job"
        thr = launch(self.start)
        super().run()
        return thr


def launch(func, *args, **kwargs):
    "run function with arguments in a thread"
    thrname = kwargs.get("name", name(func))
    thr = Thread(func, thrname, *args)
    thr.start()
    return thr
