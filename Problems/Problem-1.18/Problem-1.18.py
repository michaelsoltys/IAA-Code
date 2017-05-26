# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 1.18 Solution - PageRank
## Ryan McIntyre
## 5/25/2017
## python 3.5.2

from fractions import Fraction as fr
from copy import copy

#input location of .txt with link matrix. txt should be a square of 1's and 0's
def PageRank(input_network, d=fr(17,20), iter_limit=1000, p=.01):
    #p is proportional difference, below which algorithm will cease
    
    #First we check out input, make sure it's well-formed
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
        elif all([ abs(float((old[i]-new[i])/old[i])) < p for i in range(n) ]):
            break
        old = copy(new)
        i += 1
    for i in range(n):
        print('PR('+str(i)+') = '+str(float(new[i])))
    return new
    
PageRank('input.txt')