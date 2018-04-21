from sys import argv
import pdb

def sort_med(seq):
	for i in range(len(seq)):
		j = i

#		pdb.set_trace()

		while (j > 0):
			if seq[j] < seq[j-1]:
				temp = seq[j]
				seq[j] = seq[j-1]
				seq[j-1] = temp
			j -= 1

		if i%2 == 0:
			print(float(seq[int(i/2)]))

		else:
			avg = (float(seq[int(i/2)]) + seq[(int(i/2) + 1)])/2
			print(avg)

def main():
	seq = []

	for arg in argv[1:]:
		seq.append(int(arg))

	sort_med(seq)

if __name__ == '__main__':
	main()
