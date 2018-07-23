# Problem 127

Let's represent an integer in a linked list format by having each node
represent a digit in the number. The nodes make up the number in reversed
order.

For example, the following linked list:

	1 -> 2 -> 3 -> 4 -> 5

is the number `54321`.

Given two linked lists in this format, return their sum in the same linked
list format.

For example, given

	9 -> 9

	5 -> 2

return `124 (99 + 25)` as:

	4 -> 2 -> 1

## Solution

To use this solution, enter `python problem127 x y` wherein `x` and `y` are
two numbers which will be turned into a linked list, and then summed together