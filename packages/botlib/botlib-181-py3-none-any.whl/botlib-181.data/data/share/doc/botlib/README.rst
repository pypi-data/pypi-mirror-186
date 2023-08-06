**NAME**

BOTLIB - The Python3 ``bot`` Namespace


**SYNOPSIS**


``bot [-c] [mod=mod1,mod2]``
``bot <cmd> [key=value] [key==value]``


**DESCRIPTION**

BOTLIB is a package providing the ``bot`` namespace package. The tarball
provided a bot binary as a demo, the package itself only installs the
bot package.

``bot`` is a solid, non hackable bot, that runs under systemd as a 24/7
background service and starts the bot after reboot, intended to be
programmable in a static, only code, no popen, no imports and no reading
modules from a directory.

``bot`` is programmable, to program the bot you have to have the code
available as employing your own code requires that you install your own bot as
the system bot. This is to not have a directory to read modules from to add
commands to the bot but include the own programmed modules directly into the
python code, so only trusted code (your own written code) is included and
runnable. Reading random code from a directory is what gets avoided. As
experience tells os.popen and __import__, importlib are also avoided. 

BOTLIB stores it's data on disk where objects are time versioned and the
last version saved on disk is served to the user layer. Files are JSON dumps
that are read-only so thus should provide (disk) persistence more chance.
Paths carry the type in the path name what makes reconstruction from filename
easier then reading type from the object.

Only include your own written code should be the path to "secure".


**INSTALL**

|
| ``pip3 install botlib --upgrade --force-reinstall``
|

**CONFIGURATION**

configuration is done by calling the ``cfg`` command of the bot.
|

*irc*

|
| ``bot cfg server=<server> channel=<channel> nick=<nick>``
|
| (*) default channel/server is #botlib on localhost
|

*sasl*

|
| ``bot pwd <nickservnick> <nickservpass>``
| ``bot cfg password=<outputfrompwd>``
|

*users*


|
| ``bot cfg users=True``
| ``bot met <userhost>``
|

*rss*

|
| ``bot rss <url>``
|

**RUNNING**

this part shows how to run the client ``bot`` version of botlib.

*cli*

without any arguments the bot doesn't respond, add arguments to have the bot execute a
command.

| ``$ bot cmd``
| ``cfg,cmd,dlt,dne,dpl,flt,fnd,ftc,log,met,mre,nme,pwd,rem,rss,tdo,thr,ver``
|

*console*

use the -c option to start the bot as a console.

| ``$ bot -c``
| ``BOT start at Fri Apr 1 20:02:40 2022``
| ``> thr``
| ``Console.loop(1s) thr(1s)``
| ``>`` 
|

*irc*


| ``$ bot``
| ``BOT start at Fri Apr 1 20:00:43 2022``
| ``server=localhost port=6667 channel=#botlib nick=botlib cc=!``
| ``> thr``
| ``Console.loop/8s IRC.keep/8s IRC.loop/8s IRC.output/8s thr/8s``
| ``>`` 
|

**COMMANDS**

the bot has the following commands.

|
| ``$ bot cmd``
| ``cfg,cmd,dlt,dne,dpl,flt,fnd,ftc,met,mre,nme,pwd,rem,rss,thr,upt,ver``
|

here is a short description of the commands.

|
| ``cfg`` - shows the irc configuration, also edits the config
| ``cmd`` - shows all commands
| ``dlt`` - removes a user from bot
| ``dne`` - flag todo as done
| ``dpl`` - sets display items for a rss feed
| ``flt`` - shows a list of bot registered to the bus
| ``fnd`` - allows you to display objects on the datastore, read-only json files on disk 
| ``ftc`` - runs a rss feed fetching batch
| ``log`` - logs some text
| ``met`` - adds a users with there irc userhost
| ``mre`` - displays cached output, channel wise.
| ``nme`` - set name of a rss feed
| ``pwd`` - combines a nickserv name/password into a sasl password
| ``rem`` - removes a rss feed by matching is to its url
| ``rss`` - adds a feed to fetch, fetcher runs every 5 minutes
| ``thr`` - show the running threads
| ``tdo`` - adds a todo item, no options returns list of todo's
| ``upt`` - show uptime
| ``ver`` - show version
|


**AUTHOR**

Bart Thate


**COPYRIGHT**

BOTLIB is placed in the Public Domain. No Copyright, No License.
