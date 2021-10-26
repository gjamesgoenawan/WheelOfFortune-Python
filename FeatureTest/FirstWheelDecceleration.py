import turtle

turtle.Screen()
for i in range (0,360):
	turtle.addshape("..\\asset\\"+str(i)+".gif")

def round(a):
	if a-int(a)<int(a)+1-a:
		return int(a)
	else:
		return int(a)+1

i = 14
n = 800
while n>0: #this function deccelerate the wheel
	i = i + ((18*(n)/800)+(18*(n-1)/800))/2	
	turtle.shape("..\\asset\\"+str(round(i)%360)+".gif")
	n-=1
print(round(i)%360)
