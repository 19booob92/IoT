#!/bin/bash

ip=192.168.8.102

find -name *.py | xargs sed -i 's/192.168.8.101/192.168.8.102/g'

find -name *.js | xargs sed -i 's/192.168.8.101/192.168.8.102/g'
