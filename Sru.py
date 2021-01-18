import time as t
import mini_driver as md
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO_Trigger = 18
GPIO_Echo = 17
GPIO.setup(GPIO_Trigger,GPIO.OUT)
GPIO.setup(GPIO_Echo,GPIO.IN)

def disi():
    GPIO.output(GPIO_Trigger,GPIO.HIGH)
    t.sleep(0.00001)
    GPIO.output(GPIO_Trigger,GPIO.LOW)
    StZ = t.time()
    SpZ = t.time()

    while GPIO.input(GPIO_Echo) == 0:
        StZ = t.time()

    while GPIO.input(GPIO_Echo) == 1:
        SpZ = t.time()

    ZU = SpZ - StZ
    cm = (ZU*34300)/2

    return cm

miniDriver = md.MiniDriver()
connect = miniDriver.connect()
tims =0
try:
    while tims <10:
        tims +=1
        a=disi()
        print(a)
        t.sleep(0.5)
        b=disi()
        print(b)
        t.sleep(0.5)
        c=disi()
        print(c)
        allS=(a+b+c)/3
        d=allS/27.8
        print(allS)
        print(d)
        if allS < 20:
            print("rechts")
            miniDriver.setOutputs(50,50,50,50)
            t.sleep(0.5) #etwa 90 Grad
            miniDriver.setOutputs(0,0,50,50)
        else:
            print("grade aus")
            miniDriver.setOutputs(50,-50,50,50)
            print(d)
	    ds = 0.0 
            ds = d-1.00
            t.sleep(ds)
            miniDriver.setOutputs(0,0,50,50)
except KeyboardInterrupt:
    miniDriver.disconnect()
    del miniDriver
    GPIO.cleanup()
    
miniDriver.disconnect()
del miniDriver
GPIO.cleanup()
print("service robot_web_server stop")#Stop Web Lib
