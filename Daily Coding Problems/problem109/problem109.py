from sys import argv
import pdb

def swap_odd_even(x):
    return ((x & 0xAA) >> 1) | ((x&0x55) << 1)

def main():
    if len(argv) != 2:
        print('Error : program requires an 8-bit integer arguments')
        return

    try:
        x = int(argv[1])

        if x < 0 or x > 0xFF:
            print('Error : input must be an 8-bit integer')
            return

        sol = swap_odd_even(x)

        print(sol)

    except:
        print('Error : invalid input')

if __name__ == '__main__':
    main()