import turtle

def koch(t, length):
	if length < 3:
		t.fd(length)
	else:
		koch(t, length / 3)
		t.lt(60)
		koch(t, length / 3)
		t.rt(60)
		koch(t, length / 3)
		t.lt(60)
		koch(t, length / 3)

bob = turtle.Turtle()
print(bob)

koch(bob, 500)

turtle.mainloop()