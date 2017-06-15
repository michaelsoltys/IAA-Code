Solution to Problem 4.9 
Implementation of the Bellman-Ford algorithm
Finds shortest paths to a given vertex in a directed graph
Author: Ryan McIntyre

Input: 
	a text file containing the costs of the edges in a 
		directed graph (comma-separated). n^2 costs for graph
		with n edges. 
	two integer indices, s and t, where a vertex's index
		ranges from 0 to n-1 and corresponds to the implicit
		labelling in the input text

An example directed graph has been given in graph.txt.
Sample call, from command line:
	python Bellman-Ford.py graph.txt 0 5

Output is the total cost of the shortest path from s to t.
Note that the algorithm could easily me modified to list
all intermediate nodes on the shortest path from s to t.
