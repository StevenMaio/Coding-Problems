from sys import argv

def create_matrix(filename):
	matrix_file = open(filename, "r")
	matrix = []

	content = matrix_file.read()
	content = content.split('\n')

	# Close the file
	matrix_file.close()
	return content

def get_cand(matrix, v, m, n):
    cand = []

    x = v[0]
    y = v[1]

    if 0 <= x+1 < m and 0 <= y < n and not matrix[x+1][y]:
        cand.append((x+1, y))

    if 0 <= x-1 < m and 0 <= y < n and not matrix[x-1][y]:
        cand.append((x-1, y))

    if 0 <= x < m and 0 <= y+1 < n and not matrix[x][y+1]:
        cand.append((x, y+1))

    if 0 <= x < m and 0 <= y-1 < n and not matrix[x][y-1]:
        cand.append((x, y-1))

    return cand

def solve(matrix, start, end):
    m = len(matrix)
    n = len(matrix[0])
    q = [start]
    aux_q = []
    keep_going = True

    layer = 0

    while keep_going:
        if len(q) == 0:
            return None
        
        # Pop the first element of the q
        v = q.pop(0)

        # Then we're done
        if v == end:
            return layer

        cand = get_cand(matrix, v, m, n)
        matrix[v[0]][v[1]] = True

        for x in cand:
            aux_q.append(x)

        if len(q) == 0:
            q = aux_q
            layer += 1
            aux_q = []


def main():
    if len(argv) != 4:
        print('Error : program requires only a filename argument')
        return
    
    filename = argv[1]

    # Get the start point
    temp = argv[2].split(',')
    start = (int(temp[0]), int(temp[1]))

    # Get the start point
    temp = argv[3].split(',')
    end = (int(temp[0]), int(temp[1]))

    # Create the matrix because python is annoying with white space
    temp = create_matrix(filename)
    m = []

    for x in temp:
        row = []
        x = x.split(' ')

        for y in x:
            if y == '0':
                row.append(False)
            else:
                row.append(True)

        m.append(row)

    sol = solve(m, start, end)
    print(sol)

if __name__ == '__main__':
    main()