## GABRIEL JAMES GOENAWAN U1920061F

maxplayer = 3 #I've only included the asset for player 1-5, so errors will occur if maxplayer is more than 5.

import random
import os
import time
import turtle
from turtle import *
from threading import Thread
import threading

#Detect Operating System & setting up CMD window
if os.name == "nt":
	clear = lambda: os.system('cls') ## for windows system
	os.system('@echo off')
	os.system('mode con: cols=50 lines=5')
else:
	print("Your operating system isn't supported. Please use windows to run this program.")
	exit()
clear()
os.system('color 06')
os.system('Title Fortune Wheel Final Build by Gabriel James Goenawan')

#Loading Asset & Global Variable setting
winner, turn, repeat, success, wstate, timeout, consonantAvailable, firstCycle = -1, 1, 0, 0, None, 0, 1, 1
wheel = {
	1:5000,
	2:500,
	3:900,
	4:700,
	5:300,
	6:800,
	7:550,
	8:400,
	9:500,
	10:600,
	11:350,
	12:500,
	13:900,
	14:"Bankrupt",
	15:650,
	16:"Free Play",
	17:700,
	18:"Lose a Turn",
	19:800,
	20:500,
	21:450,
	22:500,
	23:300,
	24:"Bankrupt"
}
#Asset loading indicator is to detect what asset is missing, if any.
clear()
print("Loading asset... 0%")
screen = turtle.Screen()
screen.setup(800,890)
clear()
print("Loading asset... 10%")
for x in range(1,6):
	turtle.addshape('asset\\endbg'+str(x)+'.gif')
clear()
print("Loading asset... 30%")
turtle.addshape('asset\\creds.gif')
clear()
print("Loading asset... 50%")
for i in range (-1,16):
	turtle.addshape("asset\\cnt"+str(i)+".gif")
clear()
print("Loading asset... 70%")

for i in range (0,360):
	turtle.addshape("asset\\"+str(i)+".gif")
clear()
print("Loading asset... 90%")
turtle.addshape("asset\\p1.gif")
turtle.addshape("asset\\p2.gif")
turtle.addshape("asset\\p3.gif")
turtle.addshape("asset\\p4.gif")
turtle.addshape("asset\\p5.gif")
screen.bgpic('asset\\bg.gif')
clear()
print("Loading asset... 95%")
turtle.penup()
turtle.ht()
turtle.speed(10000)
turtle.back(2)
turtle.right(90)
turtle.forward(83)
turtle.st()
turtle.shape("asset\\0.gif")
clear()
print("Loading asset... 100%")
time.sleep(0.5)
clear()
os.system('mode con: cols=90 lines=35')
#global functions

def existConsonant(word_hidden, word): #function to check if a consonant exist
	for i in range (0,len(word)):
		if (not word[i].upper() in "AIUEO") and word[i] != word_hidden[i]:
			return 1
	return -1

def credit(): #credit screen renderer
	t = turtle.Turtle()
	t.penup()
	t.ht()
	t.speed(900)
	t.left(90)
	t.forward(890)
	t.shape('asset\\creds.gif')
	t.speed(4)
	t.st()
	t.backward(890)
	t.stamp()

def ending(turn, prize): #ending screen renderer
	turtle.clearscreen()
	b = turtle.Turtle()
	b.ht()
	b.penup()
	b.speed(900)
	b.left(90)
	b.forward(890)
	b.shape('asset\\endbg'+str(turn)+'.gif')
	b.speed(4)
	b.st()
	b.backward(890)
	b.stamp()
	b.ht()
	time.sleep(0.3)
	b.backward(250)
	b.color('white')
	b.write("$"+str(prize)+"!", font=('Arial', 72, 'bold'), align='center')
	time.sleep(5)


def nextPlayer(): #Player Turn Handler
	global turn,stop,current,repeat,success,letter,wheel,firstCycle
	if turn == player:
		turn = 1
		firstCycle = 0
	else:
		turn += 1
	consonantAvailable = existConsonant(word_hidden, word)
	if firstCycle != 1:
		current = "choose"
		success = 1
	else:
		stop = spin(wheel)
		current = wheel[stop]
		success = 0
	repeat = 0
	letter = ''

