#Libraries
import RPi.GPIO as GPIO
import time
import subprocess
from threading import Thread
import sys


#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(self.trigpin, GPIO.OUT)
#GPIO.setup(self.echopin, GPIO.IN)

class ProcessThread(Thread):
    def __init__(self,ultraio):
        super(ProcessThread, self).__init__()
        self.running = True
        self.ultra_io=ultraio

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            # block for 1 second only:
            self.ultra_io.update_distance()
            time.sleep (1)

class ultrasonic_io:
    def __init__(self, trigpin, echopin, multiplier):
        #zero the tracking distance and the current distance
        self.lastdist=0.0
        self.currdist=0.0
        self.speed=0.0

        #start off with no speed, not tracking distance, and set the multiplier/second
        self.speed=0.0
        self.processing=False
        self.multiplier=multiplier

        #set GPIO Pins
        self.trigpin = trigpin
        self.echopin = echopin


    def update_distance(self):
        # set Trigger to HIGH
        GPIO.output(self.trigpin, True)
 
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.trigpin, False)

 
        StartTime = time.time()
        StopTime = time.time()
 
        # save StartTime
        while GPIO.input(self.echopin) == 0:
            StartTime = time.time()
 
        # save time of arrival
        while GPIO.input(self.echopin) == 1:
            StopTime = time.time()
 
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        self.lastdist = self.currdist
        self.currdist = (TimeElapsed * self.multiplier) / 2
        self.speed    = self.lastdist-self.currdist
    
    def get_last_distance(self):
        return self.lastdist

    def get_curr_distance(self):
        return self.currdist

    def get_speed(self):
        return self.speed

    def setup_channels(self):
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.trigpin, GPIO.OUT)
        GPIO.setup(self.echopin, GPIO.IN)

    def start_processing(self):
        if self.processing == False:
            #set GPIO direction (IN / OUT)
            self.setup_channels()
            self.thread = ProcessThread(self)
            self.thread.start()
            self.processing=True

    def stop_processing(self):
        self.thread.stop()
        self.thread.join()
        self.processing=False

 
if __name__ == '__main__':
    dist = ultrasonic_io(12,18,34300)
    try:
        GPIO.setmode(GPIO.BOARD)
        #dist.start_processing()
        dist.setup_channels()
        while True:
            dist.update_distance()
            ##print ("Measured Distance = %.1f cm" % dist.distance())
            print ("CURRENT: "+str(dist.get_curr_distance()))
            print ("PRIOR  : "+str(dist.get_last_distance()))
            print ("SPEED  : "+str(dist.get_speed()))
            print ("=========")
            #print ("Speed = %.1f cm/sec" % dist.speed())

            time.sleep(2)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        #dist.stop_processing()
        GPIO.cleanup()
    except:
        print "EXCEPTION: "+str(sys.exc_info())
        #e = sys.exc_info()[0]
        #print e
        #dist.stop_processing()
        GPIO.cleanup()
