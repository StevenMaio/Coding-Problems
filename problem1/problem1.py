def sum_exists(int_arr, k):
	"""
	Returns true if @k can represented as a sum of elements of int_arr
	"""
	int_dict= dict()	# initialize empty dictionary

	# iterate through the integers in the array
	for x in int_arr:

		# if k - x is in the dictionary, then we're done
		if k - x in int_dict:
			return True

		# otherwise, add x to the dictionary
		else:
			int_dict[x] = 1

	return False

def main():
	# Ask user for the number of items in the list and then fill the list
	count = int(input('How many items: '))
	numbers = []

	# Add count integers to numbers
	while count > 0:
		numbers.append(int(input('Enter a number: ')))	

	desired_sum = int(input('Enter the desired sum: '))

	output = '\n{}'.format(sum_exists(numbers, desired_sum))
	print(output)

if __name__ == '__main__':
	main()
