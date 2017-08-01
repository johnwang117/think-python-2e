def has_no_e(word):
	if 'e' in word:
		return False
	else:
		return True

count = 0
total = 111809
fin = open('words.txt')
for line in fin:
	word = line.strip()
	if has_no_e(word):
		#print(word)
		count = count + 1
proportion = count / total * 100
print('There\'re %.2f%% words has no letter e' % proportion)
