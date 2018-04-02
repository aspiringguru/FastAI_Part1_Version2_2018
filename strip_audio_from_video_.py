#https://zulko.github.io/moviepy/install.html
#pip install moviepy
import moviepy.editor as mp
fileName = "test.mp4"
print ("file length:", mp.VideoFileClip(fileName).duration)
clip = mp.VideoFileClip(fileName).subclip(0,30)
#clip.audio.write_audiofile("theaudio.mp3")
#we will use .wav format only.
clip.audio.write_audiofile("theaudio.wav")
