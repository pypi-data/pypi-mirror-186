# This file is placed in the Public Domain.


"config"


from bot.objects import edit, keys, last, printable, write
from bot.runtime import Cfg


def __dir__():
    return (
            "cfg",
           )


def cfg(event):
    "runtime configuration"
    last(Cfg)
    if not Cfg.prs.txt:
        event.reply("config is empty")
        return
    if not event.sets:
        event.reply(printable(
                              Cfg,
                              keys(Cfg),
                              skip="name,password,prs",
                             )
                   )
    else:
        edit(Cfg, event.sets)
        write(Cfg)
        event.done()
