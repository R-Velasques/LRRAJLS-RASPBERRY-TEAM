from machine import Pin, PWM
from time import sleep

buzzerPIN=16
BuzzerObj=PWM(Pin(buzzerPIN))

def buzzer(buzzerPinObject,frequency,sound_duration,silence_duration):

    buzzerPinObject.duty_u16(int(65536*0.2))
    buzzerPinObject.freq(frequency)
    sleep(sound_duration)
    buzzerPinObject.duty_u16(int(65536*0))
    sleep(silence_duration)

buzzer(BuzzerObj,523,0.5,0.1)
buzzer(BuzzerObj,587,0.5,0.1)

buzzer(BuzzerObj,659,0.5,0.1) #E (MI)
buzzer(BuzzerObj,698,0.5,0.1) #F (FA)

buzzer(BuzzerObj,784,0.5,0.1) #G (SOL)
buzzer(BuzzerObj,880,0.5,0.1) #A (LA)
buzzer(BuzzerObj,987,0.5,0.1) #B (SI)