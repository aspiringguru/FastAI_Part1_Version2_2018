#pip install SpeechRecognition
#https://github.com/Uberi/speech_recognition
#https://stackoverflow.com/questions/41525200/convert-mp4-sound-to-text-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa

import urllib
import speech_recognition as sr
import subprocess
import os

#url = 'https://blah'
#mp4file = urllib.urlopen(url)

#with open("input_file.mp4", "wb") as handle:
#    handle.write(mp4file.read())

cmdline = ['avconv',
           '-i',
           'test.mp4',
           '-vn',
           '-f',
           'wav',
           'test.wav']
subprocess.call(cmdline)

r = sr.Recognizer()
with sr.AudioFile('test.wav') as source:
    audio = r.record(source)

command = r.recognize_google(audio)
print (command)

#os.remove("test.mp4")
#os.remove("test.wav")
