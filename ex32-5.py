def do_twice(f, value):
	f(value)
	f(value)

def do_four(f, bruce):
	do_twice(f, bruce)
	do_twice(f, bruce)

def print_twice(maps):
	print(maps)
	print(maps)

do_four(print_twice, 'spam')