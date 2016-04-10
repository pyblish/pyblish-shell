#!/bin/bash

brew update
brew install qt55
brew link --force qt55

export QT_ROOT=/usr/local/opt/qt55
export SIP=/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/bin/sip
