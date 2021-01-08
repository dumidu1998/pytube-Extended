from pytube import Playlist
import subprocess


#
#print('done')

url="https://youtube.com/playlist?list=PLc-ZL1ypjkEY2Nj4M106SO_Jf_LrnXQeY"
playlist = Playlist(url)

print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
for video in playlist.videos:
    s= video.streams.get_highest_resolution()
    print(s.title)
    s.download()
    print("-----------------------done------------------------")

subprocess.call("./sleep.sh")
