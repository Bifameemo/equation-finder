# equation-finder
Returns all possible ways to concatenate, add or subtract the numbers 1 to 9 in order to get the given input, in a single line of code!

> Example usage:

    >> func1(32)
    123 + 4 - 5 + 6 - 7 - 89 = 32
    12 + 3 + 4 - 56 + 78 - 9 = 32
    12 + 3 + 4 - 5 - 6 + 7 + 8 + 9 = 32
    12 + 3 - 4 + 5 + 6 - 7 + 8 + 9 = 32
    12 - 3 + 45 + 67 - 89 = 32
    12 - 3 + 4 + 5 + 6 + 7 - 8 + 9 = 32
    12 - 3 - 45 + 67 - 8 + 9 = 32
    12 - 3 - 4 + 5 - 67 + 89 = 32
    1 + 2 + 34 - 5 + 6 - 7 - 8 + 9 = 32
    1 + 2 + 34 - 5 - 6 + 7 + 8 - 9 = 32
    1 + 2 - 34 - 5 + 67 - 8 + 9 = 32
    1 - 23 + 4 + 56 - 7 - 8 + 9 = 32
    1 - 23 - 4 - 5 - 6 + 78 - 9 = 32
    1 - 2 + 34 - 5 - 6 - 7 + 8 + 9 = 32
    1 - 2 + 3 + 4 - 56 - 7 + 89 = 32
    1 - 2 + 3 - 45 + 6 + 78 - 9 = 32
    1 - 2 - 3 + 4 + 56 - 7 - 8 - 9 = 32
    1 - 2 - 3 - 45 - 6 + 78 + 9 = 32
    1 - 2 - 3 - 4 - 56 + 7 + 89 = 32

Future improvements:
1. write a shorter function without using `eval`
2. allow the range of numbers (1 to 9) to be varied
3. allow use of parentheses, multiplication (and division?)
