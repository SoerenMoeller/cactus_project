from os import listdir
from os.path import isfile, join

def get_random_music():
    path: str = "resources/music"
    files = [f.removesuffix(".mp3") for f in listdir(path) if isfile(join(path, f))]
    print(files)

get_random_music()
