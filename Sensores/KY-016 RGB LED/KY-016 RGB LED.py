from machine import Pin,PWM
import utime
import random

#asignamos los puertos a utilizar a variables
Led_R = PWM(Pin(2))
Led_G = PWM(Pin(3))
Led_B = PWM(Pin(4))

# Definimos la frecuencia de cada pin
Led_R.freq(2000)
Led_G.freq(2000)
Led_B.freq(2000)
if name == "main":
 while True:
     # Creamos tres variables a la cual le asignamos rango de numeros aleatorios
     R=random.randint(0,65535)
     G=random.randint(0,65535)
     B=random.randint(0,65535)

     #asignamos la variable con el numero aleatorio a la funcion duty de cada pin para poder controlar el ciclo de trabajo y agregar cierta cantidad de R,G o B al led
     Led_R.duty_u16(R)
     Led_G.duty_u16(G)
     Led_B.duty_u16(B)

     #Establecemos una pausa de 100 milisegundis
     utime.sleep_ms(100)