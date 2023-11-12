import lcd.lcddriver as lcddriver
from time import *


LCD_WIDTH = 16
lcd = lcddriver.lcd()
lcd.lcd_clear()


def display(text: str):
    lcd.lcd_clear()

    top = text
    bottom = ""
    if len(text) > LCD_WIDTH:
        top = text[:LCD_WIDTH]
        text = text[LCD_WIDTH:]
        bottom = text

        if len(text) > LCD_WIDTH:
            bottom = text[:LCD_WIDTH] 

    lcd.lcd_display_string(top, 1)
    lcd.lcd_display_string(bottom, 2)


def close():
    if lcd is not None:
        lcd.close()
