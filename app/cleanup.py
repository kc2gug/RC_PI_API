#!/usr/bin/env python

import RPi.GPIO as GPIO
import config as cfg
from time import sleep

GPIO.setmode(GPIO.BOARD)

for thing in range(0,len(cfg.DPIO)):
    print ("Closing GPIO pin: "+str( cfg.DPIO[thing] ))
    GPIO.setup(cfg.DPIO[thing],GPIO.OUT)



print ("Closing GPIO pin: "+str( cfg.ULTIO_TRIG ))
GPIO.setup(cfg.ULTIO_TRIG, GPIO.OUT)
print ("Closing GPIO pin: "+str( cfg.ULTIO_ECHO ))
GPIO.setup(cfg.ULTIO_ECHO, GPIO.OUT)

GPIO.cleanup()
