def is_triangle(a, b, c):
	a = int(a)
	b = int(b)
	c = int(c)

	if a + b > c:
		print('Yes, this 3 lines could make a triangle.')
	else:
		print('No, this 3 lines couldn\'t make a triangle.')

is_triangle(3, 3, 9)