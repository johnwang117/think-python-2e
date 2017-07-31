# 使用递归

def print_n(s, n):
	if n <= 0:
		return
	print(s)
	print_n(s, n - 1)

print_n('sublime', 3)



#使用迭代

def print_n(s, n):
	while n > 0:
		print(s)
		n = n - 1

print_n('sublime', 3)