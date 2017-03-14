#!/bin/bash  
 
# Bash script for installing most required packages for AldaCourse.

sudo apt-get clean
sudo apt-get update
sudo python3 -m pip install Django==1.10.6
sudo python3 -m pip install selenium
sudo python3 -m pip install numpy
sudo python3 -m pip install openpyxl

# install phantomJS
sudo apt-get update
sudo apt-get install build-essential chrpath libssl-dev libxft-dev
sudo apt-get install libfreetype6 libfreetype6-dev
sudo apt-get install libfontconfig1 libfontconfig1-dev

cd ~
export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
sudo tar xvjf $PHANTOM_JS.tar.bz2
sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin

cd -
