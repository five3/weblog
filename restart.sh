#!/bin/bash
#cd ~/python/webpycms/
ps -ef | grep python | grep 8090 | awk '{print $2}' | xargs kill -9
find . -type f -name "*.pyc" | xargs rm -rf
svn up
find . -type f -name "*.pyc" | xargs rm -rf
nohup python app.py 8090 &
