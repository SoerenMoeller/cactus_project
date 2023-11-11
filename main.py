import speaker_control
import RPi.GPIO as GPIO


def main():
    speaker_control.play_audio("test")
    setup()
    while True:
        loop()

def setup():
    GPIO.setmode(GPIO.BCM)
    
    # set IO
    GPIO.setup(17, GPIO.OUT)

    # init values
    GPIO.output(17, True)


def loop():
    ...


if __name__ == "__main__":
    main()
