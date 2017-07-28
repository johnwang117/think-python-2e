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

def snowflake(t, length):
	for i in range(3):
		koch(t, length)

bob = turtle.Turtle()
print(bob)

snowflake(bob, 500)

turtle.mainloop()