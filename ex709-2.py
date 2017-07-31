# a little more thing to be done.
def eval_loop():
	while True:
		s = input('Please input: ')
		if s != 'done':
			print(eval(s))
		else:
			break

eval_loop()