from sys import argv
from graph import deserialize, mark_parent
import pdb

def find_node(root, data):
    if root.data == data:
        return root

    if root.left:
        target = find_node(root.left, data)

        if target:
            return target

    if root.right:
        target = find_node(root.right, data)

        if target:
            return target

    return None
        

# Find the lowest common ancestor of x and y
def find_lca(root, x, y):
    if x is root or y is root:
        return root

    # Initialize an empty dict for the parents of x
    parents = {}
    cursor = x

    # Hash each parent of x (the value doesn't matter)
    while cursor.parent:
        parents[cursor] = True  # This isn' very important
        cursor = cursor.parent

    cursor = y

    # Set the cursor to y, and find the first ancestor of y that is hashed
    # inside the parents dictionary
    while cursor.parent:
        try:
            if parents[cursor]:
                return cursor

        except:
            cursor = cursor.parent

    return root

def main():
    if len(argv) != 4:
        print('Error : program requires filename argument and two data arguments')
        return

    try:
        # Deserialize the tree
        filename = argv[1]
        data1 = int(argv[2])
        data2 = int(argv[3])
        root = deserialize(filename)
        root.parent = None      # this is so that root will have an attribute parent

        mark_parent(root)
        x = find_node(root, data1)
        y = find_node(root, data2)

        lca = find_lca(root, x, y)
        print('{}'.format(lca.data))

    except:
        print('Error : invalid arguments given')

if __name__ == '__main__':
    main()