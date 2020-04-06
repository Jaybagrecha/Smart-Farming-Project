import RPi.GPIO as gpio
import RPi.GPIO as gpio
import time
from firebase import firebase
firebase = firebase.FirebaseApplication('https://farm-2981b.firebaseio.com/')


level1=31
level2=33
level3=35
buzzer=37

gpio.setmode(gpio.BOARD)
gpio.setup(buzzer,gpio.OUT)


while(1):
    gpio.setup(level1,gpio.IN)
    gpio.setup(level2,gpio.IN)
    gpio.setup(level3,gpio.IN)

    
    if(gpio.input(level1)==True and gpio.input(level2)==False):
        gpio.setup(level2,gpio.OUT)
        gpio.setup(level3,gpio.OUT)
        gpio.setup(level2,gpio.LOW)
        gpio.setup(level3,gpio.LOW)
        perc=30;
        p=str(perc)
        firebase.put('/Farm/Irrigation','WaterLevel',p)
        print("Water :"+p)
        time.sleep(2)
    elif(gpio.input(level2)==True and gpio.input(level3)==False):
        gpio.setup(level1,gpio.OUT)
        gpio.setup(level3,gpio.OUT)
        gpio.setup(level1,gpio.LOW)
        gpio.setup(level3,gpio.LOW)
        perc=50;
        p=str(perc)
        firebase.put('/Farm/Irrigation','WaterLevel',p)
        print("Water :"+p)
        time.sleep(2)
    elif(gpio.input(level3)==True):
        gpio.setup(level1,gpio.OUT)
        gpio.setup(level2,gpio.OUT)
        gpio.setup(level1,gpio.LOW)
        gpio.setup(level2,gpio.LOW)
        perc=80;
        p=str(perc)
        firebase.put('/Farm/Irrigation','WaterLevel',p)
        print("Water :"+p)
        time.sleep(2)
    else:
        gpio.setup(level1,gpio.OUT)
        gpio.setup(level2,gpio.OUT)
        gpio.setup(level3,gpio.OUT)
        gpio.setup(level1,gpio.LOW)
        gpio.setup(level2,gpio.LOW)
        gpio.setup(level3,gpio.LOW)
        perc=10;
        p=str(perc)
        firebase.put('/Farm/Irrigation','WaterLevel',p)
        print("No Water")
        time.sleep(1)
    
gpio.cleanup()



