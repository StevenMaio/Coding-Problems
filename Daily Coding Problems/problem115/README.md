# Problem 115

Given two non-empty binary trees s and t, check whether tree t has exactly
the same structure and node values with a subtree of s. A subtree of s is
a tree consists of a node in s and all of this node's descendants. The trees
could also be considered as a subtree of itself.

## Solution

To use this solution enter `python problem115.py s_file t_file` wherein
`s_file` is the name of the file containing `s` and `t_file` is the name
of the name containing `t`.

**Sample tests**  
`python problem115.py input1.txt input2.txt` => `False`  
`python problem115.py input1.txt input3.txt` => `True`  
`python problem115.py input1.txt input4.txt` => `True`

I also realized that there isn't any insight as to how `==` works for two
binary trees, so I decided to include here the implementation for `==`

```python
def __eq__(self, other):
    # If the two values are unequal
    if self.data != other.data:
        return False

    # If the two do not share the same adjacency structure
    elif not self.left and other.left:
        return False

    elif self.left and not other.left:
        return False

    elif self.right and not other.right:
        return False

    elif not self.right and other.right:
        return False

    elif not self.right and not self.left:
        return True

    #  Determine if the left and right subtrees are equal
    ret = False

    if self.left:
        ret |= self.left == other.left

    if self.right:
        ret |= self.right == self.right
```