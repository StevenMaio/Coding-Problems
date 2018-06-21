from sys import argv
import pdb

# denominations
denoms = [
    1, 2, 5, 10, 20,
    50, 100, 200,
]

# denominations index
d_ind = {
    1: 0,
    2: 1,
    5: 2,
    10: 3,
    20: 4,
    50: 5,
    100: 6,
    200: 7,
}

# Global count variable
total = 0

def get_candidates(a, k, n):
    candidates = []
    if k == 0:
        for d in denoms:
            candidates.append(d)
            
        return candidates

    index = 0
    length = len(a)

    # Find the first nonzero element in the array
    for i in range(length)[::-1]:
        if a[i] != 0:
            index = i
            break

    # Find the denominations which do not go over
    for i in range(index, length):
        d = denoms[i]

        if n - k - d >= 0:
            candidates.append(d)
    
    return candidates

def backtrack(a, k, n):
    # First, get the candidates
    cand = get_candidates(a, k, n)
    length = len(cand)
    # pdb.set_trace()

    # Perform the backtracking step
    for i in range(length):
        d = cand[i]
        ind = d_ind[d]

        # perform the current step
        k += d
        a[ind] += 1

        # determine if there is a solution
        if k == n:
            global total
            total += 1

        # Recursively call backtrack
        elif k < n:
            backtrack(a, k, n)

        # Undo the last step
        k -= d
        a[ind] -= 1


def get_nsums(n):
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    k = 0
    pdb.set_trace()

    backtrack(a, k, n)

def main():
    if len(argv) != 2:
        print('Error : invalid number of arguments')
        return

    try:
        n = int(argv[1])

        if (n <= 0):
            print('Error : n must be positive')
            return

        get_nsums(n)
        print(total)

    except:
        print('Error : invalid argument')

if __name__ == '__main__':
    main()