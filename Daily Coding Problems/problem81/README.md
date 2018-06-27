# Problem 81
Given a mapping of digits to letters (as in a phone number), and a digit
string, return all possible letters the number could represent. You can
assume each valid number in the mapping is a single digit.

For example if `{'2': ['a', 'b', 'c'], 3: ['d', 'e', 'f'], …}` then `'23'`
should return `['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']`.

## Solution
To use this solution, enter `python problem81.py filename s` where
`filename` is the name of the file whose content is the mapping of a digit
to strings, and `s` is the combination.