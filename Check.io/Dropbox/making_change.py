import pdb

class SolutionVector():
    def __init__(self):
        self.total = 0
        self.last_denom = None
        self.length = 0

count = 0

def checkio(total, denoms):
    def gen_candidates(seq):
        x = seq.last_denom

        if x == None:
            return [x for x in denoms]
        else:
            return list(filter(lambda t: t >= x, denoms))

    seq = SolutionVector()
    q = [seq]
    
    pdb.set_trace()

    while len(q) != 0:
        global count
        count += 1

        seq = q.pop(0)

        s = seq.total

        # Return the length of the sequence if it totals
        if s == total:
            return seq.length

        # Reiterate if we're over total
        elif s >  total:
            continue

        candidates = gen_candidates(seq)

        for c in candidates:
            cp_seq = SolutionVector()
            cp_seq.last_denom = c
            cp_seq.total = seq.total + c
            cp_seq.length = seq.length + 1

            q.append(cp_seq)

    return None

def main():
    total =  8
    denoms = [1, 3, 5, 10, 9]
    sol = checkio(total, denoms)

    print('Minimum number of coins: {}'.format(sol))
    print('Total iterations: {}'.format(count))

if __name__ == '__main__':
    main()
