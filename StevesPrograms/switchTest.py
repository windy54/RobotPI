from raspirobotboard import *

rr = RaspiRobot()

switchState= rr.sw1_closed()

if (switchState):
  print "switch closed"
else:
  print "switch opn"
  