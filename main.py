import speaker_control
import RPi.GPIO as GPIO
import signal
import sys


GPIO_BUTTON: int = 10


def main():
    speaker_control.play_audio("test")
    setup()
    while True:
        loop()


def setup():
    GPIO.setmode(GPIO.BCM)
    
    # set IO
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(GPIO_BUTTON, GPIO.IN)

    # init values
    GPIO.output(17, True)

    GPIO.add_event_detect(GPIO_BUTTON, GPIO.FALLING, 
            callback=button_pressed_callback, bouncetime=100)
    #GPIO.add_event_detect(BUTTON_GPIO, GPIO.RISING, 
    #        callback=button_released_callback, bouncetime=100)


def loop():
    ...


def button_pressed_callback(channel):
    ...


def signal_handler(sig, frame):
    """Cleanup when interrupted"""
    GPIO.cleanup()
    sys.exit(0)


if __name__ == "__main__":
    main()
