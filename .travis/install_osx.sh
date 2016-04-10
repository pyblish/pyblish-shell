#!/bin/bash

brew update
brew install qt55 python
brew link --force qt55

echo export QT_ROOT=/usr/local/opt/qt55 >> POST_COMMAND
echo export SIP=/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/bin/sip >> POST_COMMAND
