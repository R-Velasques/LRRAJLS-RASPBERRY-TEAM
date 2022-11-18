from machine import Pin
import time

ReedSensor = Pin(18, Pin.IN)
while True:
    value = ReedSensor.value()
    print(value, end = " ")
    if value == 0:
        print("Sin Campo Magnetico")
    else:
        print("Campo Magnetico")
    time.sleep(0.5)
