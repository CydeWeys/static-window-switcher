#!/usr/bin/python3

import argparse
import subprocess

def syscall(*args):
  """ Helper method to make a syscall, check for errors, and return output as a string."""
  return subprocess.run(args, capture_output=True, check=True, text=True).stdout

# Parse args (accept exactly one of prev or next)
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-p", "--prev", help="switch to the previous window", action="store_true")
group.add_argument("-n", "--next", help="switch to the next window", action="store_true")
args = parser.parse_args()

# Get list of window handles from wmctrl and convert to decimal
windows_res = syscall("wmctrl", "-l")
windows = [str(int(s.partition(" ")[0], 16)) for s in windows_res.splitlines()]

# Get the current window handle
current_window = syscall("xdotool", "getwindowfocus").strip()

# Calculate the window handle to switch to and switch to it
step = 1 if args.next else -1
switch_to_window = windows[(windows.index(current_window) + step) % len(windows)]
syscall("xdotool", "windowactivate", switch_to_window)
