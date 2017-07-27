def check_fermat(a, b, c, n):
	if a ** n + b ** n == c ** n:
		print('Holy smokes, Fermat was wrong!')
	else:
		print('No, that doesn\'t work.')

print('Please input 4 numbers to check if Fermat\'s Last Theorem is right or wrong.')
a = int(input('First is a: '))
b = int(input('Second is b: '))
c = int(input('Third is c: '))
n = int(input('The last is n: '))

check_fermat(a, b, c, n)