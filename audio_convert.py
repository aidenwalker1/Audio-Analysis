import noisereduce as nr
from scipy.io import wavfile
import os
root = 'C:/Users/awalker/Downloads/wav_files'
dest = "C:/Users/awalker/Downloads/reduced"
files = os.listdir(root)
for file in files :
    filename = root + '/' + file
    rate, data = wavfile.read(filename)

    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    wavfile.write(dest + '/' + file, rate, reduced_noise)