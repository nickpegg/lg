#!/bin/bash

adduser --system --home /home/lg --shell /bin/rbash --disabled-password --disabled-login lg
mkdir /home/lg/bin
ln -s `which mtr` /home/lg/bin/mtr
ln -s `which ping` /home/lg/bin/ping
chmod +s `which mtr`

echo "export PATH=/home/lg/bin" > /home/lg/.bashrc
chown -R root:root /home/lg

