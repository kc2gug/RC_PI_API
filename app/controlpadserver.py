#!/usr/bin/env python
# server.py

import socket
import SocketServer
import select
import config as cfg
import Queue
import subprocess

import RPi.GPIO as GPIO

from threading import Thread
from time import sleep
from random import randint
import sys

class ProcessThread(Thread):
    def __init__(self):
        super(ProcessThread, self).__init__()
        self.running = True
        self.q = Queue.Queue()

    def add(self, data):
        self.q.put(data)

    def stop(self):
        self.running = False

    def run(self):
        q = self.q
        while self.running:
            try:
                # block for 1 second only:
                value = q.get(block=True, timeout=5)
                process(value)
            except Queue.Empty:
                sys.stdout.write('.')
                sys.stdout.flush()
        #
        if not q.empty():
            print "Elements left in the queue:"
            while not q.empty():
                print q.get()

t = ProcessThread()
t.start()

GPIO.setmode(GPIO.BOARD)


def process(value):
    xySplit = value.split()[len(value.split())-1].split('&',2);
    xVal = int(xySplit[0].split('=',2)[1]);
    yVal = int(xySplit[1].split('=',2)[1]);

    if xVal == 0 and yVal > 0: ## FORWARD
        set_gpio("FWD")
    elif xVal == 0 and yVal < 0: ## BACKWARD
        set_gpio("BAK")
    elif xVal > 0 and yVal == 0: ## SPIN RIGHT
        set_gpio("SRT")
    elif xVal < 0 and yVal == 0: ## SPIN LEFT
        set_gpio("SLT")
    elif xVal < 0 and yVal > 0: ## FL
        set_gpio("FWL")
    elif xVal < 0 and yVal < 0: ## BL
        set_gpio("BWL")
    elif xVal > 0 and yVal < 0: ## BR
        set_gpio("BWR")
    elif xVal > 0 and yVal > 0: ## FR
        set_gpio("FWR")
    else: ## STOP
        set_gpio("STP")
        
    print xVal
    print yVal

def set_gpio(direction):
    for thing in range(0,len(cfg.GPIO_DRIVE_PINS)):
        GPIO.output(cfg.GPIO_DRIVE_PINS[thing],cfg.DRIVE_DEFS[cfg.DRIVE_DIR][0][direction][0]["PIN"+str(thing+1)])

def enable_gpio():
    for thing in range(0,len(cfg.GPIO_DRIVE_PINS)):
        GPIO.setup(cfg.GPIO_DRIVE_PINS[thing],GPIO.OUT)
        GPIO.output(cfg.GPIO_DRIVE_PINS[thing],False)

def main():
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    this_ip = subprocess.check_output(['hostname', '--all-ip-addresses']).split(" ",1)[0]
    s.bind((this_ip, cfg.PORT))        # Bind to the port
    print "Listening on port ", cfg.PORT," ..."
    s.listen(5)                 # Now wait for client connection.
    while True:
 
        try:
            client, addr = s.accept()
            ready = select.select([client,],[], [],2)
            if ready[0]:
                data = client.recv(4096)
                #print data
                t.add(data)
        except KeyboardInterrupt:
            print
            print "Stop."
            break
        except socket.error, msg:
            print "Socket error! %s" % msg
            break
    cleanup()

def cleanup():
    GPIO.cleanup()
    t.stop()
    t.join()

#########################################################

if __name__ == "__main__":
    main()
