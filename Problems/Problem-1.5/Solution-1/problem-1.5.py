# Introduction to the Analysis of Algorithms (2nd ed)
# Michael Soltys
# Solution to problem 1.17
# February 20, 2015

import sys

def division(x,y):
	q = 0
	r = x
	print "q = ",0
	print "r = ",x
	while y <= r:
		r = r-y
		q = q+1
		print "q = ",q
		print "r = ",r
	print "%d = %dx%d + %d" % (x,q,y,r)

division(int(sys.argv[1]),int(sys.argv[2]))
