Berkowitz's algorithm
Finds the characteristic polynomial of a square matrix
Author: Ryan McIntyre

Input is given in the command line as a file containing a matrix. This
matrix is a semicolon-separated list of rows, with the values within
rows separated by commas. An example is provided in input.txt.

	python berk.py input.txt

Output is the characteristic polynomial of the input matrix.

While Berkowitz's works in any field, this particular implementation
does not deal with precision issues in the reals. Try the
fractions.Fraction data type for this.
