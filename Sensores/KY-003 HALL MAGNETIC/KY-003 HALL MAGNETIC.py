import utime

sensor=Pin(26, Pin.IN)
utime.sleep(1)

while True:
   if sensor.value()==1:
       print("Ningun campo detectado")
       utime.sleep(1)
   else:
       print("Campo magnetico detectado")
       utime.sleep(1)
utime.sleep(1)