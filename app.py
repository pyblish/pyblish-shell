import os
import sys

from PyQt5 import (
    QtGui,
    QtCore,
    QtQml,
    QtQuick
)

PYTHONPATH = os.environ.get("PYTHONPATH") or ""

print("PYTHONPATH: %s" % PYTHONPATH)
for path in sys.path:
    print path

for path in PYTHONPATH.split(os.pathsep):
    sys.path.insert(0, path)

print("Running app..")
import pyblish_qml.app
pyblish_qml.app.main(debug=True, validate=False)

__all__ = [
    "QtGui",
    "QtCore",
    "QtQml",
    "QtQuick",
]
