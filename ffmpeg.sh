#!/bin/bash
while :
do
  rm -rf /opt/cv2/a.jpg
  ffmpeg -f avfoundation -i "default" /opt/cv2/a.jpg
  sleep 1
done