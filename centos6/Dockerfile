FROM        centos:6.7
MAINTAINER  Marcus Ottosson <marcus@abstractfactory.io>

RUN yum install -y wget

# ADD doesn't like these links, so we use wget
RUN wget -O sip.tar.gz http://sourceforge.net/projects/pyqt/files/sip/sip-4.17/sip-4.17.tar.gz && \
    wget -O pyqt.tar.gz http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/PyQt-gpl-5.5.1.tar.gz && \
    wget -O qt.tar.gz http://download.qt.io/official_releases/qt/5.5/5.5.1/single/qt-everywhere-opensource-src-5.5.1.tar.gz

RUN yum update -y && \
    yum groupinstall -y "Development Tools" && \
    yum install -y \
      perl \
      git \
      tar \
      python27 \
      python-devel \
      mesa-libGL-devel

RUN mkdir /src && \
    tar -xvf qt.tar.gz -C /src && \
    tar -xf sip.tar.gz -C /src && \
    tar -xf pyqt.tar.gz -C /src && \
    mv /src/qt-everywhere-opensource-src-5.5.1 /src/qt && \
    mv /src/sip-4.17 /src/sip && \
    mv /src/PyQt-gpl-5.5.1 /src/pyqt

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

RUN scl enable python27 "\
    cd /src/sip && \
    python configure.py && \
    make && \
    make install"

RUN scl enable python27 "\
    cd /src/pyqt && \
    python configure.py \
      --confirm-license \
      --qmake /usr/local/Qt/bin/qmake \
      --sip /usr/bin/sip && \
    make && \
    make install"
