import speaker_control
import pin_mapping as pin
import RPi.GPIO as GPIO
import signal
import sys
from enum import Enum


class State(Enum):
    IDLE = 0
    START_MUSIC = 1
    MUSIC_LOOP = 2


DUTY_CYCLE = 100
FREQUENCY_ENGINE = 50
BUTTON_BOUNCE = 20
engine_power_l = None
engine_power_r = None
state: State = State.IDLE
activate_music: bool = False


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


def loop():
    global state

    match state:
        case State.IDLE:
            if activate_music:
                state = State.START_MUSIC
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

                print("Stopped music")
        case _:
            assert False, "Unknown state"


def button_pressed_callback(channel):
    global activate_music

    activate_music = not activate_music


def signal_handler(sig, frame):
    """Cleanup when interrupted"""
    if engine_power_l is not None:
        engine_power_l.stop()
    GPIO.cleanup()
    sys.exit(0)


if __name__ == "__main__":
    main()
