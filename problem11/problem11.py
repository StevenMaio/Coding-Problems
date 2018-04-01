from sys import argv
from test1 import query, strings
#import pdb

def autocomplete(query, strings):
	autocomplete_set = []

	# This will be a brute force method first
	n = len(query)

	for s in strings:
		if s[:n] == query:
			autocomplete_set.append(s)

	return autocomplete_set

def main():
	# Get the values form the file in argv
	result = autocomplete(query, strings)

	for x in result:
		print(x)

if __name__ == '__main__':
	main()
