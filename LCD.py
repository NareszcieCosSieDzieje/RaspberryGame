from time import *
import MySQLdb

import I2C_LCD_driver
import BUTTON
import LEDS

#obiekty w ukladzie
mainLcd = I2C_LCD_driver.lcd() #3, 5
rightButton = BUTTONS.smallButton(24) 
centerButton = BUTTONS.smallButton(22) 
leftButton = BUTTONS.smallButton(18)
mainButton = BUTTONS.bigButton(12, 16)
leds = LEDS.RGB();

# do lcd backlight?
score = 0
choice = 0
current_line = 0
mainLcd.lcd_clear()
timer = time.time()
while True:	
	if current_line == 0:
		if mainButton.getState() == 1:
			choice = 0
			break
		if rightButton.getState() == 1:
			current_line = 1
		if time.time()-timer > 0.25:
			mainLcd.lcd_display_string(" -> Add a new user.", 1, 0)
		if time.time()-timer > 0.5:		
			timer = time.time()
		sleep(0.02)
		mainLcd.lcd_display_string("Use an existing user.", 2, 0)
	elif current_line == 1:
		if mainButton.getState() == 1:
			choice = 1
			break
		if leftButton.getState() == 1:
			current_line = 0
		mainLcd.lcd_display_string("Add a new user.", 1, 0)
		sleep(0.02)
		if time.time()-timer > 0.24:
			mainLcd.lcd_display_string(" -> Use an existing user.", 2, 0)
		if time.time()-timer_a > 0.5:		
			timer = time.time()

mainLcd.lcd_clear()

db = MySQLdb.connect("localhost", "game", "password", "players") #TODO: password change?
curs=db.cursor()

#SCOOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRRRRRRRRIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNGGGGGGGGGGGG !!!!!!!!!!!
# ZAPISUJ NAJWYZSZE!!!!!!!!!!!!!!!!!!!

last_id = 0

if choice == 0:
	with db:
		curs.execute("INSERT INTO players (score, tdate) values(0, CURRENT_DATE())")
		last_id = cursor.lastrowid
		mainLcd.lcd_display_string("Added player" + str(last_id), 1, 0)
		timer = time.time()
		while time.timer() - timer < 1.0
			pass
elif choice == 1:
	hasChoice = True
	records = curs.fetchall()
	recLen = len(records)
	iter = 0
	timer = time.time()
	if recLen == 0:
		hasChoice = False
		mainLcd.lcd_display_string("No players to", 1, 0)
		mainLcd.lcd_display_string("choose from.", 2, 0)
		while time.time() - timer < 2.0:
			pass
		with db:
			curs.execute("INSERT INTO players (score, tdate) values(0, CURRENT_DATE())")
			last_id = cursor.lastrowid
			mainLcd.lcd_display_string("Added player" + str(last_id), 1, 0)
			timer = time.time()
			while time.timer() - timer < 1.0
				pass
	if hasChoice:
		mainLcd.lcd_clear()
		while time.time() - timer < 6.0:
			if time.time() - timer < 2:
				mainLcd.lcd_display_string("Left, right to", 1, 0)
				mainLcd.lcd_display_string("change player", 2, 0)
			elif time.time() - timer < 4:
				mainLcd.lcd_display_string("Middle to", 1, 0)
				mainLcd.lcd_display_string("delete player", 2, 0)
			else:
				mainLcd.lcd_display_string("Big to", 1, 0)
				mainLcd.lcd_display_string("choose player", 2, 0)	
		timer = time.time()
		while True:
			row = records[iter]
			mainLcd.lcd_display_string("Player id " + str(row[0]), 1, 0) #("Id = ", row[0], )
			if time.time() - timer < 1:
				#mainLcd.lcd_display_string("Player id " + str(row[0]), 1, 0)
				mainLcd.lcd_display_string("Best score " + str(row[1]), 2, 0)
			elif time.time() - timer < 2:
				#mainLcd.lcd_display_string("Player id: " + str(row[0]), 1, 0)
				mainLcd.lcd_display_string("Date " + str(row[2]), 2, 0)
			if centerButton.getState() == 1:
				#delete player 
				mainLcd.lcd_clear()
				mainLcd.lcd_display_string("Left -> delete", 1, 0)
				mainLcd.lcd_display_string("Right -> return", 2, 0)	
				while True:
					if leftButton.getState() == 1:
						sql = ("DELETE FROM players WHERE pID = %s")
						val = (row[iter]) 
						with db:
							curs.execute(sql, val)
							records = curs.fetchall()
							recLen = len(records)
						if recLen == 0:
							mainLcd.lcd_display_string("No players to", 1, 0)
							mainLcd.lcd_display_string("choose from.", 2, 0)
							timer = time.time()
							while time.time() - timer < 2.0:
								pass
							with db:
								curs.execute("INSERT INTO players (score, tdate) values(0, CURRENT_DATE())")
								last_id = cursor.lastrowid
								mainLcd.lcd_display_string("Added player" + str(last_id), 1, 0)
							timer = time.time()
							iter = 0
							while time.time() - timer < 1.0:
								pass 
						else:
							iter = iter - 1
						break
					elif rightButton.getState() == 1:
						break
			elif (leftButton.getState() == 1) and (iter > 0):
				iter = iter - 1
			elif (rightButton.getState() == 1) and (iter < recLen - 1):
				iter = iter + 1
			elif bigButton.getState() == 1:
				last_id = row[iter][0]
			
