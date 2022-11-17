import time
from machine import Pin
from ir import NEC_16

def callback(data, addr, ctrl):
    if data > 0:  
        print('Data {:02x} Addr {:04x}'.format(data, addr))

ir = NEC_16(Pin(28, Pin.IN), callback)