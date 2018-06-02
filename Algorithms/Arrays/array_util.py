from sys import argv

def parse_file(filename):
	# Open the file, read its contents and then close it
	fle = open(filename, "r")
	text = fle.read()
	fle.close()

	arr = []

	text = text.split(',')
	for x in text:
		arr.append(int(x))

	return arr


# Defunct main function
def main():
	filename = argv[1]

	arr = parse_file(filename)

	print(arr)

if __name__ == '__main__':
	main()
