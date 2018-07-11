from sys import argv
from graph import deserialize

def find_eq_sub(s_root, t_root):
    if s_root == t_root:
        return True

    ret = False

    if s_root.left:
        ret |= s_root.left == t_root

    if s_root.right:
        ret |= s_root.right == t_root

    return ret

def main():
    if len(argv) != 3:
        print('Error : program requires two filename arguments')
        return

    try:
        s_file = argv[1]
        t_file = argv[2]

        s_root = deserialize(s_file)
        t_root = deserialize(t_file)

        sol = find_eq_sub(s_root, t_root)
        print(sol)

    except:
        print('Error : error occurred creating trees')

if __name__ == '__main__':
    main()