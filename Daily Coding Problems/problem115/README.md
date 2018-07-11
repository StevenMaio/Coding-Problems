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