def print_plus_minus():
	print('+', '- ' * 4, '+', '- ' * 4, '+')

def print_slash():
	print('|', ' ' * 8, '|', ' ' * 8, '|')
	print()

def do_four(func):
	func()
	func()
	func()
	func()

print_plus_minus()
do_four(print_slash)
print_plus_minus()
do_four(print_slash)
print_plus_minus()
