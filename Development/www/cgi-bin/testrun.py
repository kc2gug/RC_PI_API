#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

print "Content-Type: text/plain;charset=utf-8"
print

print "Hello World!"


while True:
	GPIO.output(11, True)
	GPIO.output(13, False)
	sleep (2)
	GPIO.output(13, True)
	GPIO.output(11,False)
	sleep(2)

