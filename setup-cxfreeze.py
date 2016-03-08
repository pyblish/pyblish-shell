import os
from cx_Freeze import setup, Executable

PYQT5_DIR = r"C:\pythonpath\PyQt5"
print(os.path.join(PYQT5_DIR, "qml", "QtQuick.2"))
include_files = [
    "qml/",
    (os.path.join(PYQT5_DIR, "qml", "QtQuick.2"), "QtQuick.2"),
    (os.path.join(PYQT5_DIR, "qml", "QtQuick"), "QtQuick"),
    (os.path.join(PYQT5_DIR, "qml", "QtGraphicalEffects"), "QtGraphicalEffects"),
]

build_exe_options = {
    "includes": [
        "PyQt5.QtCore",
        "PyQt5.QtWidgets",
        "PyQt5.QtGui",
        "PyQt5.QtQml",
        "PyQt5.QtQuick",
        "PyQt5.QtNetwork",
        "PyQt5.QtOpenGL",
        "PyQt5.QtTest",
        "os",
        "__future__",
        "getpass",
        "ctypes",
        "contextlib",
        "logging",
        "ConfigParser",
        "xml.etree.ElementTree",
        "xmlrpclib",
        "SimpleXMLRPCServer",
        "json",
        "urllib2",
        "numbers",
    ],
    "excludes": [
        "Tkinter",
        "pyblish",
        "pyblish_qml",
        "pyblish_rpc",
    ],
    "include_files": include_files
}

setup(
    name="pyblish-shell",
    version="0.1",
    description="Pyblish Shell",
    options={"build_exe": build_exe_options},
    executables=[Executable("app.py")]
)
