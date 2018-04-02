#https://github.com/nficano/pytube
#pip install pytube
from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=bkfgWJYz-Us")
yt = yt.streams.first().download()
