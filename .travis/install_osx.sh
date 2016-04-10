#!/bin/bash

brew update
brew install qt55
brew link --force qt55

echo "Python version: $(python --version)"
echo "Python dir: $(python -c 'import sys;print(sys.executable)')"

export QT_ROOT=/usr/local/opt/qt55
export SIP=/System/Library/Frameworks/Python.framework/Versions/2.7/bin/sip
