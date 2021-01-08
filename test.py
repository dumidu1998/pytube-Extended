import pytube

url = 'https://www.youtube.com/watch?v=6iERC2SSNvc'

youtube = pytube.YouTube(url)
streams = youtube.streams.all()

for i in streams:
	print(i)

video = youtube.streams.get_by_itag(136)
video.download('/home/dumidu/utube')
print('done')
