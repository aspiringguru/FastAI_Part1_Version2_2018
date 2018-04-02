#https://zulko.github.io/moviepy/install.html
#pip install moviepy
import moviepy.editor as mp
clip = mp.VideoFileClip("Gun Control Americas Got A Gun Problem.mp4")#.subclip(0,20)
clip.audio.write_audiofile("theaudio.mp3")
