# Problem 44
We can determine how "out of order" an array A is by counting the number 
of inversions it has. Two elements A[i] and A[j] form an inversion if 
A[i] > A[j] but i < j. That is, a smaller element appears after a 
larger element.

Given an array, count the number of inversions it has. Do this faster 
than O(N^2) time.

## Using this solution
To run this solution type `python problem44.py n`. The program will then 
generate an array with `n` random elements, print all of the elements, and
then count the number of inversions.
