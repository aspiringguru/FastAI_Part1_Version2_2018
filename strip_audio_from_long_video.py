#https://zulko.github.io/moviepy/install.html
#pip install moviepy
import moviepy.editor as mp
fileName = "test.mp4"
vidLength = mp.VideoFileClip(fileName).duration
print ("file length:", vidLength)


#NB: this is temp fix to allow processing in 30 second blocks
#obviously 30 second blocks will break mid phonetic sound
#and break the audio to text conversion inconsistently.
def stripAudio(fileName, startTime, endTime, counter):
    clip = mp.VideoFileClip(fileName).subclip(startTime, endTime)
    #clip.audio.write_audiofile("theaudio.mp3")
    #we will use .wav format only.
    clip.audio.write_audiofile("theaudio{}.wav".format(counter))



vid_processing_length = 30 #30 seconds
vid_segments = list(range(0, int(vidLength), vid_processing_length))
counter_ = 0
for start_time in vid_segments[:-1]:
    print (start_time, start_time+vid_processing_length)
    stripAudio(fileName, start_time, start_time+vid_processing_length, counter_)
    counter_ += 1
print ("vid_segments[:-1]:", type(vid_segments[:-1]))
print ("vid_segments[-1]:", vid_segments[-1])
print (vidLength)
stripAudio(fileName, int(vid_segments[-1]), int(vidLength), counter_)
