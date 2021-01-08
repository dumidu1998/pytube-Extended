import pytube
import subprocess

url = 'https://www.youtube.com/watch?v=zq3sW8aeJZY&list=PLcwO5OebB2Ek-T0Vlktjz7UX2i9vdkysf&index=3'

youtube = pytube.YouTube(url)

video = youtube.streams.get_audio_only()
print(video.title)
video.download()
print('done')
