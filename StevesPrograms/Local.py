#!/usr/bin/python
# Filename: LocalExample.py
# MiloCreek JS MiloCreek
# Version 1.1 4/8/13
#
# Local Execute Objects for RasPiConnect  
# to add Execute objects, modify this file 
#
#
#
# RasPiConnectServer interface constants

REMOTE_WEBVIEW_UITYPE = 1
ACTION_BUTTON_UITYPE = 16
FEEDBACK_ACTION_BUTTON_UITYPE = 17
SINGLE_LED_DISPLAY = 32
SPEEDOMETER_UITYPE = 64
VOLTMETER_UITYPE = 128
SERVER_STATUS_UITYPE = 256
PICTURE_REMOTE_WEBVIEW_UITYPE = 512
LABEL_UITYPE = 1024
FM_BLINK_LED_UITYPE = 2048
TEXT_DISPLAY_UITYPE = 4096
TOGGLE_SWITCH_UITYPE = 33
SEND_TEXT_UITYPE = 34

# system imports
import sys
import subprocess

# RasPiConnectImports

import Config
import Validate
import BuildResponse 

#  Raspi Robot imports
from raspirobotboard import *
led1State = False
led2State = False
forwardState = False
rearState = False

rr = RaspiRobot()

rr.set_led1(False)
rr.set_led2(False)

# camera imports
import os

