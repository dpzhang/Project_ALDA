#!/bin/bash  
 
# Bash script for installing most modules for AldaCourse.

sudo apt-get clean
sudo apt-get update
sudo python3 -m pip install Django==1.10.6
sudo python3 -m pip install selenium
sudo python3 -m pip install numpy
sudo python3 -m pip install openpyxl

# install PhantomJS
#sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
# extract the files to directory
#sudo tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2

#sudo mv $PHANTOM_JS /usr/local/share
#sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

PHANTOM_VERSION="phantomjs-1.9.8"
ARCH=$(uname -m)

if ! [ $ARCH = "x86_64" ]; then
    $ARCH="i686"
fi

PHANTOM_JS="$PHANTOM_VERSION-linux-$ARCH"

sudo apt-get update
sudo apt-get install build-essential chrpath libssl-dev libxft-dev -y
sudo apt-get install libfreetype6 libfreetype6-dev -y
sudo apt-get install libfontconfig1 libfontconfig1-dev -y

cd ~
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2

sudo tar xvjf $PHANTOM_JS.tar.bz2

sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

cd AldaCourse/aldacourse/
python3 manage.py runserver
