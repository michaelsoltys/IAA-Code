Implementation of Algorithm 6.1
Author: Ryan McIntyre

Input is given in the command line a text file containing
the adjacency matrix of tuhe input graph, the "mode"
(either 'any' or 'fl'), and (optionally) the number of
iterations (default 100). mode "any" is for existence of
any perfect matching, whereas "fl" is for a perfect matching
specifically between the "first half" and "last half" of the
vertices as implied by the order of the adjacency matrix.
A sample input has been provided.

sample call:
	python match.py adj.py any 100

Output is (probably) True if a perfect matching exists, and
certainly False if no such matching exists.
