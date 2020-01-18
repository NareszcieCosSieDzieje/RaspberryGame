# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO 

def class smallButton:
	
	def __init__(self, pin):
		self.pin = pin
		GPIO.setwarnings(False) # Ignore warning for now
		GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
		GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin to be an input pin and set initial value to be pulled UP (high)
		
	def getState(self):
		if GPIO.input(self.pin) == GPIO.LOW:
			return 1
		elif GPIO.input(self.pin) == GPIO.HIGH:
			return 0
			
def class bigButton():

	def __init__(self, pin1, pin2):
		self.pushPin = pin1
		self.ledPin = pin2
		GPIO.setwarnings(False) # Ignore warning for now
		GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
		GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin to be an input pin and set initial value to be pulled UP (high)
		GPIO.setup(pin, GPIO.OUT, pull_up_down=GPIO.PUD_UP) # Set pin to be an input pin and set initial value to be pulled UP (high)
		
	def getState(self):
		if GPIO.input(self.pushPin) == GPIO.LOW:
			return 1
		elif GPIO.input(self.pushPin) == GPIO.HIGH:
			return 0
			