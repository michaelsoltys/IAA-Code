Gram-Schmidt
Converts basis to orthogonal basis
Author: Ryan McIntyre

Input is given in the command line as a file containing a basis. This
basis is a semicolon-separated list of vectors, with the values within
vectors separated by commas. New lines and blank spaces are ignored.
An example is provided in input.txt.

	python gs.py input.txt

Output is the result of Gram-Schmidt on the input basis, and is
printed to the console. No checks are done regarding the quality of
the input; if it is not a basis, the result won't be either (though it
should still be orthogonal and have the same span as the input).
