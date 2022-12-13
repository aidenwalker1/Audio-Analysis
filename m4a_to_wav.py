from pydub import AudioSegment
import os
import sys

# directory where the audio files are
root = "C:/Users/awalker/Downloads/audio/audio"
dest = "C:/Users/awalker/Downloads/wav_files"

# checking if inputing root/dest folders
if sys.argv.count > 2 :
   root = sys.argv[1]
   dest = sys.argv[2]

# checking root folder exists
if not os.path.exists(root) or not os.path.isdir(root):
   print('Could not open containing folder')
   exit()

# checking dest folder exists, creating new one if not
if not os.path.exists(dest) or not os.path.isdir(dest):
    print('Dest not found: Creating folder wav_files')
    os.makedirs('wav_files')
    dest = 'wav_files'

files = os.listdir(root)

# go through each file
for file in files :
    # get file name
   file_name = root + '/' + file

   # get m4a format, export as wav
   audio = AudioSegment.from_file(file_name, format='m4a')
   audio.export(dest + '/' + file[:-4] + '.wav', format='wav')
