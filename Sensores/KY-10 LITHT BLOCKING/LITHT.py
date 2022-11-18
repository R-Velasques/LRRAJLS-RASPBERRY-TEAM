import machine
import time
  
machine.setmode(machine.BCM)
  

machine_PIN = 21
machine.setup(machine_PIN, GPIO.IN, pull_up_down = machine.PUD_DOWN)
  
print "KY-010 Sensor Test [press ctrl+c to end the test]"
  
def outputFunction(null):
        print("Sensor is blocked")
  


machine.add_event_detect(machine_PIN, GPIO.RISING, callback=outputFunction, bouncetime=100) 
  


try:
        while True:
                time.sleep(1)
  


except KeyboardInterrupt:
        machine.cleanup()