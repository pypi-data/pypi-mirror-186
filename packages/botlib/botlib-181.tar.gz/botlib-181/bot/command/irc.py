# This file is placed in the Public Domain.


"internet relay chat"


import base64


from bot.objects import edit, keys, last, printable, save

from bot.irc import Config


def __dir__():
    return (
            "icfg",
            "mre",
            "pwd"
           )


def icfg(event):
    "irc config"
    config = Config()
    last(config)
    if not event.sets:
        event.reply(printable(
                              config,
                              keys(config),
                              skip="control,password,realname,sleep,username")
                             )
    else:
        edit(config, event.sets)
        save(config)
        event.ok()


def mre(event):
    "more text"
    if not event.channel:
        event.reply("channel is not set.")
        return
    bot = event.bot()
    if "cache" not in dir(bot):
        event.reply("bot is missing cache")
        return
    if event.channel not in bot.cache:
        event.reply("no output in %s cache." % event.channel)
        return
    for _x in range(3):
        txt = bot.gettxt(event.channel)
        if txt:
            bot.say(event.channel, txt)
    size = bot.size(event.channel)
    event.reply("%s more in cache" % size)


def pwd(event):
    "create sasl password"
    if len(event.args) != 2:
        event.reply("pwd <nick> <password>")
        return
    txt = "\x00%s\x00%s" % (event.args[0], event.args[1])
    enc = txt.encode("ascii")
    base = base64.b64encode(enc)
    dcd = base.decode("ascii")
    event.reply(dcd)
