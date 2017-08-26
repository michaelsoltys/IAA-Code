# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 7.5 - Csanky (characteristic polynomial) via Newton's symmetric...
## Ryan McIntyre
## 8/25/2017
## python 3.5.2

from numpy import matrix, identity
from fractions import Fraction as frac
import sys

#---------------------------------------------------some basic matrix utilities

def tr(A): # trace of square matrix (numpy matrices probably have a
    n,m = A.shape # built-in trace, but I'll make my own...)
    if n!=m:
        raise ValueError(n,'by',m,'matrix input. Input must be square.')
    return sum([A.item(i,i) for i in range(n)])

def Id(n): # nxn identity
    return matrix(identity(n))

#-----------------------------------------------------------------the algorithm

def csanky(input_matrix):
    A = input_matrix
    n,m = A.shape
    if n!=m:
        raise ValueError(n,'by',m,'matrix input. Input must be square.')
    
    # get traces
    M = Id(n)
    trace = dict()
    i = 1
    while i <= n:
        M = M*A
        trace[i] = tr(M)
        i += 1
    
    s = {0:frac(1,1)}
    k = 1
    while k <= n:
        s[k] = sum([ (-1)**((i-1)%2)*s[k-i]*trace[i] for i in range(1,k+1)])/k
        k += 1
    
    rtn = ''
    k = 0
    while k <= n:
        rtn += '('+str(float(s[k]))+')\u00b7x^('+str(n-k)+')'
        if k%2==0:
            rtn += ' - '
        else:
            rtn += ' + '
        k += 1
    return rtn[:-3]

#--------------------------------------------------------------------------main

if __name__=='__main__':
    if len(sys.argv)==2:
        file = open(sys.argv[1],'r')
        A = matrix(file.read().replace('\n','').replace(' ',''))
        file.close()
        print('Characteristic polynomial:')
        print('   '+csanky(A))
    else:
        print('csanky.py expected 1 additional arguement.',len(sys.argv)-1,'given.')