#!/bin/sh

for f in *.mp4; do ffmpeg -n -i "$f" -c:a libmp3lame "output/${f%.mp4}.mp3"; rm "$f"; done
