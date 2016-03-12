# Compile dependencies and build pyblish-shell for Centos 6.7
# Produce output in current working directory.
#
# Usage:
#   $ git clone https://github.com/pyblish/pyblish-shell.git
#   $ cd pyblish-shell
#   $ docker run -ti --rm -v $(pwd):/root mottosso/pyblish-shell-centos6.7 build-exe.sh

FROM        centos:6.7
MAINTAINER  Marcus Ottosson <marcus@abstractfactory.io>

# ADD doesn't like these links, so we use wget
RUN yum install -y wget && \
    cd ~ && \
    wget -O ~/sip.tar.gz http://sourceforge.net/projects/pyqt/files/sip/sip-4.17/sip-4.17.tar.gz && \
    wget -O ~/pyqt.tar.gz http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/PyQt-gpl-5.5.1.tar.gz && \
    wget -O ~/qt.tar.gz http://download.qt.io/official_releases/qt/5.4/5.4.0/single/qt-everywhere-opensource-src-5.4.0.tar.gz

RUN yum update -y && \
    yum groupinstall -y "Development Tools" && \
    yum install -y \
      perl \
      git \
      tar \
      centos-release-SCL \
      python-devel \
      mesa-libGL-devel && \
    yum install -y python27

# Must install python27 *after* centos-release-SCL

RUN tar -xvf ~/qt.tar.gz -C ~/ && \
    tar -xf ~/sip.tar.gz  -C ~/ && \
    tar -xf ~/pyqt.tar.gz  -C ~/ && \
    mv ~/qt-everywhere-opensource-src-5.4.0 ~/qt && \
    mv ~/sip-4.17 ~/sip && \
    mv ~/PyQt-gpl-5.5.1 ~/pyqt

RUN cd ~/qt && \
  ./configure \
    -confirm-license \
    -opensource \
    -nomake examples \
    -nomake tests \
    -no-compile-examples \
    -no-xcb \
    -prefix "/usr/local/Qt" && \
  make -j4 all && \
  make install

RUN cd ~ && \
    source /opt/rh/python27/enable && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py

RUN cd ~/sip && \
    source /opt/rh/python27/enable && \
    python configure.py && \
    make && \
    make install

RUN cd ~/pyqt && \
    source /opt/rh/python27/enable && \
    python configure.py \
      --confirm-license \
      --qmake /usr/local/Qt/bin/qmake \
      --sip /opt/rh/python27/root/usr/bin/sip && \
    make && \
    make install && \
    cp -r /usr/local/Qt/qml /opt/rh/python27/root/usr/lib64/python2.7/site-packages/PyQt5/qml

RUN echo source /opt/rh/python27/enable > ~/.bashrc

WORKDIR /root/workdir
