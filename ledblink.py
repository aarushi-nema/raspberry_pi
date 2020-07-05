#!/usr/bin/python3
import RPi.GPIO as  GPIO
import time 

ledpin=22

def setup():
   GPIO.setmode(GPIO.BOARD)
   GPIO.setup(ledpin, GPIO.OUT)
   GPIO.output(ledpin, GPIO.LOW)


def loop():
   while True:
     print ('LED on')
     GPIO.output(ledpin, GPIO.HIGH)
     time.sleep(1.0)
     print ('LED off')
     GPIO.output(ledpin, GPIO.LOW)
     time.sleep(1.0)


def endprogram():
   GPIO.output(ledpin, GPIO.LOW)
   GPIO.cleanup()

if __name__ =='__main__':
   setup()
   try:
     loop()
   except KeyboardInterrupt:
     endprogram()
