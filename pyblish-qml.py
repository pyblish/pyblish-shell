#!/usr/bin/python

import os
import sys
import imp
import runpy

# Preserve PYTHONPATH, which is removed from sys.path by cx_Freeze
PYTHONPATH = os.environ.get("PYTHONPATH") or ""

for path in PYTHONPATH.split(os.pathsep):
    sys.path.insert(0, path)

if not imp.find_module("pyblish_qml"):
    sys.stderr.write("Could not find pyblish_qml on your path.")
    exit(1)

# Remove traces of cx_Freeze
if hasattr(sys, "frozen"):
    delattr(sys, "frozen")

runpy.run_module("pyblish_qml")
