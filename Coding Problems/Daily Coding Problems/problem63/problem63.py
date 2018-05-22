from sys import argv

def find_word_helper(matrix, word, row_ind, col_ind, w_ind):
	# Check to see if we've reached the boundaries for any parameter
	if w_ind == len(word):
		return True

	elif row_ind == len(matrix) or col_ind == len(matrix[0]):
		return False

	# If the words match, search for a matching word
	if matrix[row_ind][col_ind] == word[w_ind]:
		return find_word_helper(matrix, word, row_ind + 1, col_ind, w_ind + 1)\
			or find_word_helper(matrix, word, row_ind, col_ind + 1, w_ind + 1)\
			or find_word_helper(matrix, word, row_ind + 1, col_ind, 0)\
			or find_word_helper(matrix, word, row_ind + 1, col_ind, 0)\

	return find_word_helper(matrix, word, row_ind + 1, col_ind, 0)\
		or find_word_helper(matrix, word, row_ind, col_ind + 1, 0)

def find_word(matrix, word):
	return find_word_helper(matrix, word, 0, 0, 0)

def main():
	word = argv[1]
	matrix = []

	for arg in argv[2:]:
		row = []
		for x in arg:
			row.append(x)

		matrix.append(row)

	solution = find_word(matrix, word)
	print('{}'.format(solution))

if __name__ == '__main__':
	main()
