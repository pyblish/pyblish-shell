#!/usr/bin/env python
import os
import sys
import json
import PyQt5
import shutil

print("PyQt5 path: %s" % PyQt5.__file__)

dst = os.path.join(os.path.dirname(__file__), "build")

print("Cleaning exe directory..")
if os.path.exists(dst):
    try:
        shutil.rmtree(dst)
    except:
        sys.stderr.write("Could not remove build directory")
        exit(1)

qmldir = (os.environ.get("QML_ROOT") or 
          os.path.join(os.path.dirname(PyQt5.__file__), "qml"))

print("QML_ROOT: %s" % qmldir)

include_files = [
    (os.path.join(qmldir, "QtQuick.2"), "QtQuick.2"),
    (os.path.join(qmldir, "QtQuick"), "QtQuick"),
    (os.path.join(qmldir, "QtGraphicalEffects"), "QtGraphicalEffects"),
    "pyblish_qml.bat",  # Windows
    "pyblish_tray.bat",
    "pyblish_qml",  # Unix
    "pyblish_tray",
]

with open("includes.json") as f:
    includes = json.load(f)

excludes = [
   "Tkinter",
]

# Test include availability
missing = list()
for module in includes:
    try:
        __import__(module, globals={}, locals={})
    except ImportError:
        missing.append(module)
    except Exception:
        pass  # Exists, but throws an error on import

if missing:
    sys.stderr.write("There were missing modules\n")
    for module in missing:
        sys.stderr.write("- %s\n" % module)
    exit(1)

# Important to import after above test
from cx_Freeze import setup, Executable
from pyblish_shell import version

setup(
    name="pyblish-shell",
    version=version,
    description="Pyblish Shell",
    options={
        "build_exe": {
            "includes": includes,
            "excludes": excludes,
            "include_files": include_files,
            "include_msvcr": True,
            "build_exe": os.path.abspath("build"),
            "compressed": True,
        }
    },
    executables=[
        Executable(
            "pyblish_shell.py",
            icon="icon.ico",
            targetDir="build",
            base="Console",
        ),
    ]
)
