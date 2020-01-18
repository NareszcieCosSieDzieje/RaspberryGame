import RPi.GPIO as GPIO 

class RGB:
	#odpowiednie piny
	INH1 = 19 #czerwone
	A1 = 29
	B1 = 23
	C1 = 21
	INH2 = 31 #niebieskie
	A2 = 37
	B2 = 35
	C2 = 33
	INH3 = 7 #zielone
	A3 = 15
	B3 = 13
	C3 = 11
	LED1 = (0,0,0)
	LED2 = (1,0,0)
	LED3 = (0,1,0)
	LED4 = (1,1,0)
	LED5 = (0,0,1)
	LED6 = (1,0,1)
	LED7 = (0,1,1)
	
	def _init_(self):
		GPIO.setwarnings(False) # Ignore warning for now
		GPIO.setmode(GPIO.BOARD) 
		GPIO.setup(INH1, GPIO.OUT, initial=1)
		GPIO.setup(INH2, GPIO.OUT, initial=1)
		GPIO.setup(INH3, GPIO.OUT, initial=1)
		GPIO.setup(A1, GPIO.OUT, initial=0)
		GPIO.setup(B1, GPIO.OUT, initial=0)
		GPIO.setup(C1, GPIO.OUT, initial=0)
		GPIO.setup(A2, GPIO.OUT, initial=0)
		GPIO.setup(B2, GPIO.OUT, initial=0)
		GPIO.setup(C2, GPIO.OUT, initial=0)
		GPIO.setup(A3, GPIO.OUT, initial=0)
		GPIO.setup(B3, GPIO.OUT, initial=0)
		GPIO.setup(C3, GPIO.OUT, initial=0)
		
	
	def setRed(self, num):
		GPIO.output(INH1, 0)  
		if num == 1:
			GPIO.output(A1, LED1[0])
			GPIO.output(B1, LED1[1])
			GPIO.output(C1, LED1[2])
		elif num == 2:
			GPIO.output(A1, LED2[0])
			GPIO.output(B1, LED2[1])
			GPIO.output(C1, LED2[2])
		elif num == 3:
			GPIO.output(A1, LED3[0])
			GPIO.output(B1, LED3[1])
			GPIO.output(C1, LED3[2])
		elif num == 4:
			GPIO.output(A1, LED4[0])
			GPIO.output(B1, LED4[1])
			GPIO.output(C1, LED4[2])
		elif num == 5:
			GPIO.output(A1, LED5[0])
			GPIO.output(B1, LED5[1])
			GPIO.output(C1, LED5[2])
		elif num == 6:
			GPIO.output(A1, LED6[0])
			GPIO.output(B1, LED6[1])
			GPIO.output(C1, LED6[2])
		elif num == 7:
			GPIO.output(A1, LED7[0])
			GPIO.output(B1, LED7[1])
			GPIO.output(C1, LED7[2])	
	
	def setBlue(self, num):
		GPIO.output(INH2, 0)  
		if num == 1:
			GPIO.output(A2, LED1[0])
			GPIO.output(B2, LED1[1])
			GPIO.output(C2, LED1[2])
		elif num == 2:
			GPIO.output(A2, LED2[0])
			GPIO.output(B2, LED2[1])
			GPIO.output(C2, LED2[2])
		elif num == 3:
			GPIO.output(A2, LED3[0])
			GPIO.output(B2, LED3[1])
			GPIO.output(C2, LED3[2])
		elif num == 4:
			GPIO.output(A2, LED4[0])
			GPIO.output(B2, LED4[1])
			GPIO.output(C2, LED4[2])
		elif num == 5:
			GPIO.output(A2, LED5[0])
			GPIO.output(B2, LED5[1])
			GPIO.output(C2, LED5[2])
		elif num == 6:
			GPIO.output(A2, LED6[0])
			GPIO.output(B2, LED6[1])
			GPIO.output(C2, LED6[2])
		elif num == 7:
			GPIO.output(A2, LED7[0])
			GPIO.output(B2, LED7[1])
			GPIO.output(C2, LED7[2])	
		
	
	def setGreen(self, num):
		GPIO.output(INH3, 0)  
		if num == 1:
			GPIO.output(A3, LED1[0])
			GPIO.output(B3, LED1[1])
			GPIO.output(C3, LED1[2])
		elif num == 2:
			GPIO.output(A3, LED2[0])
			GPIO.output(B3, LED2[1])
			GPIO.output(C3, LED2[2])
		elif num == 3:
			GPIO.output(A3, LED3[0])
			GPIO.output(B3, LED3[1])
			GPIO.output(C3, LED3[2])
		elif num == 4:
			GPIO.output(A3, LED4[0])
			GPIO.output(B3, LED4[1])
			GPIO.output(C3, LED4[2])
		elif num == 5:
			GPIO.output(A3, LED5[0])
			GPIO.output(B3, LED5[1])
			GPIO.output(C3, LED5[2])
		elif num == 6:
			GPIO.output(A3, LED6[0])
			GPIO.output(B3, LED6[1])
			GPIO.output(C3, LED6[2])
		elif num == 7:
			GPIO.output(A3, LED7[0])
			GPIO.output(B3, LED7[1])
			GPIO.output(C3, LED7[2])		
		
		def setOffRed(self):
			if GPIO.input(INH1): 
				GPIO.output(INH1, 1)  
				
		def setOffBlue(self):
			if GPIO.input(INH2): 
				GPIO.output(INH2, 1)  
				
		def setOffGreen(self):
			if GPIO.input(INH3): 
				GPIO.output(INH3, 1)  
				