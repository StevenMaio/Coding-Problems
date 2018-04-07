from sys import argv

def way_up_n_steps(n, x):
    unique_paths = {0: 0}

    for i in range(n + 1):
        way_up_n_steps_helper(i, x, unique_paths)

    return unique_paths[n]

def way_up_n_steps_helper(k, x, paths_dict):
    if (k < 0):
        return 0
    elif k in paths_dict.keys():
        return paths_dict[k]
    else:
        paths = 0

        if k in x:
            paths += 1

        for i in x:
            paths += way_up_n_steps_helper(k - i, x, paths_dict)

        paths_dict[k] = paths

        return paths

def main():
	# Exit the program if there aren't enough arguments
	if (len(argv) < 2):
		print('Program must be called in the form problem12.py n x_1 x_2,... x_n')
		return 

	n = int(argv[1])
	x = []

	for i in argv[2:]:
		x.append(int(i))

	val = way_up_n_steps(n, x)

	print("{0} different ways.".format(val))

if __name__ == '__main__':
    main()
