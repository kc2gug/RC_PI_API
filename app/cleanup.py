#!/usr/bin/env python

import RPi.GPIO as GPIO
import config as cfg
from time import sleep

GPIO.setmode(GPIO.BOARD)

for thing in range(0,len(cfg.DPIO)):
    print (cfg.DPIO[thing],cfg.DRIVE_DEFS['FORWARD'][0]['FWD'][0][cfg.DPIO[thing]])
    GPIO.setup(cfg.DPIO[thing],GPIO.OUT)


GPIO.cleanup()
