import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

en1= 2
in1= 3
in2= 4
en2= 14
in3= 15
in4= 18

GPIO.setup(en1, GPIO.OUT)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)


pwm1= GPIO.PWM(en1, 100)
pwm2= GPIO.PWM(en2, 100)

pwm1.start(0)
pwm2.start(0)


while True:
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.HIGH)
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)
    sleep(4)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    pwm1.ChangeDutyCycle(50)
    pwm2.ChangeDutyCycle(50)
    sleep(4)

    

