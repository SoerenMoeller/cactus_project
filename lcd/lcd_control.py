import lcd.lcddriver as lcddriver
from time import *


lcd = lcddriver.lcd()
lcd.lcd_clear()


def display(top: str, bottom: str):
    lcd.lcd_clear()
    lcd.lcd_display_string(top, 1)
    lcd.lcd_display_string(bottom, 2)


def close():
    if lcd is not None:
        lcd.close()
