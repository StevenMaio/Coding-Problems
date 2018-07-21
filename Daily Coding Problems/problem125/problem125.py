from sys import argv
from graph import deserialize

def find_pair(root, sum):
    q = [root]

    d = {}

    while len(q) != 0:
        x = q.pop(0)
        data = x.data

        if d.get(sum - data):
            return '{}, {}'.format(data, sum - data)

        if x.left:
            q.append(x.left)

        if x.right:
            q.append(x.right)

        d[data] = True

    return 'No pair found'

def main():
    if len(argv) != 3:
        print('Error : not enough arguments')
        return

    try:
        filename = argv[1]
        k = int(argv[2])

        root = deserialize(filename)

        sol = find_pair(root, k)
        print(sol)

    except:
        print('Error : invalid arguments')

if __name__ == '__main__':
    main()