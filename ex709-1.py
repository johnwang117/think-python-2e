import math

print('a', 'mysqrt(a)', 'math.sqrt(a)', 'diff',)
print('-', '-' * 9, '-' * 12, '-' * 4)


def mysqrt(a):
	x = a / 2
	while True:
		y = (x + a/x) / 2
		if abs(y - x) < 0.0000001:
			break
		x = y
	return y

def test_squre_root(a):
	print(a, mysqrt(a), math.sqrt(a), abs(mysqrt(a)-math.sqrt(a)))

for i in range(1, 10):
	test_squre_root(i)