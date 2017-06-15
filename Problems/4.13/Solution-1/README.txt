Solution to Problem 4.13 / Implementation of Algorithm 4.3 
Maximizes actual capacity of knapsack, given capacity and weights
Author: Ryan McIntyre

Input is a comma separated list of positive integers, or a a text
file containing one. The first integer is the supremum capacity, C. 
The rest define a multi-set W of weights.

Call in the command line
	python sks.py input.txt

Output is a list of the weights which fit in a sack with capacity C, 
and moreover minimizes the "unused" capacity.
