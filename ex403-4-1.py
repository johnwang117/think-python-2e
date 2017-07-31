import turtle
import math

def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360 / n)

def circle(t, r):
	circumference = 2 * math.pi * r
	n = int(circumference / 3) + 1
	length = circumference / n
	polygon(t, length, n)

bob = turtle.Turtle()
print(bob)

circle(bob, 100)

turtle.mainloop()