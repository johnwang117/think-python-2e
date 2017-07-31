def do_twice(f, value):
	f(value)
	f(value)

def print_spam(spam):
	print(spam)

do_twice(print_spam, 'maps')