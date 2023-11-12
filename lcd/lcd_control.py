import lcd.lcddriver as lcddriver
from time import *


LCD_WIDTH = 16
lcd = lcddriver.lcd()
lcd.lcd_clear()


def display(top: str, bottom: str):
    """This expexts both strings to have a length <= 16"""
    
    lcd.lcd_clear()

    lcd.lcd_display_string(top, 1)
    lcd.lcd_display_string(bottom, 2)


def close():
    if lcd is not None:
        lcd.close()
