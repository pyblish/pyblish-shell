# cx_Freeze should have made these links by itself,
# but for some reason it wont. We rectify this here.
#
# It shouldn't cause trouble if at some point cx_Freeze
# does the right thing.

sudo chmod u+w build/QtGui && \
    install_name_tool -change "$QT_ROOT/lib/QtWidgets.framework/Versions/5/QtWidgets"   "./QtWidgets"   build/PyQt5.QtWidgets.so && \
    install_name_tool -change "$QT_ROOT/lib/QtGui.framework/Versions/5/QtGui"           "./QtGui"       build/PyQt5.QtWidgets.so && \ 
    install_name_tool -change "$QT_ROOT/lib/QtCore.framework/Versions/5/QtCore"         "./QtCore"      build/PyQt5.QtWidgets.so && \ 
    install_name_tool -change "$QT_ROOT/lib/QtCore.framework/Versions/5/QtCore"         "./QtCore"      build/PyQt5.QtCore.so && \
    install_name_tool -change "$QT_ROOT/lib/QtWidgets.framework/Versions/5/QtWidgets"   "./QtWidgets"   build/PyQt5.QtGui.so && \
    install_name_tool -change "$QT_ROOT/lib/QtGui.framework/Versions/5/QtGui"           "./QtGui"       build/PyQt5.QtGui.so && \
    install_name_tool -change "$QT_ROOT/lib/QtCore.framework/Versions/5/QtCore"         "./QtCore"      build/PyQt5.QtGui.so && \
    install_name_tool -change "$QT_ROOT/lib/QtQuick.framework/Versions/5/QtQuick"       "./QtQuick"     build/PyQt5.QtQuick.so && \
    install_name_tool -change "$QT_ROOT/lib/QtGui.framework/Versions/5/QtGui"           "./QtGui"       build/PyQt5.QtQuick.so && \
    install_name_tool -change "$QT_ROOT/lib/QtCore.framework/Versions/5/QtCore"         "./QtCore"      build/PyQt5.QtQuick.so && \
    install_name_tool -change "$QT_ROOT/lib/QtQml.framework/Versions/5/QtQml"           "./QtQml"       build/PyQt5.QtQuick.so && \
    install_name_tool -change "$QT_ROOT/lib/QtNetwork.framework/Versions/5/QtNetwork"   "./QtNetwork"   build/PyQt5.QtQuick.so && \
    install_name_tool -change "$QT_ROOT/lib/QtNetwork.framework/Versions/5/QtNetwork"   "./QtNetwork"   build/PyQt5.QtNetwork.so && \
    install_name_tool -change "$QT_ROOT/lib/QtCore.framework/Versions/5/QtCore"         "./QtCore"      build/PyQt5.QtNetwork.so && \
    install_name_tool -change "$QT_ROOT/lib/QtGui.framework/Versions/5/QtGui"           "./QtGui"       build/PyQt5.QtQml.so && \
    install_name_tool -change "$QT_ROOT/lib/QtCore.framework/Versions/5/QtCore"         "./QtCore"      build/PyQt5.QtQml.so && \
    install_name_tool -change "$QT_ROOT/lib/QtQml.framework/Versions/5/QtQml"           "./QtQml"       build/PyQt5.QtQml.so && \
    install_name_tool -change "$QT_ROOT/lib/QtNetwork.framework/Versions/5/QtNetwork"   "./QtNetwork"   build/PyQt5.QtQml.so && \
    install_name_tool -change "$QT_ROOT/lib/QtWidgets.framework/Versions/5/QtWidgets"   "./QtWidgets"   build/PyQt5.QtTest.so && \
    install_name_tool -change "$QT_ROOT/lib/QtGui.framework/Versions/5/QtGui"           "./QtGui"       build/PyQt5.QtTest.so && \
    install_name_tool -change "$QT_ROOT/lib/QtTest.framework/Versions/5/QtTest"         "./QtTest"      build/PyQt5.QtTest.so && \
    echo "Relinking successful" || exit 1
