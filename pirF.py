import RPi.GPIO as GPIO
import time
from firebase import firebase

firebase = firebase.FirebaseApplication('https://farm-2981b.firebaseio.com/')
    
PIR_input1 = 16  #read PIR Output
PIR_input2 = 26
buzz=37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)    #choose pin no. system
GPIO.setup(PIR_input1, GPIO.IN)
GPIO.setup(PIR_input2, GPIO.IN)
GPIO.setup(buzz, GPIO.OUT)
GPIO.output(buzz, GPIO.LOW)
while True:
    s=firebase.get('/Farm/Boundry/system',None)
    if(s==1):    
        if(GPIO.input(PIR_input2)==True or GPIO.input(PIR_input1)==True):
            print("ANIMAL DETECTED")
            GPIO.output(buzz, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(buzz, GPIO.LOW)
            firebase.put('/Farm/Boundry','Detect',1)
        else:
            print("SAFE")
            firebase.put('/Farm/Boundry','Detect',0)
            #GPIO.output(buzz, GPIO.LOW)
            #time.sleep(0.01)        
gpio.cleanup()
