#Download youtube video in local
#install pytube

from pytube import YouTube

#input link of desire video

link = input("Enter the link: https://youtu.be/3v4HRXgGQys")
yt = YouTube(link)

print(yt.title) # it will print title of the video
#print(yt.streams)
ys = yt.streams.get_highest_resolution() #this will select highest resolution for the desire video

ys.download() #will download video in the same folder where this python code is.
