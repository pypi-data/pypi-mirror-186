# This file is placed in the Public Domain.
# pylint: disable=C0115,C0116,C0411,C0413,W0212,R0903,W0201,E0402,W0613


"runtime"


import rlcompleter
import time


from .message import Event, Parsed
from .objects import Class, Default, update


def __dir__():
    return (
            "Cfg",
            "Console",
            "boot",
            "command",
            "parse",
            "setcompleter",
            "wait"
           )


class Completer(rlcompleter.Completer):

    def __init__(self, options):
        rlcompleter.Completer.__init__(self)
        self.matches = []
        self.options = options

    def complete(self, text, state):
        if state == 0:
            if text:
                self.matches = [
                                s for s in self.options
                                if s and s.startswith(text)
                               ]
            else:
                self.matches = self.options[:]
        try:
            return self.matches[state]
        except IndexError:
            return None



class Config(Default):

    pass


Class.add(Config)


Cfg = Config()
Cfg.prs = Parsed()


def boot(txt):
    prs = parse(txt)
    if "c" in prs.opts:
        Cfg.console = True
    if "d" in prs.opts:
        Cfg.daemon= True
    if "v" in prs.opts:
        Cfg.verbose = True
    if "w" in prs.opts:
        Cfg.wait = True
    if "x" in prs.opts:
        Cfg.exec = True
    update(Cfg.prs, prs)
    update(Cfg, prs.sets)


def command(cli, txt, event=None):
    evt = (event() if event else Event())
    evt.parse(txt)
    evt.orig = repr(cli)
    cli.handle(evt)
    evt.wait()
    return evt


def parse(txt):
    prs = Parsed()
    prs.parse(txt)
    update(Cfg.prs, prs)
    return prs


def wait(func=None):
    while 1:
        time.sleep(1.0)
        if func:
            func()