def ExecuteUserObjects(objectType, element):

	global led1State
	global led2State
	global forwardState
	global rearState
	global rr

	# Example Objects

	# fetch information from XML for use in user elements

	#objectServerID is the RasPiConnect ID from the RasPiConnect App

        objectServerID = element.find("./OBJECTSERVERID").text
        objectID = element.find("./OBJECTID").text

        if (Config.debug()):
        	print("objectServerID = %s" % objectServerID)
	# 
	# check to see if this is a Validate request
	#
        validate = Validate.checkForValidate(element)

        if (Config.debug()):
        	print "VALIDATE=%s" % validate

        
	# Build the header for the response

	outgoingXMLData = BuildResponse.buildHeader(element)


	# objects are split up by object types by Interface Constants
	#
	#
	#
	# search for matches to object Type 

	# object Type match
	if (objectType == ACTION_BUTTON_UITYPE):
		#print "ACTION_BUTTON_UTYPE of %s found" % objectServerID

		if (Config.debug()):
			print "ACTION_BUTTON_UTYPE of %s found" % objectServerID

		# B-2 - play a beep on the Raspberry Pi
		if (objectServerID == "B-2"):	

                	#check for validate request
			# validate allows RasPiConnect to verify this object is here 
                	if (validate == "YES"):
                        	outgoingXMLData += Validate.buildValidateResponse("YES")
                        	outgoingXMLData += BuildResponse.buildFooter()
                        	return outgoingXMLData

			# not validate request, so execute

			# note that python is in the main directory for this call, not the local directory

			output = subprocess.call(["aplay", "sounds/match1.wav"])
			
			responseData = "OK"
                	outgoingXMLData += BuildResponse.buildResponse(responseData)
      			outgoingXMLData += BuildResponse.buildFooter()
                	return outgoingXMLData
		elif (objectServerID == "B-4"):	
	          #print "button B-4"

                  #check for validate request
                  if (validate == "YES"):
                        outgoingXMLData += Validate.buildValidateResponse("YES")
                        outgoingXMLData += BuildResponse.buildFooter()

                        return outgoingXMLData

                  if(led1State):
                    led1State=False
		    responseData = "OFF"
		    rr.set_led1(False)
		    rr.stop()
		    #print "led1 true"
		  else:
                    led1State=True
		    responseData = " ON"
		    rr.set_led1(True)
		    rr.right()
		    #print "led1 false"
		  responseData = "OK"
                  outgoingXMLData += BuildResponse.buildResponse(responseData)
      		  outgoingXMLData += BuildResponse.buildFooter()
                  return outgoingXMLData
		elif (objectServerID == "B-5"):	
	          #print "button B-5"

                  #check for validate request
                  if (validate == "YES"):
                        outgoingXMLData += Validate.buildValidateResponse("YES")
                        outgoingXMLData += BuildResponse.buildFooter()

                        return outgoingXMLData

                  if(led2State):
                    led2State=False
		    responseData = "OFF"
		    rr.set_led2(False)
		    rr.stop()
		    #print "led2 true"
		  else:
                    led2State=True
		    responseData = " ON"
		    rr.set_led2(True)
		    rr.left()
		    #print "led2 false"
		  responseData = "OK"
                  outgoingXMLData += BuildResponse.buildResponse(responseData)
      		  outgoingXMLData += BuildResponse.buildFooter()
                  return outgoingXMLData		
		elif (objectServerID == "B-6"):	
		  #forwards
	          #print "button B-4"

                  #check for validate request
                  if (validate == "YES"):
                        outgoingXMLData += Validate.buildValidateResponse("YES")
                        outgoingXMLData += BuildResponse.buildFooter()

                        return outgoingXMLData

                  if(forwardState):
                    forwardState=False
		    responseData = "OFF"
		    rr.set_led1(False)
		    rr.set_led2(False)
		    rr.stop()
		    #print "forward true"
		  else:
                    forwardState=True
		    responseData = " ON"
		    rr.set_led1(False)
		    rr.set_led2(False)
		    rr.forward()
		    #print "forward false"
		  responseData = "OK"
                  outgoingXMLData += BuildResponse.buildResponse(responseData)
      		  outgoingXMLData += BuildResponse.buildFooter()
                  return outgoingXMLData
		elif (objectServerID == "B-7"):	
		  # rear
	          #print "button B-7"

                  #check for validate request
                  if (validate == "YES"):
                        outgoingXMLData += Validate.buildValidateResponse("YES")
                        outgoingXMLData += BuildResponse.buildFooter()

                        return outgoingXMLData

                  if(rearState):
                    rearState=False
		    responseData = "OFF"
		    rr.set_led1(False)
		    rr.set_led2(False)
		    rr.stop()
		    #print "led2 true"
		  else:
                    rearState=True
		    responseData = " ON"
		    rr.set_led1(True)
		    rr.set_led2(True)
		    rr.reverse()
		    #print "led2 false"
		  responseData = "OK"
                  outgoingXMLData += BuildResponse.buildResponse(responseData)
      		  outgoingXMLData += BuildResponse.buildFooter()
                  return outgoingXMLData	
		elif (objectServerID == "B-8"):	
		  # rear
	          #print "button B-8"

                  #check for validate request
                  if (validate == "YES"):
                        outgoingXMLData += Validate.buildValidateResponse("YES")
                        outgoingXMLData += BuildResponse.buildFooter()

                        return outgoingXMLData
		  rr.stop()
		  os.system("sudo shutdown -h now")
		  responseData = "OK"
                  outgoingXMLData += BuildResponse.buildResponse(responseData)
      		  outgoingXMLData += BuildResponse.buildFooter()
                  return outgoingXMLData	

	elif (objectServerID == "W-2"):
			if (validate == "YES"):
				outgoingXMLData += Validate.buildValidateResponse("YES")
				outgoingXMLData += BuildResponse.buildFooter()
				return outgoingXMLData
			
			os.system("raspistill -o static/camImage.jpg -t 0")	
			imageName = "camImage.jpg"	

			responseData = "<html><head>"
			responseData += "<title></title><style>body,html,iframe{margin:0;padding:0;}</style>"
			responseData += "</head>"	
			responseData += "<body><img src=\""
 			responseData += Config.localURL()
 			responseData += "static/"
			responseData += imageName
			responseData += "\" type=\"jpg\" width=\"300\" height=\"300\">"
			responseData += "<BR>Picture<BR>"
			responseData +="</body>static"		
			responseData += "</html>"		
			outgoingXMLData += BuildResponse.buildResponse(responseData)
      		  	outgoingXMLData += BuildResponse.buildFooter()
	                return outgoingXMLData			

        		if (Config.debug()):
				print outgoingXMLData	
	elif (objectServerID == "FB-1"):	
		# do a toggle
		print "FB-1"

                #check for validate request
                if (validate == "YES"):
                        outgoingXMLData += Validate.buildValidateResponse("YES")
                        outgoingXMLData += BuildResponse.buildFooter()
                        return outgoingXMLData	


		responseData = "False"
		if (rr.sw1_closed()):
		  responseData = "True "

	
                outgoingXMLData += BuildResponse.buildResponse(responseData)
 	  	outgoingXMLData += BuildResponse.buildFooter()
                return outgoingXMLData	
	else:
		return ""
	# returning a zero length string tells the server that you have not matched 
	# the object and server 
	return ""

rr=RaspiRobot()
rr.set_led1(False)
rr.set_led2(False)

