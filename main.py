import speaker_control
import RPi.GPIO as GPIO
import signal 
import sys
from enum import Enum


DUTY_CYCLE        = 100
ENGINE_POWER_PIN  = 15
ENGINE_POWER_BACKWARDS_PIN = 14
GPIO_BUTTON_MUSIC = 18
LED_POWER         = 23
engine_power = None



class State(Enum):
    IDLE = 0
    START_MUSIC = 1
    MUSIC_LOOP = 2


state: State = State.IDLE
activate_music: bool = False


def main():
    setup()
    while True:
        loop()


def setup():
    global engine_power

    signal.signal(signal.SIGINT, signal_handler)
    GPIO.setmode(GPIO.BCM)
    
    # set IO
    GPIO.setup(GPIO_BUTTON_MUSIC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(LED_POWER, GPIO.OUT)
    GPIO.setup(ENGINE_POWER_PIN, GPIO.OUT)
    engine_power = GPIO.PWM(ENGINE_POWER_PIN, 50)
    GPIO.setup(ENGINE_POWER_BACKWARDS_PIN, GPIO.OUT)
    engine_power_backwards = GPIO.PWM(ENGINE_POWER_BACKWARDS_PIN, 50)

    GPIO.output(LED_POWER, False)

    GPIO.add_event_detect(GPIO_BUTTON_MUSIC, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=100)


def loop():
    global state

    match state:
        case State.IDLE:
            if activate_music:
                state = State.START_MUSIC
        case State.START_MUSIC:
            speaker_control.play_audio("test")
            GPIO.output(LED_POWER, True)
            engine_power.start(DUTY_CYCLE)
            
            print("Starting music")
            state = State.MUSIC_LOOP
        case State.MUSIC_LOOP:
            if not activate_music:
                speaker_control.terminate_audio()
                GPIO.output(LED_POWER, False)
                state = State.IDLE
                engine_power.stop()

                print("Stopped music")
        case default:
            assert false, "Unknown state"


def button_pressed_callback(channel):
    global activate_music

    activate_music = not activate_music


def signal_handler(sig, frame):
    """Cleanup when interrupted"""
    engine_power.stop()
    GPIO.cleanup()
    sys.exit(0)


if __name__ == "__main__":
    main()
