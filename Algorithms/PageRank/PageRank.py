# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## PageRank
## Ryan McIntyre
## 5/25/2017
## python 3.5.2

from fractions import Fraction as fr
from copy import copy
import sys

#input location of .txt with link matrix. txt should be a square of 1's and 0's
def PageRank(input_network, d=fr(17,20), iter_limit=1000, p=1000000000):
    '''1/p is proportional difference threshold between iterations
    i.e. |old-new|/old. iteration stops when iter_limit is reached
    or the largest proportional difference is less than 1/p.'''
    
    #First we check out input, make sure it's well-formed
    if d<=0 or d>1:
        raise ValueError('invalid value "'+str(d)+'" for d; must be in (0,1]')
    if p!=int(p) or p<1:
        raise ValueError(p,'must be a natural number (ideally a large one).')
    net = open(input_network,'r').read().splitlines()
    n = len(net)
    if any([len(row)!=n or any([char!='1' and char!='0' for char in row]) for row in net]):
        raise TypeError('PageRank input must be a square of 1\'s and 0\'s.')
    if any([net[i][i]!='0' for i in range(n)]):
        raise TypeError('Pages can\'t link to themselves.')

    #Next, we set up the initial state, in the form of dictionaries
    #vertex to outgoing link count first
    
    outgoing = dict([(i,sum([int(char) for char in net[i]])) for i in range(n)])
    old = dict([(i,fr(1,n)) for i in range(n)])#vertex to current value
    new = dict()#vertex to new value
    D = fr(1-d,n)
    
    #Finally, the core of the algorithm
    i = 0
    while i < iter_limit:
        new = dict([
            (i,
                 D+d*sum([int(net[j][i])*old[j]/outgoing[j] for j in range(n)])
            ) for i in range(n)
        ])
        if p==0 and new==old:
            break
        elif all([ abs((old[i]-new[i])/old[i]) < fr(1,p) for i in range(n) ]):
            break
        old = copy(new)
        i += 1
    if i==iter_limit:
        print('Warning: iter_limit reached. Series did not converge.')
    else:
        print('Iteration count:',i)
    for i in range(n):
        print('PR('+str(i)+') = '+str(round(float(new[i]),4)))
    return new

#We can run from the command line.
#ex: python some_directory/PageRank.py a_directory/input.txt d=some_number
if __name__ == "__main__":
    if len(sys.argv)>5:
        raise AttributeError('Too many inputs for PageRank.')
    elif len(sys.argv)<2:
        raise AttributeError('PageRank requires an input network.')
    else:
        arg = "PageRank('"+sys.argv[1]+"'"
        if len(sys.argv)>2:
            arg += ', '+', '.join(sys.argv[2:])
        arg += ')'
        eval(arg)