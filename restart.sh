#!/bin/bash
#cd ~/python/webpycms/
find . -type f -name "*.pyc" | xargs rm -rf
nohup python app.py 8090 &
