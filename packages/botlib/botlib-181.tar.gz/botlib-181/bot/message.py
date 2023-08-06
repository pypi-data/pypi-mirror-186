# This file is placed in the Public Domain.
# pylint: disable=R0902,R0903


"message"


import threading
import time


from bot.objects import Class, Default, register
from bot.handler import Bus


def __dir__():
    return  (
             "Parsed",
             "Event",
            )


class Parsed(Default):


    "parsed object based of line of text"


    def __init__(self):
        Default.__init__(self)
        self.args = []
        self.cmd = ""
        self.gets = Default()
        self.opts = ""
        self.otxt = ""
        self.index = ""
        self.isparsed = False
        self.rest = ""
        self.sets = Default()
        self.toskip = Default()
        self.txt = ""

    def parse(self, txt=None):
        "parse with self.txt or provided txt"
        self.isparsed = True
        self.otxt = txt or self.txt
        spl = self.otxt.split()
        args = []
        _nr = -1
        for word in spl:
            if word.startswith("-"):
                try:
                    self.index = int(word[1:])
                except ValueError:
                    self.opts = self.opts + word[1:2]
                continue
            try:
                key, value = word.split("==")
                if value.endswith("-"):
                    value = value[:-1]
                    register(self.toskip, value, "")
                register(self.gets, key, value)
                continue
            except ValueError:
                pass
            try:
                key, value = word.split("=")
                register(self.sets, key, value)
                continue
            except ValueError:
                pass
            _nr += 1
            if _nr == 0:
                self.cmd = word
                continue
            args.append(word)
        if args:
            self.args = args
            self.rest = " ".join(args)
            self.txt = self.cmd + " " + self.rest
        else:
            self.txt = self.cmd


Class.add(Parsed)


class Event(Parsed):


    "parsed event"


    def __init__(self):
        Parsed.__init__(self)
        self.__ready__ = threading.Event()
        self.__thr__ = None
        self.control = "!"
        self.createtime = time.time()
        self.result = []
        self.type = "event"

    def bot(self):
        "return originating bot"
        return Bus.byorig(self.orig)

    def error(self):
        "silence error"

    def done(self, txt=None):
        "reply with ok"
        text = "ok " + (txt or "")
        text = text.rstrip()
        Bus.say(self.orig, self.channel, text)

    def ready(self):
        "flag event as ready"
        self.__ready__.set()

    def reply(self, txt):
        "add add txt to the result"
        self.result.append(txt)

    def show(self):
        "show result"
        for txt in self.result:
            Bus.say(self.orig, self.channel, txt)

    def wait(self):
        "wait for event to finish"
        if self.__thr__:
            self.__thr__.join()
        self.__ready__.wait()


Class.add(Event)
