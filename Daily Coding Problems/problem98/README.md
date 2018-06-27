# Problem 98
Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example, given the following board:

	[
	  ['A','B','C','E'],
	['S','F','C','S'],
	['A','D','E','E']
	]

exists(board, "ABCCED") returns true, exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.

## Solution
To use this solution, enter `python problem98.py filename s` where `filename`
corresponds to the file whose content is the board, and `s` is the string
being searched for.