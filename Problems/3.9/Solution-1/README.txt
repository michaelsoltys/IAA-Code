Solution to Problem 3.8 / Implementation of Savitch's algorithm
Author: Ryan McIntyre

Input is the location of a text file containing the adjacency 
matrix (a square of 1's and 0's) of a (directed) graph, along
with the indicies of two vertices (which are assumed to refer
to the corresponding row / column in the adjacency matrix).
A sample input has been provided in 'graph.txt'.

***Unlike most of our applications so far, index starts at 1***

Output is True or False. This version does not perfectly follow
the text's displayed output; if simply prints 'F' if the two
are not connected, and displays a "proof" of their connectedness
(i.e. a sequence of iterations of the recursion which returns 
True).

Call in the command line:
	python savitch.py

It will then prompt the user for a filename and two vertices,
which should be indexed by integers, starting at 1!
	... graph.txt 1 3
