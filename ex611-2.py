def ark(m, n):
	if m == 0:
		return n + 1
	elif m > 0 and n == 0:
		return ark(m - 1, 1)
	elif m > 0 and n > 0:
		return ark(m - 1, ark(m, n - 1))
	else:
		return 'Wrong number'

print(ark(3, 4))