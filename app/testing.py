#!/usr/bin/evn python
# testing.py

##import json
import config as cfg

print (len(cfg.GPIO_DRIVE_PINS))
print (cfg.GPIO_DRIVE_PINS)
print (cfg.DRIVE_DEFS['FORWARD'][1])
print (cfg.DRIVE_DEFS['FORWARD'][0]["SRT"])

direction="BAK"

for thing in range(0,len(cfg.GPIO_DRIVE_PINS)):
    print (cfg.GPIO_DRIVE_PINS[thing],cfg.DRIVE_DEFS['FORWARD'][0][str(direction)][0]["PIN"+str(thing+1)])
