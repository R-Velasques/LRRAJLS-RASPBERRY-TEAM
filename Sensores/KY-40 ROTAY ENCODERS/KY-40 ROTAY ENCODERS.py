import board
import digitalio

dirPin = digitalio.DigitalInOut(board.GP16)
stePin = digitalio.DigitalInOut(board.GP17)
dirPin.direction  = digitalio.Direction.INPUT
stepPin.direction = digitalio.Direction.INPUT

dirPin.pull = digitalio.Pull.UP
stepPin.pull = digitalio.Pull.UP
previousValue = True
while 1==1:
  if previousValue != stepPin.value:
      if stepPin.value == False:
          if dirPin.value == False:
              print("A la izquierda, a al izquierda!")
          else:
              print("A la derecha,a la derecha")
      previousValue = stepPin.value