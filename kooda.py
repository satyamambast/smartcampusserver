import nfc
import requests
import RPi.GPIO as GPIO
import time
import cv2
import threading
GPIO.setmode(GPIO.BCM)

trig_1 = 18
echo_1 = 24
GPIO.setup(trig_1,GPIO.OUT)
GPIO.setup(echo_1,GPIO.IN)
trig_2 = 23
echo_2 = 22
GPIO.setup(trig_2,GPIO.OUT)
GPIO.setup(echo_2,GPIO.IN)

servoPin1 = 17
servoPin2 = 27
GPIO.setup(servoPin1, GPIO.OUT)
pwm1=GPIO.PWM(servoPin1,50)
pwm1.start(2.5)
GPIO.setup(servoPin2, GPIO.OUT)
pwm2=GPIO.PWM(servoPin2,50)
pwm2.start(2.5)

#cam = cv2.VideoCapture(0)

def distance1():
    GPIO.output(trig_1,True)

    time.sleep(0.00001)
    GPIO.output(trig_1,False)

    start_time1 = time.time()
    stop_time1 = time.time()

    while GPIO.input(echo_1)==0:
        start_time1 = time.time()
    while GPIO.input(echo_1)==1:
        stop_time1 = time.time()

    timeElapsed1 = stop_time1-start_time1
    
    distance1 = (timeElapsed1*34300)/2
    
    return distance1

def distance2():
    GPIO.output(trig_2,True)

    time.sleep(0.00001)
    GPIO.output(trig_2,False)

    start_time1 = time.time()
    stop_time1 = time.time()

    while GPIO.input(echo_2)==0:
        start_time1 = time.time()
    while GPIO.input(echo_2)==1:
        stop_time1 = time.time()

    timeElapsed1 = stop_time1-start_time1
    
    distance2 = (timeElapsed1*34300)/2
    
    return distance2

def code():
    try:
        while True:
            d1 = distance1()
            d2 = distance2()
            if(d1<40):
                print
            print("Distance left in Plastic Dustbin is->",d1)
            print("Distance left in Paper Dustbin is ->",d2)
            clf=nfc.ContactlessFrontend()
            assert clf.open('ttyS0') is True
            tag = clf.connect(rdwr={'on-connect': lambda tag: False})
            print(tag)
            if tag == False:
                time.sleep(1)
                continue
            garbage = input('give input->')
            if garbage == "paper":
                for i in range(13,3,-1):
                    pwm1.ChangeDutyCycle(i)
                    time.sleep(0.03)
                    print("up")
                time.sleep(5)
                for i in range(3,13):
                    pwm1.ChangeDutyCycle(i)
                    time.sleep(0.03)
                    print("down")
            if garbage == "plastic":
                for i in range(13,3,-1):
                    pwm2.ChangeDutyCycle(i)
                    time.sleep(0.03)
                    print("up")
                time.sleep(5)
                for i in range(3,13):
                    pwm2.ChangeDutyCycle(i)
                    time.sleep(0.03)
                    print("down")
            url = 'http://192.168.43.86:8090/'
            myobj = {'type':'nfc','tag':tag,'distance':d,'time':'6766767'}
            x = requests.post(url, data = myobj)

            time.sleep(1)
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()

def camera():
    while True:
        ret,frame = cam.read()
        cv2.imshow('frame',frame)

#cami = threading.Thread(target=camera)
#full = threading.Thread(target=code)
#cami.start()
#full.start()
#cami.join()
#full.join()
code()

