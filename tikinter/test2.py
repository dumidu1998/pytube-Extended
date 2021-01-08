from tkinter import *
import pytube 


root=Tk()
root.title('Youtube Downloader')
root.geometry("400x100")

e = Entry(root, width=40, borderwidth=3)
e.pack()


def myClick():
    url = e.get() 
    myLabel =Label(root,text=url)
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()
    myLabel =Label(root,text=video.title)
    myLabel.pack()
myButton= Button(root,text="Click me!", command=myClick)
myButton.pack()

root=mainloop()