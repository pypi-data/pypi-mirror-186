README
######


**NAME**

| ``OPERBOT - write your own commands``
|

**SYNOPSIS**

| ``operbot [-c|-d|-h]``
| ``operbot <cmd> [key=value] [key==value]``
|


**DESCRIPTION**


``OPERBOT`` is a bot, intended to be programmable, with a client program to
develop modules on and a systemd version with code included to run a 24/7
presence in a channel. 

``OPERBOT`` stores it's data on disk where objects are time versioned and the
last version saved on disk is served to the user layer. Files are JSON dumps
that are read-only so thus should provide (disk) persistence. Paths carry the
type in the path name what makes reconstruction from filename easier then
reading type from the object.

``OPERBOT`` has some functionality, mostly feeding RSS feeds into a irc
channel. It can do some logging of txt and take note of things todo.


**INSTALL**

| ``pip3 install operbot``
|

**CONFIGURATION**

| configuration is done by calling the ``icfg`` command of ``operbot``
| 

**irc**

| ``operbot icfg server=<server> channel=<channel> nick=<nick>``
|
| (*) default channel/server is #operbot on localhost
|

**sasl**

| ``operbot pwd <nickservnick> <nickservpass>``
| ``operbot icfg password=<outputfrompwd>``
|

**users**

as default the user's userhost is checked when a user types a command in a
channel. To add a user to the bot use the met command:

| ``operbot met <userhost>``
|

to delete a user use the del command with a substring of the userhost:

| ``operbot del <substring>``
|

to disable userhost checking disable users with the ``icfg`` command:

| ``operbot icfg users=False``
|

**rss**


| ``operbot rss <url>``
|


**RUNNING**

| this part shows how to run ``operbot``.
|


**cli**

without any arguments ``operbot`` doesn't respond, add arguments to have
``operbot`` execute a command:

| ``$ operbot``
| ``$``
|

the ``cmd`` command shows you a list of available commands:

| ``$ operbot cmd``
| ``cfg,cmd,dlt,dpl,flt,fnd,ftc,icfg,met,mre,nme,pwd,rem,rss,thr,upt``
|

**console**

| use the -c option to start the bot as a console.
|
| ``$ operbot -c mod=irc,rss,cmd``
| ``OPERBOT started at Fri Jan 6 01:49:58 2023 version=111 console=True mod=irc,rss,cmd``
| ``> cmd``
| ``cmd,dlt,dpl,flt,ftc,icfg,log,met,mre,nme,pwd,rem,rss,thr,upt``
| ``>``
|

running the bot in the background is done with the -d option.

| ``$ operbot -d``
| ``$``
|

the bot has a -h option to show a short help message.

| ``operbot [-c|-d|-h] [cfg|cmd|fnd|dlt|icfg|met|mre|pwd|dpl|ftc|nme|rem|rss|flt|thr|upt]``
|
| ``-h show help``
| ``-c start console``
| ``-d daemonize``
|

**COMMANDS**


| here is a short description of the commands.
|
| ``icfg`` - show the irc configuration, also edits the config
| ``cmd`` - show all commands
| ``dlt`` - remove a user
| ``dne`` - flag todo as done
| ``dpl`` - set display items for a rss feed
| ``flt`` - show a list of bot registered to the bus
| ``fnd`` - allow you to display objects on the datastore, read-only json files on disk 
| ``ftc`` - run a rss feed fetching batch
| ``log`` - log some text
| ``met`` - add a users with there irc userhost
| ``mre`` - displays cached output, channel wise.
| ``nme`` - set name of a rss feed
| ``pwd`` - combine a nickserv name/password into a sasl password
| ``rem`` - remove a rss feed by matching is to its url
| ``rss`` - add a feed to fetch, fetcher runs every 5 minutes
| ``thr`` - show the running threads
| ``tdo`` - adds a todo item, no options returns list of todo's
| ``upt`` - show uptime
| ``ver`` - show version
|


**PROGRAMMING**


The ``opr`` package provides an Object class, that mimics a dict while using
attribute access and provides a save/load to/from json files on disk.
Objects can be searched with database functions and uses read-only files
to improve persistence and a type in filename for reconstruction. Methods are
factored out into functions to have a clean namespace to read JSON data into.

basic usage is this::

 >>> from opr import Object
 >>> o = Object()
 >>> o.key = "value"
 >>> o.key
 >>> 'value'

Objects try to mimic a dictionary while trying to be an object with normal
attribute access as well. hidden methods are provided, the methods are
factored out into functions like get, items, keys, register, set, update
and values.

load/save from/to disk::

 >>> from opr import Object, load, save
 >>> o = Object()
 >>> o.key = "value"
 >>> p = save(o)
 >>> obj = Object()
 >>> load(obj, p)
 >>> obj.key
 >>> 'value'

great for giving objects peristence by having their state stored in files::

 >>> from opr import Object, save
 >>> o = Object()
 >>> save(o)
 opr.objects.Object/89efa5fd7ad9497b96fdcb5f01477320/2022-11-21/17:20:12.221192


**SYSTEMD**


to run the bot after reboot, install the service file and start the service
by enabling it with ``--now``::

 $ ``sudo systemctl enable /usr/local/operbot/operbot.service  --now``

 (*) default channel/server is #operbot on localhost

 use ``operbotctl`` instead of the use ``operbot`` program

 $ ``sudo operbotctl cfg server=<server> channel=<channel> nick=<nick>``
 $ ``sudo operbotctl pwd <nickservnick> <nickservpass>``
 $ ``sudo operbotctl cfg password=<outputfrompwd>``
 $ ``sudo operbotctl cfg users=True``
 $ ``sudo operbotctl met <userhost>``
 $ ``sudo operbotctl rss <url>``


**AUTHOR**


Bart Thate - operbot100@gmail.com


**COPYRIGHT**


``operbot`` is placed in the Public Domain.
