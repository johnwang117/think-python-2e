# more to be done

def count(word, letter):
	count = 0
	index = 0
	for letter in word:
		if letter == word[index]:
			count = count + 1
		index = index + 1
	print(count)

count('banana', 'a')