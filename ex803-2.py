prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	if letter == 'O':
		print(letter + 'uack')
	if letter == 'Q':
		print(letter + 'uack')
	else:
		print(letter + suffix)