mainLcd.lcd_clear()

while True:
	for i in range(0,15):
		mainLcd.lcd_display_string("Press start.", i, 0)
		sleep(0.5)
		if mainButton.getState() == 1:
			timer_a = time.time()
			while time.time()-timer_a < 1:
				mainLcd.lcd_display_string("3...", 1, 0)
				sleep(0.1)
			while time.time()-timer_a < 2:
				mainLcd.lcd_display_string("2..", 1, 0)
				sleep(0.1)
			while time.time()-timer_a < 3:
				mainLcd.lcd_display_string("1.", 1, 0)
				sleep(0.1)
			break
			
mainLcd.lcd_clear()

win = 0

def gameLoop(speed):
	timer_a = time.time()
	timer_b = time.time()
	while True:
		#czerwona mroga z jakas Hz i swieci sie dany czas
		#kolejne sie zapalaja i swieca jakis czas
		#potem siodma sie naklada i razem mrogaja jakis czas
		
		if time.time() - timer_a < 1.5/speed:  
			leds.setRed(1)
		elif time.time() - timer_a < 2.0/speed:  
			leds.setOffRed()
		else: #time.time() - timer_a
			timer_a = time.time()
		
		if time.time() - timer_b < 0.5/speed :
			leds.setBlue(2)
			win = 0
		elif time.time() - timer_b < 1.0/speed :
			leds.setBlue(3)
		elif time.time() - timer_b < 1.5/speed :
			leds.setBlue(4)
			win = 0
		elif time.time() - timer_b < 2.0/speed :
			leds.setBlue(5)
			win = 0
		elif time.time() - timer_b < 2.5/speed :
			leds.setBlue(6)
			win = 0
		elif time.time() - timer_b < 3.0/speed :
			leds.setBlue(7)
			win = 0
		elif time.time() - timer_b < 3.5/speed :
			leds.setBlue(1)
			win = 1
		else:
			timer_b = time.time()
		if mainButton.getState() == 1:
			break
	
	
def alternativeGameLoop1(speed):
	timer_b = time.time()
	leds.setRed(1)
	while True:			
		if time.time() - timer_b < 0.5/speed :
			leds.setBlue(2)
			win = 0
		elif time.time() - timer_b < 1.0/speed :
			leds.setBlue(3)
		elif time.time() - timer_b < 1.5/speed :
			leds.setBlue(4)
			win = 0
		elif time.time() - timer_b < 2.0/speed :
			leds.setBlue(5)
			win = 0
		elif time.time() - timer_b < 2.5/speed :
			leds.setBlue(6)
			win = 0
		elif time.time() - timer_b < 3.0/speed :
			leds.setBlue(7)
			win = 0
		elif time.time() - timer_b < 3.5/speed :
			leds.setBlue(1)
			win = 1
		else:
			timer_b = time.time()
			
		if mainButton.getState() == 1:
			break
			
def alternativeGameLoop2(speed):
	timer_a = time.time()
	timer_b = time.time()
	set = True
	while True:			
		
		if time.time() - timer_a > 0.1:
			if !set:
				leds.setRed(1)
			else:
				leds.setOffRed()
			timer_a = time.time()	
		
		if time.time() - timer_b < 0.5/speed :
			leds.setBlue(2)
			win = 0
		elif time.time() - timer_b < 1.0/speed :
			leds.setBlue(3)
		elif time.time() - timer_b < 1.5/speed :
			leds.setBlue(4)
			win = 0
		elif time.time() - timer_b < 2.0/speed :
			leds.setBlue(5)
			win = 0
		elif time.time() - timer_b < 2.5/speed :
			leds.setBlue(6)
			win = 0
		elif time.time() - timer_b < 3.0/speed :
			leds.setBlue(7)
			win = 0
		elif time.time() - timer_b < 3.5/speed :
			leds.setBlue(1)
			win = 1
		else:
			timer_b = time.time()
			
		if mainButton.getState() == 1:
			break
	
lvl = level = 0
timer_a = time.time()
for lvl in range(1,3)
	gameLoop(lvl)
	if win == 0:
		level = lvl - 1
		timer_b = time_time()
		break
		
mainLcd.lcd_display_string("Got to level: " + str(lvl) + "and" + str(text = "won" if win == 1 else "lost" )

score = (level*100)/(timer_b-timer_a) 

sql = ("UPDATE players SET score = %s, tdate = CURRENT_DATE() WHERE pID = %s")
val = (score, last_id) 
with db:
	curs.execute(sql, val)

db.commit()
db.close()

GPIO.cleanup() 
