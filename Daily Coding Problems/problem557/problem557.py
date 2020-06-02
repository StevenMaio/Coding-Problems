from sys import argv

def main(n, x):
    count = 0
    for i in range(1, n+1):
        if (x%i)==0:
            k = x/i
            count += int(k <= n)
    print(count)


if __name__ == '__main__':
    if len(argv) < 3:
        print('usage: problem557.py N X')
    else:
        n,x = map(lambda x : int(x), argv[1:3])
        main(n,x)
