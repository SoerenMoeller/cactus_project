LCD_ENABLED = False


import speaker_control
import pin_mapping as pin
import RPi.GPIO as GPIO
import signal
import sys
import tts_control
from random import randrange
from random_phrases import *
from time import time
from enum import Enum
if LCD_ENABLED:
    import lcd.lcd_control as lcd_control


class State(Enum):
    IDLE = 0
    START_MUSIC = 1
    MUSIC_LOOP = 2
    START_RANDOM_PLAY = 3


DUTY_CYCLE = 100
FREQUENCY_ENGINE = 50
BUTTON_BOUNCE = 20
RANDOM_PLAY_MIN_WAIT = 10   # in sec
RANDOM_PLAY_MAX_WAIT = 15   # in sec

engine_power_l = None
engine_power_r = None
state: State = State.IDLE
activate_music: bool = False
time_start = time()
next_play_delay = 10000


def main():
    setup()
    while True:
        loop()


def setup():
    global engine_power_l, engine_power_r

    signal.signal(signal.SIGINT, signal_handler)
    GPIO.setmode(GPIO.BCM)

    # set IO
    GPIO.setup(pin.BUTTON_MUSIC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(pin.LED_POWER, GPIO.OUT)
    GPIO.setup(pin.ENGINE_POWER_L, GPIO.OUT)
    GPIO.setup(pin.ENGINE_POWER_R, GPIO.OUT)

    engine_power_l = GPIO.PWM(pin.ENGINE_POWER_L, FREQUENCY_ENGINE)
    engine_power_r = GPIO.PWM(pin.ENGINE_POWER_R, FREQUENCY_ENGINE)

    GPIO.output(pin.LED_POWER, False)

    GPIO.add_event_detect(pin.BUTTON_MUSIC, GPIO.FALLING,
            callback=button_pressed_callback, bouncetime=BUTTON_BOUNCE)
    
    if LCD_ENABLED:
        lcd_control.display("")
    start_random_timer()

def loop():
    global state

    match state:
        case State.IDLE:
            if activate_music:
                state = State.START_MUSIC

            time_stamp = time()
            if time_stamp - time_start >= next_play_delay:
                state = State.START_RANDOM_PLAY
        case State.START_MUSIC:
            speaker_control.play_audio("test")
            GPIO.output(pin.LED_POWER, True)
            engine_power_l.start(DUTY_CYCLE)

            print("Starting music")
            state = State.MUSIC_LOOP
        case State.MUSIC_LOOP:
            if not activate_music:
                speaker_control.terminate_audio()
                GPIO.output(pin.LED_POWER, False)
                state = State.IDLE
                engine_power_l.stop()
                start_random_timer()

                print("Stopped music")
        case State.START_RANDOM_PLAY:
            print("Starting to random play")
            phrase = get_random_phrase()
            tts_control.createTTS(phrase[VOICE])
            speaker_control.play_audio("tts", False)
            if LCD_ENABLED:
                lcd_control.display(phrase[TEXT][0], phrase[TEXT][1])

            start_random_timer()
            state = State.IDLE
        case _:
            assert False, "Unknown state"


def button_pressed_callback(channel):
    global activate_music

    activate_music = not activate_music


def start_random_timer():
    global next_play_delay, time_start
    current_time = time()

    next_play_delay = randrange(RANDOM_PLAY_MIN_WAIT, RANDOM_PLAY_MAX_WAIT)
    print(f"Waiting for {next_play_delay}s before playing randomly")
    time_start = current_time


def signal_handler(sig, frame):
    """Cleanup when interrupted"""
    if engine_power_l is not None:
        engine_power_l.stop()
    GPIO.cleanup()
    if LCD_ENABLED:
        lcd_control.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
