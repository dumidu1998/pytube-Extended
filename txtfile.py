
import sys
import pytube 

# Using readlines() 
file1 = open('vlinks.txt', 'r') 
Lines = file1.readlines() 
  
def yt(url):
    
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    print(video.title)
    print("start downloading")
    #video.download()
    print("downloaded")


    
def download(x):
    yt(x)



count = 0
# Strips the newline character 
for line in Lines: 
    #print("Line{}: {}".format(count, line.strip()))
    s= line.strip()
    print(s)
    download(s)