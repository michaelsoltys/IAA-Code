# Introduction to the Analysis of Algorithms (2nd ed)
# Michael Soltys
# Solution to problem 1.12

# Note that it only works in the case where all node labels are
# exactly one character (so we can have at least 2x26+10 of them - the
# uppler and lower case letters, together with the 10 digits; seems
# like enough).  Also note that there is no error detection; the
# input is assumed to be well formed


inf_bool = pre_bool = pos_bool = 0

f = open('prb-1.11.txt', 'r')
for line in f:
    if line[0:3]=='inf':
    	inf = line[5::2]
	inf = inf[1:]
	inf_bool = 1
    elif line[0:3]=='pos':
	pos = line[7::2]
	pos = pos[1:]
	pos_bool = 1
    elif line[0:3]=='pre':
	pre = line[6::2]
	pre = pre[1:]
	pre_bool = 1
    else:
    	print 'unknown format - exiting'
	exit
f.close()

print inf,pos
