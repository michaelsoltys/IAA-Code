Implementation of the Gale-Shapely Stable Marriage algorithm.
Author: Ryan McIntyre

Matchmaking algorithm for disjoint sets of size n.

Input is expected to be file containing 2n lists, each of length n. 
Lines 0 through n-1 the first groups preference orders for matches 
in the second. Lines n through 2n-1 are the same for the second set's 
preferences on group 1.

For example, if n is 3, the first row could be [0,1,2], and there
should be 6 total rows in the input.

Output is stable matching of the two groups.

Sample output has been provided in 'input.txt'.
