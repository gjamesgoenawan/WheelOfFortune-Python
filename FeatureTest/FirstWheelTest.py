import turtle
import os
screen = turtle.Screen()

for i in range (0,360):
	screen.addshape("..\\asset\\"+str(i)+".gif")

for i in range(0,360):
	turtle.Turtle().shape("..\\asset\\"+str(i)+".gif")
