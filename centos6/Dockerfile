FROM        centos:6.7
MAINTAINER  Marcus Ottosson <marcus@abstractfactory.io>

# ADD doesn't like these links, so we use wget
RUN yum install -y wget && \
    wget -O sip.tar.gz http://sourceforge.net/projects/pyqt/files/sip/sip-4.17/sip-4.17.tar.gz && \
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

RUN tar -xvf qt.tar.gz && \
    tar -xf sip.tar.gz  && \
    tar -xf pyqt.tar.gz  && \
    mv ~/qt-everywhere-opensource-src-5.5.1 ~/qt && \
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
  cd ~/qt && \
  make -j4 all && \
  make install

RUN source /opt/rh/python27/enable && \
    cd ~/sip && \
    python configure.py && \
    make && \
    make install

RUN cd ~/pyqt && \
    python configure.py \
      --confirm-license \
      --qmake /usr/local/Qt/bin/qmake \
      --sip /usr/bin/sip && \
    make && \
    make install

RUN cd ~/pyblish-shell && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    pip install -r requirements.txt  && \
    python setup.py build && \
    echo Completed Successfully!
