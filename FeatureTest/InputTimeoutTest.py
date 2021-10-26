from threading import Thread
import threading
import time
import turtle
timeout = 0
for i in range (0,16):
	turtle.addshape("..\\asset\\cnt"+str(i)+".gif")

def To(): #timout indicator
	global timeout,terminate
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

	timer = threading.Timer(17.0, To)
	timer.start()
	thd = Thread(target = inp)
	thd.start()
	for i in range (15,-1,-1):
		if terminate == 0:
			timerturtle.shape("..\\asset\\cnt"+str(i)+".gif")
			time.sleep(1)
		else:	
			break
	timer.cancel()
	print("Oops, time's up. Input anything to continue")	
	thd.join()
	timerturtle.ht()
	return [x,timeout]

x = timed_input("please input your number> ")
if x[1] == 1:
	print("Time's up. You lost a turn")
else:
	print(x[0])


