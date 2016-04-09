SIP=""
export QT_ROOT=""

echo "Evaluating OS.."
if [[ $TRAVIS_OS_NAME = 'osx' ]]; then
    echo "Building in OSX"

    brew update
    brew install qt55 python
    brew link --force qt55

    export QT_ROOT=/usr/local/opt/qt55
    SIP=/usr/local/Cellar/python/2.7.11/Frameworks/Python.framework/Versions/2.7/bin/sip

elif [[ $TRAVIS_OS_NAME = 'linux' ]]; then
    echo "Building in Linux"

    sudo apt-add-repository -y ppa:beineri/opt-qt551
    sudo apt-get update
    sudo apt-get install -y qt-latest
    source /opt/qt55/bin/qt55-env.sh

    export QT_ROOT=/opt/qt55
    SIP=/usr/bin/sip

else
    echo $TRAVIS_OS_NAME not supported.
    exit 1
fi