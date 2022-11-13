from machine import Pin
import time

red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)

while True:
    red.value(1)
    green.value(0)
    time.sleep(1)
    
    red.value(0)
    green.value(1)
    time.sleep(1)
    
    red.value(1)
    green.value(1)
    time.sleep(1)
    
    red.value(0)
    green.value(0)
    time.sleep(1)