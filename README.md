# static-window-switcher
A statically ordered window switcher for X (Linux desktop).

If you've ever wanted shortcuts that navigate through your open windows in the
exact order that they appear in the task bar, then this is the program for you.
There's no annoying most recently used algorithm, just next (right) and previous
(left).

This program is written in Python3.  It should work in any Linux manager as it
uses low-level X primitives, but I've tested it in Gnome/Cinnamon.

## Install instructions

1. Clone this repo locally.
2. Create two new keyboard shortcuts in your window manager of choice as
   follows.  This should be somewhere in System Settings -> Keyboard.
    1. Next Window:  `python3 /path/to/static-window-switcher/switch.py -n`
    2. Prev Window:  `python3 /path/to/static-window-switcher/switch.py -p`
3. Assign keybindings to your new shortcuts.  Personally I'm using ` Alt-Tab `
   and `` Alt-` `` (you may need to unbind the existing shortcuts first).

That's it!
