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
    n = int(input("How many steps do you wish to climb: "))
    i = int(input("How many different ways can you climb the stairs: "))

    x = []

    for j in range(i):
        k = int(input("Enter how many steps can be made in one stride: "))
        x.append(k)

    val = way_up_n_steps(n, x)

    print("{0} different ways.".format(val))

if __name__ == '__main__':
    main()