#!/usr/bin/python

import os
import sys
import code
import runpy
import argparse

# Preserve PYTHONPATH, which is removed from sys.path by cx_Freeze
PYTHONPATH = os.environ.get("PYTHONPATH") or ""

for path in PYTHONPATH.split(os.pathsep):
    sys.path.insert(0, path)

# Remove traces of cx_Freeze
if hasattr(sys, "frozen"):
    delattr(sys, "frozen")

# Message for interactive interpreter
banner = (
    'Pyblish 2.7.10 (default, May 23 2015, 09:44:00) '
    '[MSC v.1500 64 bit (AMD64)] on win32\n'
    'Type "help", "copyright", "credits" or "license" '
    'for more information.'
)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Customised Python shell for Pyblish")

    parser.add_argument("--command", "-c")
    parser.add_argument("--module", "-m", nargs=argparse.REMAINDER)

    args = parser.parse_args()

    if not (args.command or args.module):
        globenv = {k: v for k, v in globals().items()
                   if k.startswith("_")}
        cons = code.InteractiveConsole(locals=globenv)
        cons.interact(banner)

    elif args.command:
        exec args.command

    elif args.module:
        module = args.module.pop(0)
        sys.argv[1:] = args.module
        runpy.run_module(module,
                         alter_sys=True,
                         run_name='__main__')
