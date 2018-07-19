from sys import argv
from matrix import create_int_matrix

def find_opt_coins(m):
    # Find the number of rows and columns
    n_rows = len(m)
    n_cols = len(m[0])


    # Add all of columns in the last row because there is only one path
    for i in range(n_cols-1)[::-1]:
        m[n_rows-1][i] += m[n_rows-1][i+1]

    # Do the same for the last column
    for i in range(n_rows-1)[::-1]:
        m[i][n_cols-1] += m[i+1][n_cols-1]

    for i in range(n_rows-1)[::-1]:
        for j in range(n_cols-1)[::-1]:
            entry = m[i][j]
            right_entry = m[i][j+1]
            bottom_entry = m[i+1][j]

            m[i][j] = entry + max(right_entry, bottom_entry)

    return m[0][0]

def main():
    if len(argv) != 2:
        print('Error : not enough arguments')
        return

    try:
        filename = argv[1]
        m = create_int_matrix(filename)

        sol = find_opt_coins(m)
        print(sol)

    except:
        print('Error : invalid input')
        return

if __name__ == '__main__':
    main()