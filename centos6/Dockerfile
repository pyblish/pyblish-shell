FROM        centos:6.7
MAINTAINER  Marcus Ottosson <marcus@abstractfactory.io>

ADD http://sourceforge.net/projects/pyqt/files/sip/sip-4.17/sip-4.17.tar.gz ~/sip.tar.gz
ADD http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/PyQt-gpl-5.5.1.tar.gz ~/pyqt.tar.gz
ADD http://download.qt.io/official_releases/qt/5.5/5.5.1/single/qt-everywhere-opensource-src-5.5.1.tar.gz ~/qt.tar.gz

RUN yum update && \
    yum groupinstall "C Development Tools and Libraries" && \
    yum install -y \
      perl \
      tar \
      git \
      wget \
      python-devel \
      mesa-libGL-devel

RUN mkdir /src && \
    cd /src && \
    tar -xvf ~/qt.tar.gz && \
    tar -xf sip.tar.gz && \
    tar -xf pyqt.tar.gz && \
    mv /src/qt-everywhere-opensource-src-5.5.1 /src/qt

RUN cd /src/qt && \
  ./configure \
    -confirm-license \
    -opensource \
    -nomake examples \
    -nomake tests \
    -no-compile-examples \
    -no-xcb \
    -prefix "/usr/local/Qt" && \
  cd /src/qt && \
  make -j4 all && \
  make install

RUN cd /src/sip-4.17 && \
    python configure.py && \
    make && \
    make install

RUN cd /src/PyQt-gpl-5.5.1 && \
    python configure.py \
      --confirm-license \
      --qmake /usr/local/Qt/bin/qmake \
      --sip /usr/bin/sip && \
    make && \
    make install && \
    cd ..