def To(): #timout indicator
	global timeout
	timeout = 1

def timed_input(phrase): #timed input handler
	timerturtle = turtle.Turtle()
	global timeout,terminate,phr,x
	timeout,terminate,phr,x = 0,0,'',''
	timerturtle.st()
	phr = phrase

	def inp():
		global x,phr,terminate
		x = input(phr)
		terminate = 1

	timer = threading.Timer(16.0, To)
	timer.start()
	thd = Thread(target = inp)
	thd.start()
	for i in range (15,-2,-1):
		if terminate == 0:
			timerturtle.shape("asset\\cnt"+str(i)+".gif")
			time.sleep(1)
		else:
			break
	timer.cancel()
	print("Oops, time's up. Input anything to continue")
	thd.join()
	timerturtle.ht()
	return [x,timeout]

def round(a): #rounding function.
	if a-int(a)<int(a)+1-a:
		return int(a)
	else:
		return int(a)+1

def spinDraw(stop, turn, wstate): #Function that makes the wheel spin after the randomizer outputs a value. Returns a wstate (Last wheel position, stamp id). # This function will make the wheel "charge up" before it spins & will adapt to the last wheel state.

	#i --> wheel rotation state | a --> speed

	if wstate != None:
		turtle.shape(turtle.shape("asset\\"+str(wstate[1])+".gif"))
	else:
		turtle.shape(turtle.shape("asset\\0.gif"))

	y = turtle.stamp() #To ensure the wheel doesn't flickering.
	stop -= 1
	turtle.ht()
	turtle.forward(294)
	turtle.st()
	turtle.shape("asset\\p" + str(turn) + ".gif")
	x = turtle.stamp()
	turtle.ht()
	turtle.back(294)

	if wstate != None:
		turtle.shape(turtle.shape("asset\\"+str(wstate[1])+".gif"))
	else:
		turtle.shape(turtle.shape("asset\\0.gif"))

	turtle.st()
	turtle.clearstamp(y)
	n, i, a = 0, 0, 18

	if wstate != None:
		i = wstate[1]
	else:
		i = 0

	n = 72

	while n>0: #for wheel gaining potential energy before spining
		i = i - ((1*(n)/72)+(1*(n-1)/72))/2
		z = int(i %360)
		if z == 360:
			z = 0
		turtle.shape("asset\\"+str(int(round(z)))+".gif")
		n-=1

	time.sleep(0.7)

	while i+18<360: #wheel instantly rotates at 18 degree per second until wheel state is reverted back to original (between(Bankrupt and 5000))
		i+=18
		z = int(i % 360)
		if z == 360:
			z = 0
		turtle.shape("asset\\"+str(int(round(z)))+".gif")

	#Original wheel state.
	i = 0
	n = 0

	while n <= 3: #wheel
		turtle.shape("asset\\"+str(int(i))+".gif")
		if i + a > 360 and n == 3:
			i = -18
			break
		elif i+a<360:
			i += a
		else:
			i = i - 360 + a
			n+=1

	var = random.randint(0,14) #This determine where the wheel will stop

	while i<stop*15+var:
		if i+18 > stop*15:
			turtle.shape("asset\\"+str(int((stop*15+var)))+".gif")
			break
		else:
			turtle.shape("asset\\"+str(int(i+18))+".gif")
			i+=18

	i = stop*15+var
	n = 800
	if wstate != None:
		turtle.clearstamp(wstate[0]) #clearing any leftover stamp
	while n>0: #this function decelerate the wheel
		i = i + ((18*(n)/800)+(18*(n-1)/800))/2
		a = int(round(i%360))
		if a == 360:
			a = 0
		turtle.shape("asset\\"+str(a)+".gif")
		n-=1
	return [x,round(i%360)]

def scoreboard(player): #Dynamic Scoreboard Handler. Basically renders the scoreboard and dynamically adjust its size.
	global balance
	a = [len(str(i)) for i in balance]
	mx = max(a)
	print("Current Score:".center(90))
	print("╔══════════╦═{}═╗".format("═"*(mx+2)).center(90))
	for i in range(1,player+1):
		b = "║ Player {} ║ {:<" + str(mx)+"} $ ║"
		print(b.format(i, str(balance[i-1])).center(90))
	print("╚══════════╩═{}═╝".format("═"*(mx+2)).center(90))

