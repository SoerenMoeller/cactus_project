from playsound import playsound
import os
import multiprocessing


RESOURCES: str = "resources"
playing_process = None


def play_audio(file_name: str):
    global playing_process

    file_path = os.path.join(RESOURCES, f"{file_name}.mp3")
    assert os.path.exists(file_path), f"File '{file_path}' not found"

    if playing_process is not None:
        playing_process.terminate()
        playing_process = None

    print(f"Playing '{file_path}'")
    playing_process = multiprocessing.Process(target=playsound, args=(file_path,))
    playing_process.daemon = True
    playing_process.start()
   
