def find(word, letter, begin):
	index = 0
	while index < len(word):
		if word[int(begin) + index] == letter:
			return index
		index = index + 1
	return -1

word = input('Please input a word: ')
letter = input('Please input a letter: ')
begin= input('Please input a begin position: ')

print('The relative position of the letter in the word is %d' % find(word, letter, begin))
