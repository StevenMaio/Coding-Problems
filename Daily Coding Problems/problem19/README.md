# Problem 19
A builder is looking to build a row of N houses that can be of K different
colors. He has a goal of minimizing cost while ensuring that no two
neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost
to build the nth house with kth color, return the minimum cost which achieves this goal.

## Solution
To use this solution, enter `python problem19.py filename` where `filename`
correspeonds to the name of the file which contains our price matrix.

It's worth noting that this solution doesn't really work well with repeated
values for one house. To further elaborate, if `h` is a house then no two
colors `c1`, `c2` will have the same cost for house `h`.