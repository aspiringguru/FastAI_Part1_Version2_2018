
from pytube import YouTube
import moviepy.editor as mp
import os
import sys

print ("started")
vid_url = ""
if len(sys.argv)<2:
    print ("needs youtube url to download")
    sys.exit()
else:
    vid_url = sys.argv[1]
    print ("vid_url=", vid_url)


directory = "./temp"
url_prefix = "https://www.youtube.com"

if url_prefix not in vid_url:
    print ("url must start with ", url_prefix)
    sys.exit()


if not os.path.exists(directory):
    os.makedirs(directory)
os.chdir(directory)
print ("Current working directory:", os.getcwd())
#NB: concurrency race condition potential for failure exists.
#needs error condition checking

#temp hack. rework this after debugging. (delete all files?)
#test if mp4 already in dir, download if no mp4.
vid_filename_suffix = ".mp4"
files = [f for f in os.listdir('.') if os.path.isfile(f)]
vid_filename = ""

def dir_file_ends_with(dir, extension):
    files = [f for f in os.listdir(dir) if os.path.isfile(f)]
    vid_filename = ""
    count = 0
    for f in files:
        if f.endswith(extension):
            vid_filename = f
            break
        count += 1
    if count == len(files):
        return None
    else:
        return vid_filename

vid_filename = dir_file_ends_with('.', vid_filename_suffix)
if vid_filename:
    print ("file ending with {} found.".format(vid_filename_suffix))
else:
    print ("Did not find file ending with {}.".format(vid_filename_suffix))
    print ("downloading")
    yt = YouTube(vid_url)
    yt = yt.streams.first().download()
    print ("downloaded.")
    vid_filename = dir_file_ends_with('.', vid_filename_suffix)


#now strip audio from the video file
print ("vid_filename:", vid_filename)
vidLength = mp.VideoFileClip(vid_filename).duration
print ("file length:", vidLength)

#NB: this is temp fix to allow processing in 30 second blocks
#obviously 30 second blocks will break mid phonetic sound
#and break the audio to text conversion inconsistently.
def stripAudio(fileName, startTime, endTime, counter):
    print ("stripAudio(", fileName, ", ", startTime, ", ", endTime, ", ", counter, ")")
    clip = mp.VideoFileClip(fileName).subclip(startTime, endTime)
    #clip.audio.write_audiofile("theaudio.mp3")
    #we will use .wav format only.
    clip.audio.write_audiofile("theaudio{}.wav".format(counter))



vid_processing_length = 30 #30 seconds
vid_segments = list(range(0, int(vidLength), vid_processing_length))
counter_ = 0
for start_time in vid_segments[:-1]:
    print (vid_filename, start_time, start_time+vid_processing_length, counter_)
    stripAudio(vid_filename, start_time, start_time+vid_processing_length, counter_)
    counter_ += 1
print ("vid_segments[:-1]:", type(vid_segments[:-1]))
print ("vid_segments[-1]:", vid_segments[-1])
print (vidLength)
stripAudio(vid_filename, int(vid_segments[-1]), int(vidLength), counter_)

#now convert audio files to text
#use fast.py 
