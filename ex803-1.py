def print_letter(word):
	index = len(word) - 1
	while index >= 0:
		letter = word[index]
		print(letter)
		index = index - 1

print_letter(input('Please input a word: '))