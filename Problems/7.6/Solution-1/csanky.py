# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 7.6 - Csanky with matrix operations
## Ryan McIntyre
## 8/25/2017
## python 3.5.2

from numpy import matrix, identity, concatenate
from fractions import Fraction as frac
import sys

#--------------------------------------------------------------matrix utilities

def Id(n):#nxn identity
    return matrix(identity(n),dtype=int)
    
def tr(A): # trace of square matrix (numpy matrices probably have a
    n,m = A.shape # built-in trace, but I'll make my own...)
    if n!=m:
        raise ValueError(n,'by',m,'matrix input. Input must be square.')
    return sum([A[i,i] for i in range(n)])
    
def rec_lt_block_invert(input_matrix): # recursive inverse for lower triangular
    M = input_matrix # also assumes that there are no 0s on diagonal, which
    n,m = M.shape # works in this context (diagonal will be 1's)
    
    # make sure it's square...
    if n!=m:
        raise ValueError('Inverse of non-square matrix.')
    
    # base case...
    if n==1:
        return matrix([[frac(1,frac(M[0,0]))]])
    
    # make sure it's lower triangular...
    for i in range(n):
        for j in range(i+1,n):
            if M[i,j]!=0:
                raise ValueError('Inversion method is for lower triangular matrices only.')
    
    # split into blocks for recursion
    l = int(n/2) # size of smaller block
    A = M[:l,:l] # upper left
    B = M[l:,l:] # lower right
    E = M[l:,:l] # lower left
    O = M[:l,l:] # upper right, should be all zeros
    A = rec_lt_block_invert(A) # invert A
    B = rec_lt_block_invert(B) # invert B
    E = -B*E*A # "invert" E
    R = concatenate((concatenate((A,E),axis=0),concatenate((O,B),axis=0)),axis=1)
    return matrix(R)

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
    
    # and the core of the algorithm...
    b = matrix([[frac((-1)**(i+1)*trace[i],i) for i in range(1,n+1)]],dtype=object).transpose()
    T = matrix([[0 for i in range(n)] for j in range(n)],dtype=object)
    i = 0
    while i<n:
        j = 0
        while j<i:
            c = (-1)**(i-j+1)
            T[i,j] = frac(c*frac(1,i+1)*trace[i-j])
            j += 1
        i += 1
    T = Id(n)-T
    T = rec_lt_block_invert(T)
    return T*b # note: returns s1 through sn; s0 is 1 and is not in the result

#--------------------------------------------------------------------------main

if __name__=='__main__':
    if len(sys.argv)==2:
        file = open(sys.argv[1],'r')
        A = matrix(file.read().replace('\n','').replace(' ',''))
        file.close()
        n = len(A)
        A = csanky(A).getA1()
        poly = '1\u00b7x^('+str(n)+')'
        i = 0
        # let's pretty up the polynomial print a bit this time...
        while i < n:
            c = A[i]
            if c==int(c):
                c = int(c)
            if i%2==0:
                if c<0:
                    poly += ' + '+str(-c)+'\u00b7x^('+str(n-i-1)+')'
                elif c>0:
                    poly += ' - '+str(c)+'\u00b7x^('+str(n-i-1)+')'
            else:
                if c>0:
                    poly += ' + '+str(c)+'\u00b7x^('+str(n-i-1)+')'
                elif c<0:
                    poly += ' - '+str(-c)+'\u00b7x^('+str(n-i-1)+')'
            i += 1
        print('Characteristic polynomial:')
        print('   '+poly)
    else:
        print('csanky.py expected 1 additional arguement.',len(sys.argv)-1,'given.')