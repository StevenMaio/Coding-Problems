# Problem 72
In a directed graph, each node is assigned an uppercase letter. We define 
a path's value as the number of most frequently-occurring letter along 
that path. For example, if a path in the graph goes through "ABACA", the 
value of the path is 3, since there are 3 occurrences of 'A' on the path.

Given a graph with n nodes and m directed edges, return the largest value 
path of the graph. If the largest value is infinite, then return null.

### This Solution
This solution makes a lot of assumptions, the first being that the graph is
topologically sorted. If the graph cannot be topologically sorted, then our
graph contains a cycle and our result will be `null`.

To run this solution, type into the command line `python problem72.py 
abc...e i,j m,n ... a,b` where `abc..e` refers to the values of the nodes, 
that is node `i`'s value will be the in the i-th index. And `m,n` refers
to an edge connection node `m` and node `n`.
