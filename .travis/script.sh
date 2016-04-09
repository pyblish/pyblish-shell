if [[ $TRAVIS_OS_NAME = 'osx' ]]; then
    export QT_ROOT=/usr/local/opt/qt55

elif [[ $TRAVIS_OS_NAME = 'linux' ]]; then
    export QT_ROOT=/opt/qt55

else
    echo $TRAVIS_OS_NAME not supported.
    exit 1
fi

bash -e build-exe.sh
bash -e build-installer.sh $TRAVIS_OS_NAME

echo "Finished script.sh"