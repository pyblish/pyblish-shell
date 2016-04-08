#!/bin/bash

if [[ $TRAVIS_OS_NAME = 'osx' ]]; then
    brew update
    brew install qt55 python
    brew link --force qt55
    sip=/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/bin/sip

elif [[ $TRAVIS_OS_NAME = 'linux' ]]; then
    sudo apt-add-repository -y ppa:beineri/opt-qt551-trusty
    sudo apt-get update
    sudo apt-get install -y qt-latest
    source /opt/qt55/bin/qt55-env.sh
    sip=/usr/bin/sip
else
    echo $TRAVIS_OS_NAME not supported.
    exit 1
fi

wget http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/PyQt-gpl-5.5.1.tar.gz
wget http://sourceforge.net/projects/pyqt/files/sip/sip-4.17/sip-4.17.tar.gz

tar xvzf sip-4.17.tar.gz
cd sip-4.17
python configure.py
make
sudo make install
cd ..

tar xvzf PyQt-gpl-5.5.1.tar.gz
cd PyQt-gpl-5.5.1
python configure.py --sip=$sip --confirm-license
make
sudo make install
cd ..