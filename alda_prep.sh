#!/bin/bash  
 
# Bash script for installing most modules for AldaCourse.

sudo apt-get clean
sudo apt-get update
sudo python3 -m pip install Django==1.10.6
sudo python3 -m pip install selenium
sudo python3 -m pip install numpy
sudo python3 -m pip install openpyxl

# install PhantomJS
sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
# extract the files to directory
sudo tar xjf phantomjs-2.1.1-linux-x86_64.tar.bz2

cd AldaCourse/aldacourse/
python3 manage.py runserver
