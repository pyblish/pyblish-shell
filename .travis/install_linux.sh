#!/bin/bash

sudo apt-add-repository -y ppa:beineri/opt-qt551
sudo apt-get update
sudo apt-get install -y qt-latest

echo source /opt/qt55/bin/qt55-env.sh >> POST_COMMAND

echo export QT_ROOT=/opt/qt55 >> POST_COMMAND
echo export SIP=/usr/bin/sip >> POST_COMMAND

