# This script takes input from the potentiometer on an Arduino Uno board to manipulate a cylinder length in VPython
# This requires upload of sketch_feb04a_pot_servo to the Arduino before running

import serial
from visual import *

# upload sketch_feb04a_pot_servo to Arduino before running

arduinoSerialData = serial.Serial('/dev/cu.usbmodem1411', 9600)  # set input from Arduino serial port
#measuringRod = cylinder(title="MyCyli", radius =.5, length=1, color=color.magenta, pos=(-10,-2,0))  # define cylinder visual python
spring = helix(pos=(0,2,1), axis=(5,0,0), radius=5, color=color.green, length=1, coils=7)
lengthlabel = label(pos=(0, 10, 0), text='Helix length is: ', box=True, height=20)


while 1 == 1:  # Loop FOREVER
    rate(20)  # tell vpython to run this loop 20x/sec
    if (arduinoSerialData.inWaiting() > 0):  # check if data available from Arduino
        myData = arduinoSerialData.readline()  # read the data from serial connection
        print myData
        distance = float(myData)  # convert myData to float type
        spring.length=distance  # change the length of the object based on input from potentiometer
        ## change color based on stretch distance
        if distance <= 3:
            spring.color=color.blue
        elif 3 < distance <= 10:
            spring.color=color.green
        elif 10 < distance <= 17:
            spring.color=color.orange
        else:
            spring.color=color.red
        myLabel = "Stretch the spring. The length is now: " + myData
        lengthlabel.text = myLabel

