#!/usr/bin/env python
# server.py

import socket
import SocketServer
import select
import config as cfg
import Queue

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
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

GPIO.output(7,False)
GPIO.output(11,False)
GPIO.output(13,False)
GPIO.output(15,False)

def process(value):
    #GPIO.output(7, True)
    #GPIO.output(11, False)
    xySplit = value.split()[len(value.split())-1].split('&',2);
    xVal = int(xySplit[0].split('=',2)[1]);
    yVal = int(xySplit[1].split('=',2)[1]);

    if xVal == 0 and yVal > 0: ## FORWARD
        GPIO.output(7,True)
        GPIO.output(11,False)
        GPIO.output(13,True)
        GPIO.output(15,False)
    elif xVal == 0 and yVal < 0: ## BACKWARD
        GPIO.output(7,False)
        GPIO.output(11,True)
        GPIO.output(13,False)
        GPIO.output(15,True)
    elif xVal > 0 and yVal == 0: ## SPIN RIGHT
        GPIO.output(7,False)
        GPIO.output(11,True)
        GPIO.output(13,True)
        GPIO.output(15,False)
    elif xVal < 0 and yVal == 0: ## SPIN LEFT
        GPIO.output(7,True)
        GPIO.output(11,False)
        GPIO.output(13,False)
        GPIO.output(15,True)
    elif xVal == 0 and yVal > 0: ## FL
        GPIO.output(7,False)
        GPIO.output(11,False)
        GPIO.output(13,True)
        GPIO.output(15,False)
    elif xVal == 0 and yVal > 0: ## BL
        GPIO.output(7,False)
        GPIO.output(11,False)
        GPIO.output(13,False)
        GPIO.output(15,True)
    elif xVal == 0 and yVal > 0: ## BR
        GPIO.output(7,False)
        GPIO.output(11,True)
        GPIO.output(13,False)
        GPIO.output(15,False)
    elif xVal == 0 and yVal > 0: ## FR
        GPIO.output(7,False)
        GPIO.output(11,False)
        GPIO.output(13,True)
        GPIO.output(15,False)
    else: ## STOP
        GPIO.output(7,False)
        GPIO.output(11,False)
        GPIO.output(13,False)
        GPIO.output(15,False)
        
    print xVal;
    print yVal;

def main():
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = cfg.PORT                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port
    print "Listening on port {p}...".format(p=port)

    s.listen(5)                 # Now wait for client connection.
    while True:
        try:
            client, addr = s.accept()
            ready = select.select([client,],[], [],2)
            if ready[0]:
                data = client.recv(4096)
                print data
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
