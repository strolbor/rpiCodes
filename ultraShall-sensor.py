#Bibliotheken einbinden
import RPi.GPIO as GPIO
import time
 
#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#GPIO Pins zuweisen
GPIO_TRIGGER = 18
GPIO_ECHO = 17
 
#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distanz():
    # setze Trigger auf HIGH
    GPIO.output(GPIO_TRIGGER, GPIO.HIGH)
 
    # setze Trigger nach 0.01ms aus LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, GPIO.LOW)
 
    StartZeit = time.time()
    StopZeit = time.time()
    #print("1")
    # speichere Startzeit
    while GPIO.input(GPIO_ECHO) == 0:
        StartZeit = time.time()
        #print("start")
    #print("2")
    # speichere Ankunftszeit
    while GPIO.input(GPIO_ECHO) == 1:
        StopZeit = time.time()
        #print("atop")

    # Zeit Differenz zwischen Start und Ankunft
    TimeElapsed = StopZeit - StartZeit
    print(TimeElapsed)
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    distanz = (TimeElapsed * 34300) / 2
 
    return distanz
 
if __name__ == '__main__':
    try:
        while True:
            abstand = distanz()
            print ("Gemessene Entfernung = %.1f cm" % abstand)
	    me=abstand/100
	    print(me)
            time.sleep(1)
 
        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        GPIO.cleanup()

