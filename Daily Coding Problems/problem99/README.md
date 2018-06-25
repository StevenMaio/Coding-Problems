# Problem 99
Given an unsorted array of integers, find the length of the longest
consecutive elements sequence.

For example, given `[100, 4, 200, 1, 3, 2]`, the longest consecutive element
sequence is `[1, 2, 3, 4]`. Return its length: `4`.

Your algorithm should run in `O(n)` complexity.

## Solution
To use this solution, enter `python problem99.py a_1 a_2 ... a_n` where `a_ii`
is the i-th element in the array.

## Analysis
Questions that first come to mind

1. Does the order of the elements matter?
2. Can I assume that `a` will always be nonempty?
3. Do I needto worry about the possiblity of there being two consecutive
element sequences of the same length (both of which are equal to the max)?
4. Is every element in `a` unique? Follow up, can we ignore duplicate
elements?

First idea, we can sort `a` and then find the length of the longest contigous
sub array. The sorting part of this problem can be performed in `O(n log(n))`
time, and the second part of this procedure will take roughyl `O(n)` time.

Other idea, we can use a dictionary, and whenever we add a new value `x`, we
can check to see either `x-1` or `x+1` are keys in the dictionary already.