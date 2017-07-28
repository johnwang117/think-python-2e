def compare(x, y):
	if x > y:
		return 1
	elif x == y:
		return 0
	else:
		return -1

a = input('Please input number x: ')
b = input('Please input number y: ')

answer = compare(a, b)
print(answer)