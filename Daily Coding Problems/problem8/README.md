# Problem 8
A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

### Solution
To use this solution enter `python problem8.py filename` where `filename` is
the name of a file formated correctly.

To explain how the format, you must first give all of your nodes names.
The first line will consist of entries of the form `name, value`. Where value
refers to the value of the node whose name is `name`. On the second line, type
in the sequences of node names traveled in a preorder traversal (seperated by spaces).
One the third line, type the sequence of node names visited in the order of an
inorder traversal (also seperated by spaces).