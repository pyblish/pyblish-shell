# Compile dependencies and build pyblish-shell for Centos 6.7
# Produce output in current working directory.
#
# Usage:
#   $ git clone https://github.com/pyblish/pyblish-shell.git
#   $ docker build -t mottosso/pyblish-shell-centos pyblish-shell/centos6
#   $ docker run -ti --rm -v $(pwd)/pyblish-shell:/root/workdir mottosso/pyblish-shell-centos build-exe.sh

FROM        centos:6.7
MAINTAINER  Marcus Ottosson <marcus@abstractfactory.io>

RUN yum update -y && \
    yum groupinstall -y "Development Tools" && \
    yum install -y \
      perl \
      git \
      tar \
      centos-release-SCL \
      libxcb \
      libxcb-devel \
      xcb-util \
      xcb-util-devel \
      mesa-libGL-devel && \
    yum install -y python27

# Must install python27 *after* centos-release-SCL

# ADD doesn't like these links, so we use wget
RUN yum install -y wget && \
    cd ~ && \
    wget -O ~/sip.tar.gz http://sourceforge.net/projects/pyqt/files/sip/sip-4.17/sip-4.17.tar.gz && \
    wget -O ~/pyqt.tar.gz http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.5.1/PyQt-gpl-5.5.1.tar.gz && \
    git clone git://code.qt.io/qt/qt5.git && \
    cd qt5 && \
    git checkout 5.4.2 && \
    perl init-repository

RUN tar -xf ~/sip.tar.gz  -C ~/ && \
    tar -xf ~/pyqt.tar.gz  -C ~/ && \
    mv ~/sip-4.17 ~/sip && \
    mv ~/PyQt-gpl-5.5.1 ~/pyqt

# We'll need GCC 4.7.2, default is 4.7.7, see here:
# http://forum.qt.io/topic/30140/solved-qt-creator-could-not-find-or-load-the-qt-platform-plugin-xcb/7
RUN wget http://people.centos.org/tru/devtools-1.1/devtools-1.1.repo -O /etc/yum.repos.d/devtools-1.1.repo && \
    yum install -y devtoolset-1.1

RUN cd ~/qt5 && \
    scl enable devtoolset-1.1 "./configure \
        -confirm-license \
        -opensource \
        -qt-xcb \
        -nomake examples \
        -nomake tests \
        -no-gtkstyle \
        -qt-libpng \
        -no-c++11
    make -j4 all && \
    make install"

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
      --confirm-license && \
    make && \
    make install

    # cp -r /usr/local/Qt/qml /opt/rh/python27/root/usr/lib64/python2.7/site-packages/PyQt5/qml

# Setup environment
RUN echo source /opt/rh/python27/enable >> ~/.bashrc
WORKDIR /root/workdir
