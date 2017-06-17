Implementation of Algorithm 4.4
Greedy solution to knapsack
Author: Ryan McIntyre

Input is a comma separated list of positive integers. The first 
integer is C, the supremum capacity. The remaining integers are 
the weights. 

Input can be given on command line, as a txt file containing the
input, or typed in manually
	python sks.py input.txt
	python sks.py 17,1,2,4,8,16

Output is the greedy attempt to "fit" as much weight as possible
(<= C) in a container with maximum capacity C. Output is optimal,
as discussed in the text, the weights are in decreasing order and
each weight is at least as large as the the sum of all subsequent 
weights.
