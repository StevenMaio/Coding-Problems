from sys import argv

def is_palindrome_helper(c1, c2):
	if c1 == c2:
		return True

	elif c1.data != c2.data:
		return False

	elif c1.next == c2:
		return True

	else:
		return is_palindrome_helper(c1.next, c2.prev)

def is_palindrome(l):
	head = l
	tail = l

	# Advance tail to the end of the linked list
	while (tail.next):
		tail = tail.next

	return is_palindrome_helper(head, tail)

def main():
	pass

if __name__ == '__main__':
	main()