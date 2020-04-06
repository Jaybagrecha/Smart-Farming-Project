import RPi.GPIO as GPIO
import time
from firebase import firebase

firebase = firebase.FirebaseApplication('https://farm-2981b.firebaseio.com/')

in1 = 10
in2 = 12
en = 8
water=40
temp1=1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(en,GPIO.HIGH)
GPIO.output(in2,GPIO.HIGH)

GPIO.setup(water, GPIO.IN)



p=GPIO.PWM(en,100)
p.start(0)
x=0


while(True):
    
    p=GPIO.PWM(en,200)
    
    while(1):
        x=firebase.get('/Farm/Irrigation/system',None)
        if(x==1):
            #GPIO.output(in1,GPIO.HIGH)
            #GPIO.output(in2,GPIO.LOW)
            p.start(50)
            #x=firebase.get('/Farm/Irrigation/system',None)
            if(GPIO.input(water)==True):
                x=0
                p.stop()
                firebase.put('/Farm/Irrigation','Moisture','1')
                firebase.put('/Farm/Irrigation','system','0')
                break
            else:
                x=1
                firebase.put('/Farm/Irrigation','Moisture','1')
            
            #time.sleep(0.1)
            #while(True):
                #x=firebase.get('/Farm/Irrigation/system',None)
                #if(x==0):
                    #p.stop()
                    #break
        elif(x==0):
            #GPIO.output(in1,GPIO.HIGH)
            #GPIO.output(in2,GPIO.LOW)
            p.stop()
            break
            #time.sleep(0.1)
            #while(True):
                #x=firebase.get('/Farm/Irrigation/system',None)
                #if(x==1):
                    #p.start(40)
                    #break

        else:
            x=firebase.get('/Farm/Irrigation/system',None)
            break
            
            
p.stop()
GPIO.cleanup()


        