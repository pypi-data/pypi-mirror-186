# This file is placed in the Public Domain.


"list bots"


from bot.handler import Bus
from bot.threads import name


def __dir__():
    return (
            'flt',
           )


def flt(event):
    "list of bots"
    try:
        index = int(event.args[0])
        event.reply(Bus.objs[index])
        return
    except (KeyError, TypeError, IndexError, ValueError):
        pass
    event.reply(" | ".join([name(o) for o in Bus.objs]))
