import os
from glob import glob
from pydub import AudioSegment

extension = '*.wav'

time = 1000 * 60 * 60

for audio in glob(extension):
    filename = os.path.basename(audio)
    splitted_filename = os.path.splitext(filename)
    base_filename = splitted_filename[0]
    fileformat = splitted_filename[1]

    sound = AudioSegment.from_file(filename, format=fileformat)

    sliced_dir = os.makedirs(f"slices/{base_filename}/")

    for i, chunk in enumerate(sound[::time]):
        with open(f"slices/{base_filename}/{base_filename}-slice-{i}.mp3", "wb") as f:
            chunk.export(f, format="mp3")
