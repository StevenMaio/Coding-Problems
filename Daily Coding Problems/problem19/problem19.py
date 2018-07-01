from sys import argv
from matrix.util import create_int_matrix

def opt_homes(price_mat, n):
    # The opt dict for the houses 
    opt = {}

    # First, we need to find the top 3 colors for each house
    # FIXME: This needs to account for duplicate values
    for i in range(n):
        # I'm doing this because I'm too lazy to sort by hand
        mat_row = price_mat[i]
        prices = [x for x in mat_row]
        prices.sort()

        opt_colors = []

        for price in prices[:3]:
            index = mat_row.index(price)
            opt_colors.append(index)

        opt[i] = opt_colors
        
    print(opt)

    # Initialize the memo arr
    memo = []
    for i in range(n):
        row = [0, 0, 0]
        memo.append(row)

    # Set the values for the row corresponding to h_0
    memo[0][0] = price_mat[0][opt[0][0]]
    memo[0][1] = price_mat[0][opt[0][1]]
    memo[0][2] = price_mat[0][opt[0][2]]

    for i in range(1, n):

        for j in range(3):
            clr = opt[i][j]

            # Get the candidate colors for opt_c
            cand_ind = [opt[i-1].index(x) for x in opt[i-1] if x != clr]
            vals = [memo[i-1][k] for k in cand_ind]
            
            entry = min(vals) + price_mat[i][clr]
            memo[i][j] = entry

    possible_solutions = [memo[n-1][i] for i in range(3)]
    return min(possible_solutions)

def main():
    if len(argv) != 2:
        print('Error : program requires 2 arguments')

    try:
        filename = argv[1]
        m = create_int_matrix(filename)
        n = len(m)

        sol = opt_homes(m, n)
        print(sol)

    except:
        print('Error : an error occurred')

if __name__ == '__main__':
    main()