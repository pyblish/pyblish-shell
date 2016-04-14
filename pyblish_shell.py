#!/usr/bin/env python
import os
import sys
import code
import runpy
import argparse
import subprocess

version = "1.1.2"

# Preserve PYTHONPATH, which is removed from sys.path by cx_Freeze
PYTHONPATH = os.environ.get("PYTHONPATH") or ""

for path in PYTHONPATH.split(os.pathsep):
    sys.path.insert(0, path)

# Remove traces of cx_Freeze
if hasattr(sys, "frozen"):
    delattr(sys, "frozen")

# Message for interactive interpreter
banner = (
    'Python 2.7.10 (pyblish, May 23 2015, 09:44:00) '
    '[MSC v.1500 64 bit (AMD64)] on win32\n'
    'Type "help", "copyright", "credits" or "license" '
    'for more information.'
)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Customised Python shell for Pyblish")

    parser.add_argument("file", nargs='*')
    parser.add_argument("--command", "-c")
    parser.add_argument("--unbuffered", "-u", action="store_true")
    parser.add_argument("--module", "-m", nargs=argparse.REMAINDER)
    parser.add_argument("--version", action="store_true")
    parser.add_argument("--background", action="store_true")

    args, extras = parser.parse_known_args()

    if args.unbuffered or os.environ.get("PYTHONUNBUFFERED"):
        sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)
        sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
        sys.stderr = os.fdopen(sys.stderr.fileno(), 'w', 0)

    if args.version:
        print(version)

    elif args.background:
        args = [sys.executable] + sys.argv[1:]
        args.remove("--background")
        CREATE_NO_WINDOW = 0x08000000
        subprocess.Popen(args,
                         creationflags=CREATE_NO_WINDOW,
                         stdout=open("log.txt", "a"),
                         stderr=subprocess.STDOUT)

    elif args.file:
        sys.argv.pop(0)
        runpy.run_path(args.file[0])

    elif not (args.command or args.module):
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
