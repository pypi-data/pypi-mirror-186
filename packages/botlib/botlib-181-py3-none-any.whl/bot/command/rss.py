# This file is placed in the Public Domain.


"rss commands"


import time


from bot.objects import Class, Db
from bot.objects import edit, find, fntime, printable, save
from bot.utility import elapsed


from bot.rss import Fetcher, Rss


def __dir__():
    return (
            "dpl",
            "ftc",
            "nme",
            "rem",
            "rss"
           )


def dpl(event):
    "rss items to display"
    if len(event.args) < 2:
        event.reply("dpl <stringinurl> <item1,item2>")
        return
    setter = {"display_list": event.args[1]}
    names = Class.full("rss")
    if names:
        feed = Db.last(names[0], {"rss": event.args[0]})
        if feed:
            edit(feed, setter)
            save(feed)
            event.done()


def ftc(event):
    "run a feed batch"
    res = []
    thrs = []
    fetcher = Fetcher()
    fetcher.start(False)
    thrs = fetcher.run()
    for thr in thrs:
        res.append(thr.join())
    if res:
        event.reply(",".join([str(x) for x in res if x]))
        return


def nme(event):
    "set name of a feed"
    if len(event.args) != 2:
        event.reply("name <stringinurl> <name>")
        return
    selector = {"rss": event.args[0]}
    got = []
    for feed in find("rss", selector):
        feed.name = event.args[1]
        got.append(feed)
    for feed in got:
        save(feed)
    event.done()


def rem(event):
    "remove a feed"
    if len(event.args) != 1:
        event.reply("rem <stringinurl>")
        return
    selector = {"rss": event.args[0]}
    for feed in find("rss", selector):
        feed.__deleted__ = True
        save(feed)
    event.done()


def rss(event):
    "add a feed"
    if not event.rest:
        nrs = 0
        for feed in find("rss"):
            event.reply("%s %s %s" % (
                                      nrs,
                                      printable(feed),
                                      elapsed(time.time() - fntime(feed.__fnm__)))
                                     )
            nrs += 1
        if not nrs:
            event.reply("no rss feed found.")
        return
    url = event.args[0]
    if "http" not in url:
        event.reply("i need an url")
        return
    dbs = Db()
    res = dbs.last("rss", {"rss": url})
    if res:
        event.reply("already got %s" % url)
        return
    feed = Rss()
    feed.rss = event.args[0]
    save(feed)
    event.done()
