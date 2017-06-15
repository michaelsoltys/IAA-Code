Solution to Problem 4.8
Implementation of Algorithm 4.2 (Floyd)
Author: Ryan McIntyre

Input is a text file containing an n by n square of comma
separated costs. Line separation is removed, so long as
the order fits the specified format. Any invalid costs
or non-positive costs will be read as "no edge".
A sample input has been provided in 'graph.txt'.

Output is a 2 dimensional array with the cost of a
shortest path between each pair of vertices, in the form
of a dictionary mapping each pair to its cost; the
vertices are named, implicitly, integers 0 to n-1,
where n is the vertex count. 
