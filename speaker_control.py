import os
from pygame import mixer


RESOURCES: str = "resources"
mixer.init()
mixer.music.set_volume(1)


def play_audio(file_name: str, loop: bool = True):
    file_path = os.path.join(RESOURCES, f"{file_name}.mp3")
    assert os.path.exists(file_path), f"File '{file_path}' not found"

    print(f"Playing '{file_path}'")
    mixer.music.load(file_path)
    if loop:
        mixer.music.play(-1)
    else:
        mixer.music.play()


def terminate_audio():
    mixer.music.pause()
