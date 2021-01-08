import pytube

url = 'https://www.youtube.com/watch?v=LXb3EKWsInQ&'

youtube = pytube.YouTube(url)

video = youtube.streams.get_highest_resolution()
print(video.title)
#video.download('/media/sf_PC')
print('done')
