import speech_recognition as sr
from pydub import AudioSegment
import os
import math
import sys

# directory where the audio files are
root = "C:/Users/awalker/Downloads/reduced"
if sys.argv.count > 1 :
   root = sys.argv[1]
if not os.path.exists(root) or not os.path.isdir(root):
   print('Could not open containing folder')
   exit()
files = os.listdir(root)

# open output file
audio_text = open('audio_text.txt', 'w+')

# write header
audio_text.write('Speech to text:\n\n')

file_index = 1

# create speech recognizer
recognizer = sr.Recognizer()

# go through each file in audio dir
for file in files :
   # write which file it is
   audio_text.write("File " + str(file_index) + ":\n")

   # get file name
   file_name = root + '/' + file

   audio = AudioSegment.from_file(file_name, format='wav')

   # length of the audio in milliseconds
   audio_length = len(audio)
   print(f'Audio Length: {audio_length}')

   split_size = 6000

   # get number of 8 second chunks
   chunk_count = len(audio) / split_size
   chunk_count = math.ceil(chunk_count)

   for i in range(0, chunk_count) :
      # get start and end, use that to get current chunk
      start = split_size*i
      end = split_size + split_size * i if i != chunk_count - 1 else len(audio)
      chunk = audio[start:end]

      # chunk name
      chunk_name = f'chunk_{i}'
      # storing the chunk to local storage
      chunk.export(chunk_name, format = 'wav')
      # printing the chunk
      print(f'{chunk_name} start: {start} end: {end}')
      
      # creating a listened audio
      with sr.AudioFile(chunk_name) as chunk_audio:
         chunk_listened = recognizer.listen(chunk_audio)
         
      # recognizing content from the audio
      try:
         # getting content from the chunk
         content = recognizer.recognize_vosk(chunk_listened)

         # writing to the file, removes the premade vosk format
         audio_text.write(content[14:-3] + ' ')
      # if not recognized
      except sr.UnknownValueError:
         print('Audio is not recognized')
      # request error if incorrectly setup
      except sr.RequestError as Error:
         print('Request Error')

   # write next line for next file
   audio_text.write('\n')
   file_index += 1
audio_text.close()