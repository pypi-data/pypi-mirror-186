# This file is placed in the Public Domain


"scanner"


import inspect
import os


from bot.handler import Command
from bot.objects import spl


def __dir__():
    return (
            "scancmd",
            "scanpkg",
            "scandir"
           )


def include(name, namelist):
    "see if name in included in namelist"
    for nme in namelist:
        if nme in name:
            return True
    return False


def listmod(path):
    "list modules in a directory"
    res = []
    if not os.path.exists(path):
        return res
    for fnm in os.listdir(path):
        if fnm.endswith("~") or fnm.startswith("__"):
            continue
        res.append(fnm.split(os.sep)[-1][:-3])
    return res



def scancmd(mod):
    "scan a module for commands"
    for key, cmd in inspect.getmembers(mod, inspect.isfunction):
        if key.startswith("cb"):
            continue
        names = cmd.__code__.co_varnames
        if "event" in names:
            Command.add(cmd)


def scanpkg(pkg, func, mods=None):
    "scan a package using scandir"
    path = pkg.__path__[0]
    name = pkg.__name__
    return scandir(path, func, name, mods)


def scandir(path, func, pname=None, mods=None):
    "scan a directory applying a function to import the module"
    res = []
    if pname is None:
        pname = path.split(os.sep)[-1]
    for modname in listmod(path):
        if not modname:
            continue
        if mods and not include(modname, spl(mods)):
            continue
        mname = "%s.%s" % (pname, modname)
        ppath = os.path.join(path, "%s.py" % modname)
        mod = func(mname, ppath)
        if mod:
            res.append(mod)
    return res
