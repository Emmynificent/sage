from pytube import YouTube
from tkinter import *
# import index.html
# x='https://www.youtube.com/watch?v=j8jqglSJXdw'
# yt = YouTube(x)
# # get = yt.streams.get_highest_resolution()
# # get.download()


# another = yt.streams.first().download()
def link(url):
    yt = YouTube(url)
    spec = yt.streams.get_highest_resolution()
    spec.download()
    

ur = input('enter Youtube Url: ')

link(ur)

