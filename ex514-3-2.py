def is_triangle(a, b, c):
	a = int(a)
	b = int(b)
	c = int(c)

	if a + b > c:
		print('Yes, this 3 lines you input A=%d B=%d C=%d could make a triangle.' % (a, b, c))
	else:
		print('No, this 3 lines you input A=%d B=%d C=%d couldn\'t make a triangle.' % (a, b, c))

print('Please input 3 numbers: ')
a = input('A is: ')
b = input('B is: ')
c = input('C is: ')

is_triangle(a, b, c)