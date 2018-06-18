# Problem 92
We're given a hashmap with a key courseId and value a list of courseIds, 
which represents that the prerequsite of courseId is courseIds. Return a 
sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given 
`{'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}`, 
should return `['CSC100', 'CSC200', 'CSCS300']`.

### Solution
To use this solution, enter `python problem92.py filename`, where `filename`
refers to the filename of the input data.

Input must formatted on each line as such

`v u_1 u_2 ... u_n`

where `v` represents the course, and each `u_i` represents a prerequesite of
the course. If the course has no prerequisites, then have a line with only
the name of that course on it.

You can find examples of how to format input in the `.txt` files.