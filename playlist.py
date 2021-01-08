from pytube import Playlist

playlist = Playlist('https://www.youtube.com/watch?v=JcVXjgLDMQM&list=PLe8J4_CLxBFoqFy9kzX-Rak_BKRI2e20y')

print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
for video in playlist.videos:
    video.streams.get_highest_resolution().download()
    print("done")
