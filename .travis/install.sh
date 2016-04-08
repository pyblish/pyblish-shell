# Build Pyblish Shell for OSX

if [ "$TRAVIS_OS_NAME" = "osx"]
then
    brew update
    brew install qt55 python
    brew link --force qt55
else
    echo "$TRAVIS_OS_NAME not supported"
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

if [ "$TRAVIS_OS_NAME" = "osx"]
then
    python configure.py --sip=/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/bin/sip --confirm-license
else
    echo "$TRAVIS_OS_NAME not supported"
    exit 1
fi

make
sudo make install
cd ..