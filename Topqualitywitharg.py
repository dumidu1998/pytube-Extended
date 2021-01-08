import pytube
import subprocess
import sys
 
url = sys.argv[1]
print(url)

youtube = pytube.YouTube(url)

#video = youtube.streams.get_by_itag(136)
videos = youtube.streams.filter(progressive=False)
if youtube.streams.get_by_itag(315):
	print("2160p Available")
	video = youtube.streams.get_by_itag(315)
elif youtube.streams.get_by_itag(401):
	print("2160p Available")
	video = youtube.streams.get_by_itag(401)
elif youtube.streams.get_by_itag(308):
	print("1440p Available")
	video = youtube.streams.get_by_itag(308)
elif youtube.streams.get_by_itag(299):
	print("1080p Available")
	video = youtube.streams.get_by_itag(299)
elif youtube.streams.get_by_itag(137):
	print("1080p Available")
	video = youtube.streams.get_by_itag(137)
elif youtube.streams.get_by_itag(298):
	print("720p Available")
	video = youtube.streams.get_by_itag(298)
elif youtube.streams.get_by_itag(136):
	print("720p Available")
	video = youtube.streams.get_by_itag(136)

audio=youtube.streams.get_by_itag(140)

print(video)
print(audio)
print('----------------Start downloading-----------')
print(video.title)
#video.download('/media/sf_PC')
video.download()
audio.download('/home/dumidu/utube/audio')
print('----------------Done------------------------')

subprocess.call("./merge.sh")




