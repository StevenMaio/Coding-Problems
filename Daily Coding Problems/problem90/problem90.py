from sys import argv
from random import randint

def thing(l, n):
    # Create a list of all of the elements from 0 to n which are not in l
    temp = [x for x in range(n) if x not in l]

    # Randomly choose some element in the filtered list and return it
    randIndex = randint(0, len(temp) - 1)
    return temp[randIndex]

def main():
    n = int( argv[1] )
    l = []

    for x in argv[2:]:
        l.append( int(x) )

    sol = thing(l, n)
    print(sol)

if __name__ == '__main__':
    main()