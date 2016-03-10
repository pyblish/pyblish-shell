FROM        centos:6.7
MAINTAINER  Marcus Ottosson <marcus@abstractfactory.io>

RUN yum update -y && \
    yum groupinstall -y "C Development Tools and Libraries" && \
    yum install -y \
      perl \
      tar \
      git \
      wget \
      python27 \
      python-devel \
      mesa-libGL-devel

# ADD doesn't like these links, so we use wget
RUN wget -O sip.tar.gz http://sourceforge.net/projects/pyqt/files/sip/sip-4.17/sip-4.17.tar.gz && \
    wget -O pyqt.tar.gz http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/PyQt-gpl-5.5.1.tar.gz && \
    wget -O qt.tar.gz http://download.qt.io/official_releases/qt/5.5/5.5.1/single/qt-everywhere-opensource-src-5.5.1.tar.gz

RUN mkdir /src && \
    tar -xvf -C /src qt.tar.gz && \
    tar -xf -C /src sip.tar.gz && \
    tar -xf -C /src pyqt.tar.gz && \
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

RUN scl enable python27 " \
    cd /src/sip-4.17 && \
    python configure.py && \
    make && \
    make install"

RUN scl enable python27 " && \
    cd /src/PyQt-gpl-5.5.1 && \
    python configure.py \
      --confirm-license \
      --qmake /usr/local/Qt/bin/qmake \
      --sip /usr/bin/sip && \
    make && \
    make install"
