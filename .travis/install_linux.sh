#!/bin/bash

sudo apt-add-repository -y ppa:beineri/opt-qt551
sudo apt-get update
sudo apt-get install -y qt-latest
source /opt/qt55/bin/qt55-env.sh

echo /opt/qt55 >> QT_ROOT
echo /usr/bin/sip >> SIP
