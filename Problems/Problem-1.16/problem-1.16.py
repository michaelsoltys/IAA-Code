# Introduction to the Analysis of Algorithms (2nd ed)
# Michael Soltys
# Solution to problem 1.25
# February 20, 2015

import sys

def ulam(n):
	while n != 1:
		print n,
		if n%2 == 0:
			n = n/2
		else:
			n = n*3+1

ulam(int(sys.argv[1]))
print 1
