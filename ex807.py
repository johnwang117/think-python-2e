
def count(word, letters):
	count = 0
	for letter in word:
		if letters == letter:
			count = count + 1
	print(count)

count('banana', 'a')