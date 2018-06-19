from sys import argv

def is_tidy(n):
    n = str(n)

    for i in range(1, len(n)):
        a = n[i-1]
        b = n[i]

        if a > b:
            return False

    return True

def tidy_number(n):
    # Our base is case is when n is 0
    if n == 0:
        return ''

    f_dig = n % 10  # remainder

    # Check to see if n is close to be a tidy number, as in only the ones digit is off
    while (f_dig > 0):
        if is_tidy(n):
            return str(n)
        
        f_dig -= 1
        n -= 1

    n -= 2
    n = int(n/10)

    return tidy_number(n) + '9'


def main():
    if len(argv) != 2:
        print('Error : program requires exactly 2 arguments')
        return

    try:
        n = int( argv[1] )

        if n <= 0:
            print('Error : n must be positive')

        sol = tidy_number(n)
        print(sol)

    except:
        print('Error : invalid input')

if __name__ == '__main__':
    main()