def GUI(turn, stop, sleepV, params = 1): #params -> 0. guess 1. normal else: no selected. Main GUI handler.
	current = wheel[stop]
	global player, word_hidden,word,wstate
	clear()
	print(word) #Cheat Mode enabled
	scoreboard(player)
	print('')
	if params == 0:
		print("Player {} is guessing the phrase".format(turn).center(90),"\n\n")
	else:
		print("Player {}'s turn".format(turn).center(90),"\n\n")
	printArray(word_hidden)
	print('\n')
	if sleepV == 1:
		wstate = spinDraw(stop,turn,wstate)
	if params == 1:
		selected(current)
	if sleepV == 1:
		time.sleep(2.5)

def selected(current): #function to display spin result
	print("Congratulations, You Got:".center(90))
	print("-----------------".center(90))
	print(str(current).center(90))
	print("-----------------".center(90))
	print("")


def minBalance(player, amount): #function to reduce player balance
	global balance
	balance[player-1] -= amount

def addBalance(player, amount): #function to indcrease player balance
	global balance
	balance[player-1] += amount

def spin(wheel): #function to spin the wheel
	return random.randint(1,24)

def check(letter): #checking function
	global word, word_hidden
	cnt = 0
	for i in range (0,len(word)):
		if letter == word_hidden[i]:
			return -1
		elif word[i] == letter.upper():
			word_hidden[i] = letter.upper()
			cnt += 1
	return cnt

def printArray(arr): #array printing handler.
	b = ""
	for i in arr:
		b += str(i)
	print(b.center(90))

#Import DB
source = open("asset\\WofFPhrases.txt","r").readlines()
word = source[random.randint(0,75)].strip()
word_hidden = []
for i in range (0, len(word)):
	if word[i] == " ":
		word_hidden.append(" ")
	else:
		word_hidden.append("□")

## Get Player Amount
while True:
	a = input("Enter The Number of Player> ")
	clear()
	if a.isdigit() and int(a) <= maxplayer and int(a) > 0:
		player = int(a)
		break
	elif a.isdigit() and int(a) >= maxplayer:
		print("Maximum number of player allowed is 3.")
		time.sleep(2.5)
		clear()
	else:
		print("Invalid number of players.")
		time.sleep(2.5)
		clear()

balance = []
for i in range(0,player):
	balance.append(0)

