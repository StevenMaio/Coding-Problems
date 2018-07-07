from sys import argv

def find_start_indices(s, w):
	s_len= len(s)
	w_len = len(w)

	if s_len < w_len:
		return []

	start = 0
	end = w_len
	indices = []

	w_d = {c: w.count(c) for c in w}

	for i in range(end, s_len + 1):
		end = i
		start = end - w_len

		temp = s[start:end]

		d = {c: temp.count(c) for c in temp}

		if d == w_d:
			indices.append(start)

	return indices

def main():
	if len(argv) != 3:
		print('Error : incorrect number of arguments')
		return

	s = argv[1]
	w = argv[2]

	l = find_start_indices(s, w)
	print(l)

if __name__ == '__main__':
	main()