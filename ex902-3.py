# need more to be done

def avoid(letter):
	if letter in word:
		return False
	else:
		return True

letter = input('Please input a letter: ')

count = 0
total = 111809

fin = open('words.txt')
for line in fin:
	word = line.strip()
	if avoid(letter):
		#print(word)
		count = count + 1
proportion = count / total * 100

print('There\'re %.2f%% words has no given letter.' % proportion)