## Main game loop
stop = spin(wheel)
current = wheel[stop]
while True:

	#GUI delay handler
	if repeat != 0:
		sleepV = 0
	else:
		sleepV = 1

	#GUI mode selector
	if success == 1:
		GUI(turn,stop, 0, 2)
	elif success == 2:
		GUI(turn, stop, 0, 0)
	else:
		GUI(turn, stop, sleepV, 1)

	#Action selector (choose -> choose action (skipped on the first turn cycle), buy -> buy vowels, guess, Lose a turn, Free play, Bankrupt, Else -> Consonant guess)
	if current == "choose":
		temp = input("It's your turn, choose an action.\n1:Buy a vowel\n2:Spin the wheel\n3:Guess the phrase\nInput your choice> ")
		if temp == "1" and balance[turn-1]<250:
			GUI(turn,stop,0,2)
			print("You don't have enough Balance".center(90))
			time.sleep(2.5)
			continue
		elif temp == "1":
			current, success, repeat, letter = "buy", 1, 1, ''
			continue
		elif temp == "3":
			current, success = "guess", 2
			continue
		else:
			consonantAvailable = existConsonant(word_hidden, word)

			if consonantAvailable == 1:
				success, repeat = 0, 0
				stop = spin(wheel)
				current = wheel[stop]
				continue
			else:
				print("\n")
				print("No more consonant available! Take your guess or buy a vowel".center(90))
				time.sleep(2.5)
				continue

	if current == "Lose a Turn":
		print("You lost a turn!".center(90))
		letter = ''
		time.sleep(2.5)
	elif current == "Bankrupt":
		print("You went Bankrupt! You lost all your money.".center(90))
		balance[turn-1]=0
		letter = ''
		time.sleep(2.5)
	elif current == "Free Play":
		letter = input("Enter a letter to guess> ")

		if letter!= None and letter != "" and len(letter)>1:
			letter = letter[0]

		if letter == '' or letter == " " or letter == None:
			GUI(turn, stop, 0, 1)
			print("Your answer can't be empty. You lost your turn.".center(90))
			time.sleep(2.5)
			nextPlayer()
			continue

		result = check(letter.upper())
		GUI(turn, stop, 0, 3)

		if result == 0:
			print("Sorry, theres no '{}' in the phrase".format(letter.upper()).center(90))
			time.sleep(2.5)
		elif result == -1:
			print("The letter '{}' has already appeared in the puzzle".format(letter.upper()).center(90))
			time.sleep(2.5)
		else:
			print("Letter '{}' exist and its position has been revealed".format(letter.upper()).center(90))
			time.sleep(2.5)

		current, success, repeat, letter = "AFree", 1, 1, ''
		continue

	elif current == "AFree":

		GUI(turn, stop, 0, 2)
		temp = input("You still have a turn due to getting a Free Play.\n1:Buy another vowel\n2:Spin the wheel again\n3:Guess the phrase\nInput your choice> ")

		if len(temp)>1:
			temp = temp[0]

		if temp == "1" and balance[turn-1]<250:
			GUI(turn, stop, 0, 2)
			print("You don't have enough Balance".center(90))
			time.sleep(2.5)
			continue
		elif temp == "1":
			current, success, repeat, letter = "buy", 1, 1, ''
			continue
		elif temp == "3":
			current, success = "guess", 2
			continue
		else:
			consonantAvailable = existConsonant(word_hidden, word)
			if consonantAvailable == 1:
				success, repeat = 0, 0
				stop = spin(wheel)
				current = wheel[stop]
				continue
			else:
				print("\n")
				print("No more consonant available! Take your guess or buy a vowel".center(90))
				time.sleep(2.5)
				continue

	elif current == "guess":
		timeout = 0
		a = timed_input("\nYou have 15 seconds.\nGuess the phrase> ")
		GUI(turn, stop, 0, 0)

		if a[1] == 1:

			print("Your time is up. You lost your turn.".center(90))
			time.sleep(2.5)
			nextPlayer()
			continue

		else:
			if a[0].upper() == word:
				winner = turn
				break

			else:
				print("INCORRECT! You lost your turn.".center(90))
				time.sleep(2.5)

	elif current == "buy":
		GUI(turn, stop, 0, 2)
		a = timed_input("\nYou have 15 seconds.\nEnter a vowel to buy it for 250$> ")
		GUI(turn, stop, 0, 2)

		if a[1] == 1:
			print("Your time is up. You lost your turn.".center(90))
			time.sleep(2.5)
			nextPlayer()
			continue
		else:
			letter = a[0]

		if letter != None and letter != "" and len(letter)>1:
			letter = letter[0]

		if letter == '' or letter == " " or letter == None:
			print("Your answer can't be empty. You lost your turn.".center(90))
			time.sleep(2.5)
			nextPlayer()
			continue

		if letter.upper() in "AIUEO":

			if balance[turn-1]<250:
				print("You don't have enough Balance".center(90))
				time.sleep(2.5)

				if success == 1:
					repeat = 0
					(turn,stop,0,2)
					temp = input("You still have a turn due to guessing correctly.\n1:Spin the wheel again\n2:Guess the phrase\nInput your choice> ")

					if len(temp)>1:
						temp = temp[0]

					elif temp == "2":
						current, success = "guess", 2
						continue
					else:
						consonantAvailable = existConsonant(word_hidden, word)
						if consonantAvailable == 1:
							success, repeat = 0, 0
							stop = spin(wheel)
							current = wheel[stop]
							continue
						else:
							print("\n")
							print("No more consonant available! Take your guess or buy a vowel".center(90))
							time.sleep(2.5)
							continue

				else:
					nextPlayer()
					continue

			else:
				result = check(letter.upper())
				minBalance(turn, 250)

				if result == 0:
					print("Sorry, theres no '{}' in the phrase".format(letter).center(90))
					print("Your balance has been updated".center(90))
					success, letter = 0, ''
					time.sleep(2.5)
				elif result == -1:
					print("The letter '{}' has already appeared in the puzzle. You Lost your turn.".format(letter.upper()).center(90))
					letter = ''
					time.sleep(2.5)
				else:
					print("Letter '{}' exist and its position has been revealed".format(letter).center(90))
					print("Your balance has been updated".center(90))
					letter = ''
					time.sleep(2.5)
					GUI(turn, stop, 0, 2)
					temp = input("Congratulation, you got another turn for guessing correctly\n1:Buy another vowel\n2:Spin the wheel again\n3:Guess the phrase\nInput your choice> ")

					if len(temp)>1:
						temp = temp[0]

					if temp == "1":
						current, success, repeat, letter = "buy", 1, 1, ''
						continue
					elif temp == "3":
						current, success = "guess", 2
						continue
					else:
						consonantAvailable = existConsonant(word_hidden, word)
						if consonantAvailable == 1:
							success, repeat = 0, 0
							stop = spin(wheel)
							current = wheel[stop]
							continue
						else:
							print("\n")
							print("No more consonant available! Take your guess or buy a vowel".center(90))
							time.sleep(2.5)
							continue

		else:
			print("{} is not a vowel. Try again.".format(letter).center(90))
			time.sleep(2.5)
			current, success, letter= "buy", 1, ''
			continue

	else:
		timeout	= 0
		a = timed_input("\nYou have 15 seconds.\nEnter a consonant to guess> ")
		GUI(turn, stop, 0, 1)

		if a[1] == 1:
			print("Your time is up. You lost your turn.".center(90))
			time.sleep(2.5)
			nextPlayer()
			continue

		letter = a[0]

		if letter!=None and letter != "" and len(letter)>1:
			letter = letter[0]

		if letter == '' or letter == " ":
			print("Your answer can't be empty. You lost your turn.".center(90))
			time.sleep(2.5)
			nextPlayer()
			continue


		if letter.lower() in "aiueo":
			print("You can't buy a vowel after spining the wheel. You lost your turn.".center(90))
			repeat, letter = 1, ''
			time.sleep(2.5)
			nextPlayer()
			continue

		else:
			result = check(letter.upper())

			if result == 0:
				print("Sorry, theres no '{}' in the phrase".format(letter).center(90))
				success, letter = 0, ''
				time.sleep(2.5)
			elif result == -1:
				print("The letter '{}' has already appeared in the puzzle. You Lost your turn.".format(letter.upper()).center(90))
				letter = ''
				time.sleep(2.5)
			else:
				print("Letter '{}' exist and its position has been revealed.".format(letter).center(90))
				print("Your balance has been updated".center(90))
				addBalance(turn, current*result)
				letter = ''
				time.sleep(2.5)
				GUI(turn, stop, 0, 2)
				temp = input("Congratulation, you got another turn for guessing correctly\n1:Buy a vowel\n2:Spin the wheel again\n3:Guess the phrase\nInput your choice> ")

				if temp == "1":
					current, success,repeat, letter = "buy", 1, 1, ''
					continue
				elif temp == "3":
					current, success = "guess", 2
					continue
				else:
					consonantAvailable = existConsonant(word_hidden, word)
					if consonantAvailable == 1:
						success, repeat = 0, 0
						stop = spin(wheel)
						current = wheel[stop]
						continue
					else:
						print("\n")
						print("No more consonant available! Take your guess or buy a vowel".center(90))
						time.sleep(2.5)
						continue

	nextPlayer()

#ending Screen.
clear()
print("\n\n\n\n\n")
print("Congratulations Player {}! You've won {}$!".format(str(winner), str(balance[winner-1])).center(90))
ending(winner, balance[winner-1])
clear()
credit()
print("\n\n\n\n\n")
print("Thankyou for playing!".center(90))
time.sleep(5)
exit()

