# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to problem 1.16 (1.25 in 2nd ed)
## February 20, 2015
## Python 2

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
