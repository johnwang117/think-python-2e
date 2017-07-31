# I may need a pen to figure this out.

def is_power(a, b):
	if a % b != 0:
		return False
	elif a == b:
		return False
	elif b == 1:
		return False
	else:
		return is_power(a/b, b)

print(is_power(9, 3))