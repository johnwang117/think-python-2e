import turtle

def polygon(t, length, n):
	for i in range(n):
		t.fd(length)
		t.lt(360 / n)

bob = turtle.Turtle()
print(bob)

polygon(bob, length = 70, n = 7)

turtle.mainloop()