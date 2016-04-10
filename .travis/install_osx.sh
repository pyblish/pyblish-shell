#!/bin/bash

brew update
brew install qt55 python
brew link --force qt55

echo /usr/local/opt/qt55 >> QT_ROOT
echo /usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/bin/sip >> SIP