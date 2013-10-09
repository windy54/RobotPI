#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# wii_remote_1.py
# Connect a Nintendo Wii Remote via Bluetooth
# and  read the button states in Python.
#
# Project URL :
# http://www.raspberrypi-spy.co.uk/?p=1101
#

import cwiid
import time
import os

import sys
import pyttsx

from raspirobotboard import *

button_delay = 0.1


# Connect to the Wii Remote. If it times out
# then quit.
wii = None
i = 2

engine = pyttsx.init()  

rr = RaspiRobot()
rr.set_led1(False)
rr.set_led2(False)

engine.say("get ready to connect")
engine.runAndWait()

# flash led to indicate get ready to connect
while i<10:
    if ( (i%2)==0):
      rr.set_led1(True)
      rr.set_led2(False)  
    else:   
      rr.set_led1(False)
      rr.set_led2(True)
    i+=1
    time.sleep(1)


engine.say("Press 1 and 2")
engine.runAndWait()



# now 10 attempts to connect again flash the led
i=0
while not wii:
  try:
    wii=cwiid.Wiimote()
  except RuntimeError:
    if (i>10):
      engine.say("Error opening wiimote connection")
      engine.runAndWait()
      quit()
      break
    if ( (i%2)==0):
      rr.set_led1(True)
      rr.set_led2(False)  
    else:   
      rr.set_led1(False)
      rr.set_led2(True)
    i+=1
    engine.say(str(i))
    engine.runAndWait()

# rumble to indicate connected
engine.say("Connected")
engine.runAndWait()

wii.rumble = 1
time.sleep(1)
wii.rumble = 0

wii.rpt_mode = cwiid.RPT_BTN

 
rr.set_led1(False)
rr.set_led2(False)
outputReversing = False

while True:
  buttons = wii.state['buttons']
  # If Plus and Minus buttons pressed
  # together then rumble and quit and shutdown PI.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    #print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    engine.say("Bye")
    engine.runAndWait()
    os.system("sudo shutdown -h now")
    exit(wii) 
  elif (buttons & cwiid.BTN_UP):
     rr.forward()
     rr.set_led1(False)
     rr.set_led2(False)
  elif (buttons & cwiid.BTN_DOWN):
     if outputReversing == False:
        engine.say("Reversing")
        engine.runAndWait()
        outputReversing = True
     rr.set_led1(True)
     rr.set_led2(True)
     rr.reverse()
  elif (buttons & cwiid.BTN_RIGHT):
     rr.set_led1(False)
     rr.set_led2(True)
     rr.right()
  elif (buttons & cwiid.BTN_LEFT):
     rr.set_led1(True)
     rr.set_led2(False)
     rr.left()
  elif (buttons - cwiid.BTN_PLUS - cwiid.BTN_B ==0):
     engine.say(" stopping program only")
     engine.runAndWait()
     quit()
  else:
     rr.stop()
     rr.set_led1(False)
     rr.set_led2(False)
     outputReversing = False


