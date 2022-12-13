import speech_recognition as sr
from pydub import AudioSegment
import os
import math

# directory where the audio files are
root = "C:/Users/awalker/Downloads/audio/audio"
dest = "C:/Users/awalker/Downloads/wav_files"
files = os.listdir(root)

for file in files :
    # get file name
   file_name = root + '/' + file

   audio = AudioSegment.from_file(file_name, format='m4a')
   audio.export(dest + '/' + file[:-4] + '.wav', format='wav')
