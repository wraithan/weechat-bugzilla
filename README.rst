Bugzilla
========

Weechat script that links to bugzilla bugs::

    17:51:59 Wraithan | We should really look into bug 800000 some more.
    17:51:59          | [http://bugzil.la/800000]

I plan to add the ability for the script to look up bugs and get summary/status
like firebot, since firebot isn't always around, but that is in the future,
right now linking is better than nothing.

Installation
------------

You can install it using the ``/script`` command like so::

    /script install bugzilla.py

As of time of writing the script is pending approval, you'll need to use the
manual installation below if the above command fails.

Manual Installation
-------------------

Copy ``bugzilla.py`` into ``~/.weechat/python`` then in weechat run::

    /python load bugzilla.py

If you want the script to load every time you start weechat, symlink into the
autoload directory like this::

    ln -s ~/.weechat/python/{,autoload/}bugzilla.py
