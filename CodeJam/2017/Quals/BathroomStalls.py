from sys import argv

class Stall():
    def __init__(self, occupied, index):
        self.left = 0
        self.right = 0
        self.occupied = occupied
        self.index = index

    def max(self):
        return max(self.left, self.right)

    def min(self):
        return min(self.left, self.right)

    def __str__(self):
        return 'O: {}, L: {}, R: {}, i: {}'.format(self.occupied, self.left, 
            self.right, self.index)

def bathroom_stalls(n, k):
    # Initialize the stalls array
    stalls_arr = []
    for i in range(n):
        stall = Stall(False, i)
        stall.left = i
        stall.right = n - i
        stalls_arr.append(stall)
        
    # Iterate each time for each person added
    unoccupied_stalls = [x for x in stalls_arr]
    s = None

    for i in range(k):
        # First, find the optimal stalls

        min_dis = max([x.min() for x in unoccupied_stalls if not x.occupied])

        # If there is only one such stall choose, it. Otherwise, choose 
        # the one for which s.max is maximal
        candidate_stalls =\
            [x for x in unoccupied_stalls if x.min() == min_dis]

        max_dis = max([x.max() for x in candidate_stalls])

        if len(candidate_stalls) == 1:
            s = candidate_stalls[0]
            s.occupied = True
        else:
            candidate_stalls = [x for x in candidate_stalls if x.max() == max_dis]
            s = candidate_stalls[0]
            s.occupied = True

        # Now, update every stall
        index = s.index

        # Update every stall to the left of s
        for i in range(index):
            t = stalls_arr[i]

            # End the loop if t is occupied
            if t.occupied:
                break

            t.right = min(t.right, index - t.index)

        # Update every stall to the right of s
        for i in range(index + 1, n):
            t = stalls_arr[i]

            # End the loop if t is occupied
            if t.occupied:
                break
            t.left = min(t.left, t.index - index)

        unoccupied_stalls.remove(s)

    return (s.max()- 1, s.min() - 1)

def main():
    if len(argv) != 3:
        print('Error: program requires 3 arguments')
        return

    # try:
    n = int(argv[1])
    k = int(argv[2])

    if n < 0 or k < 0:
        print('Error : both n,k must be positive')
        return

    if (k > n):
        print('Error : k must be less than n')
        return

    sol = bathroom_stalls(n, k)
    print(sol)

    # except:
    #     print('Error : invalid input')

if __name__ == '__main__':
    main()