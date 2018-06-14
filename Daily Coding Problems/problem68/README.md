# Problem 68
On our special chessboard, two bishops attack each other if they share 
the same diagonal. This includes bishops that have another bishop located 
between them, i.e. bishops can attack through pieces.

### Running this solution
To run this solution, type `python3 problem68.py m b_1 b_2 ...` where `m` 
represents the parameter M in the problem, and `b_i` represent the bishops.

## Analysis
Two bishops will be able to attack each other if the difference of their
coordinates is of the form `(n, n)`, `(n, -n)` where `n` is some integer.
So to check all tuples of bishops, we end up with the number of bishops
squared checks.

By design, we will automatically have no unique tuples, because we only 
check tuples of the form `(i, j)` with `i < j`. And because we only check
such a tuple once, we will have only unique answers.

Thus, our answer will be the number of pairs described in the first 
paragraph.
