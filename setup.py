#!/usr/bin/python

import os
import json
import PyQt5
import shutil

from cx_Freeze import setup, Executable

with open("includes.json") as f:
    includes = json.load(f)

# Cleanup
try:
    shutil.rmtree(
        os.path.join(
            os.path.dirname(__file__), "build"))
except OSError as e:
    if e.errno != 2:
        # Could not remove
        raise e
    pass  # Already removed

excludes = [
   "Tkinter",
]

PYQT5_DIR = os.path.join(os.path.dirname(PyQt5.__file__), "qml")
include_files = [
    (os.path.join(PYQT5_DIR, "QtQuick.2"), "QtQuick.2"),
    (os.path.join(PYQT5_DIR, "QtQuick"), "QtQuick"),
    (os.path.join(PYQT5_DIR, "QtGraphicalEffects"), "QtGraphicalEffects"),
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
            "build_exe": "build/pyblish-shell",
            "compressed": True,
        }
    },
    executables=[
        Executable(
            "app.py",
            targetName="pyblish-shell" + ".exe" if os.name == "nt" else "",
            icon="icon.ico",
            targetDir="build/pyblish-shell",
            compress=True,
        ),
        Executable(
            "pyblish-qml.py",
            icon="icon.ico",
            targetDir="build/pyblish-shell",
            compress=True
        )
    ]
)
