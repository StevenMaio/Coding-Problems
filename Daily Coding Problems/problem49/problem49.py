from sys import argv
from pdb import set_trace

def max_cont_sim(int_l):
	# First, find the sum
	length = len(int_l)
	list_sum = sum(int_l)

	# Now, find the best starting position
	l_sum = list_sum # l for left
	max_l = l_sum
	start_pos = 0

	for i in range(length):
		l_sum -= int_l[i]

		if l_sum > max_l:
			max_l = l_sum
			start_pos = i + 1
	
	# Find the best stop
	r_sum = list_sum	# r for right
	max_r = r_sum
	end_pos = length

	for j in range(length)[::-1]:
		r_sum -= int_l[j]

		if r_sum > max_r:
			max_r = r_sum 
			end_pos = j

	final_sum = sum(int_l[start_pos : end_pos])
	if (final_sum < 0):
		final_sum = 0

	return final_sum

def main():
	int_l = []

	for arg in argv[1:]:
		int_l.append(int(arg))

	solution = max_cont_sim(int_l)
	print(solution)

if __name__ == '__main__':
	main()
