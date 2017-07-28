# need to change later, i can't think out know, give me some time.

def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def is_palindrome(word):
	if first(word) != last(word):
		return False
	elif first(word) == last(word) and len(word) % 2 == 3:
		return True
	elif first(word) == last(word) and len(word) % 2 == 2:
		return True
	else:
		return is_palindrome(middle(word))

print(is_palindrome('redivider'))