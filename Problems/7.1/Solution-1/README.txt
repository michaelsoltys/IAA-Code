Gaussian Elimination
Author: Ryan McIntyre

Input is a matrix, given in the command line, encoded (with no
spaces!) as a list of colon-separated rows, where each row is a
comma-separated list.

for example, this matrix:

	1  2  3  4
	5  6  7  8
	9 10 11 12

would be given like this:

	python GaussElim.py 1,2,3,4:5,6,7,8:9,10,11,12

Output is the result of Gaussian elimination, rounded to 2 decimal
places, and is printed in the console.
