from sys import argv
'''
	Input format, the first argument needs to be the string (with no spaces)
		and the following arguments will be the words in the dictionary
'''

# This will be the implementation for the simple version of this problem
def unscramble(string, dictionary):
	message = []
	i = 0
	j = 0

	while j < len(string):
		substr = string[i:j + 1]

		for word in dictionary:
			if word == substr:
				message.append(word)
				i = j + 1

				continue

		j += 1


	return message

def main():
	# Check to see if there are enough arguments
	if (len(argv) < 3):
		print("Not enough arguments")
		return

	# Initiliaze the string and the dictionary
	dict_str = argv[1]
	dictionary = []

	for arg in argv[2:]:
		dictionary.append(arg)

	# Unscramble the message and create a nice output
	message = unscramble(dict_str, dictionary)
	output = ''

	for word in message:
		output += word + ' '

	print(output)

if __name__ == '__main__':
	main()
