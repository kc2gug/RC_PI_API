#!/usr/bin/env python

import RPi.GPIO as GPIO
import config as cfg
from time import sleep

GPIO.setmode(GPIO.BOARD)

for thing in range(0,len(cfg.GPIO_DRIVE_PINS)):
    print (cfg.GPIO_DRIVE_PINS[thing],cfg.DRIVE_DEFS['FORWARD'][0]["FWD"][0]["PIN"+str(thing+1)])
    GPIO.setup(cfg.GPIO_DRIVE_PINS[thing],GPIO.OUT)


GPIO.cleanup()
