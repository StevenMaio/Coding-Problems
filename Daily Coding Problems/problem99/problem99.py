from sys import argv
import pdb

def larg_con(arr):
	d = {}
	# pdb.set_trace()

	for x in arr:
		d[x] = 1
		# First, see if x - 1 is in the d
		try:
			if d[x-1]:
				d[x] += d[x-1]
				d[x - d[x-1]] = d[x]

		except:
			pass

		# Now, see if x+1 is in d
		try:
			if d[x+1]:
				# I need to update the left side
				l = x + 1 - d[x]
				d[x] += d[x+1]
				d[l] = d[x]
				d[x + d[x+1]] = d[x]

		except:
			pass

	return max(d.values())

def main():
	if len(argv) < 2:
		print('Error : not enough arguments')
		return

	arr = []

	for x in argv[1:]:
		arr.append(int(x))

	sol = larg_con(arr)
	print(sol)

if __name__ == '__main__':
	main()