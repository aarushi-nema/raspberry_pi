#!/usr/bin/python3

import RPi.GPIO as GPIO
import time

button = 16
led = 18

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(led, GPIO.OUT)

def loop():
    while True:
        Button_state= GPIO.input(button)
        if Button_state == False:
            GPIO.output(led, True)
            print("Button Pressed")
            while GPIO.input(button)==False:
                time.sleep(0.2)

        else:
            GPIO.output(led, False)

def endprogram():
    GPIO.output(led, False)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Keyboard Interrupt Detetcted")
        endprogram()
