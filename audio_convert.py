import noisereduce as nr
from scipy.io import wavfile
import os
import sys
root = 'C:/Users/awalker/Downloads/wav_files'
dest = "C:/Users/awalker/Downloads/reduced"

# checking if inputing dest/root folder
if sys.argv.count > 2 :
   root = sys.argv[1]
   dest = sys.argv[2]

# checking root folder exist
if not os.path.exists(root) or not os.path.isdir(root):
   print('Could not open containing folder')
   exit()

# checking dest exist, make new dir if not
if not os.path.exists(dest) or not os.path.isdir(dest):
    print('Dest not found: Creating folder reduced')
    os.makedirs('reduced')
    dest = 'reduced'

files = os.listdir(root)

# go through each file
for file in files :
    filename = root + '/' + file

    # read in file
    rate, data = wavfile.read(filename)

    # reduce noise, save to dest folder
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write(dest + '/' + file, rate, reduced_noise)