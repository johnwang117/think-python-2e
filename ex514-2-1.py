def check_fermat(a, b, c, n):
	if a ** n + b ** n == c ** n:
		print('Holy smokes, Fermat was wrong!')
	else:
		print('No, that doesn\'t work.')

check_fermat(2, 2, 1, 2)
