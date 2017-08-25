2D Gaussian Lattice Reduction
Author: Ryan McIntyre

Input is given in the command line as a file containing a lattice basis.

	python glr.py input.txt

This basis is encoded as a semicolon-separated list of vectors, with values
within vectors separated by commas. See input.txt for an example.

Output is reduced (orthongonal) basis for the same 2D lattice.
No checks are done with respect to quality of input.
