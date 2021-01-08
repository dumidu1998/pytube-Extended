from pytube import Playlist
playlist = Playlist('https://www.youtube.com/playlist?list=PLcwO5OebB2Ek-T0Vlktjz7UX2i9vdkysf')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
for video in playlist.videos:
    video.streams.first().download('/media/sf_PC')
