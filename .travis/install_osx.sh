#!/bin/bash

brew update
brew install qt55 tree
brew link --force qt55

# Debug info
python --version
echo "Python dir: $(python -c 'import sys;print(sys.executable)')"

export QT_ROOT=/usr/local/Cellar/qt55
export SIP=/System/Library/Frameworks/Python.framework/Versions/2.7/bin/sip

echo "Qt install: $QT_ROOT"
tree $QT_ROOT

echo "Qt Cellar: /usr/local/Cellar/qt55/"
tree /usr/local/Cellar/qt55/