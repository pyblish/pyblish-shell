#!/usr/bin/env python
import os
import sys
import json
import PyQt5
import shutil

from cx_Freeze import setup, Executable

dst = os.path.join(os.path.dirname(__file__), "build")

print("Cleaning exe directory..")
if os.path.exists(dst):
    try:
        shutil.rmtree(dst)
    except:
        sys.stderr.write("Could not remove build directory")
        exit(1)

qmldir = os.path.join(os.path.dirname(PyQt5.__file__), "qml")
include_files = [
    (os.path.join(qmldir, "QtQuick.2"), "QtQuick.2"),
    (os.path.join(qmldir, "QtQuick"), "QtQuick"),
    (os.path.join(qmldir, "QtGraphicalEffects"), "QtGraphicalEffects"),
]

with open("includes.json") as f:
    includes = json.load(f)

excludes = [
   "Tkinter",
]

setup(
    name="pyblish-shell",
    version="1.0",
    description="Pyblish Shell",
    options={
        "build_exe": {
            "includes": includes,
            "excludes": excludes,
            "include_files": include_files,
            "include_msvcr": True,
            "build_exe": "build",
            "compressed": True,
        }
    },
    executables=[
        Executable(
            "app.py",
            targetName="pyblish-shell" + ".exe" if os.name == "nt" else "",
            icon="icon.ico",
            targetDir="build",
            compress=True,
        ),
        Executable(
            "pyblish-qml.py",
            icon="icon.ico",
            targetDir="build",
            compress=True
        )
    ]
)
