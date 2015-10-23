#! /bin/sh

wget http://sourceforge.net/projects/pyqt/files/sip/sip-4.16.9/sip-4.16.9.tar.gz
tar -zxvf sip-4.16.9.tar.gz
cd sip-4.16.9/
python configure.py
make
make install
