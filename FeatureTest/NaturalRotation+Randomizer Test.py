import turtle
from turtle import Screen, Shape
import os
import time
from tkinter import PhotoImage
import random
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

def round(a):
	if a-int(a)<int(a)+1-a:
		return int(a)
	else:
		return int(a)+1

screen = turtle.Screen()
screen.setup(800,890)
for i in range (0,360):
	turtle.addshape("..\\asset\\"+str(i)+".gif")
turtle.addshape("..\\asset\\"+"p1.gif")
turtle.addshape("..\\asset\\"+"p2.gif")
turtle.addshape("..\\asset\\"+"p3.gif")
screen.bgpic("..\\asset\\"+'bg.gif')
turtle.penup()
turtle.ht()
turtle.speed(10000)
turtle.back(2)
turtle.right(90)
turtle.forward(83)
turtle.st()

def spinDraw(stop, turn, stamp_id):
	stop -= 1
	print(wheel[stop+1])
	turtle.forward(294)
	turtle.st()
	turtle.shape("..\\asset\\"+"p" + str(turn) + ".gif")
	x = turtle.stamp()
	turtle.ht()
	turtle.back(294)
	turtle.st()
	n, i, a = 0, 0, 18
	if stamp_id != None:
		turtle.clearstamp(stamp_id)
	while n <= 1:
		turtle.shape("..\\asset\\"+str(i)+".gif")
		if i + a > 360 and n == 1:
			i = -18
			break
		elif i+a<360:
			i += a
		else:
			i = i - 360 + a
			n+=1	
	var = random.randint(0,13)
	while i<stop*15+var:
		if i+18 > stop*15+var:
			turtle.shape("..\\asset\\"+str((stop*15+var))+".gif")
			break
		else:
			turtle.shape("..\\asset\\"+str(i+18)+".gif")
			i+=18
	i = stop*15+var
	n = 800
	while n>0:
		i = i + ((18*(n)/800)+(18*(n-1)/800))/2
		if round(i%360)==360:
			i = 0
		turtle.shape("..\\asset\\"+str(round(i%360))+".gif")
		n-=1
	return [x,round(i%360)]

def resetWheel(x, i):
	turtle.clearstamp(x)
	if i!= 0:
		while i<360-1:
			i+=1
			turtle.shape("..\\asset\\"+str(i)+".gif")
		x = turtle.stamp()
		turtle.ht()
		return x


x = None
while True:
	x = spinDraw(random.randint(1,24),random.randint(1,3),x)
	time.sleep(2)
	x = resetWheel(x[0],x[1])
	time.sleep(2)


