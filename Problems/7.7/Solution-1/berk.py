# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 7.7 - Berkowitz
## Ryan McIntyre
## 8/26/2017
## python 3.5.2

from numpy import matrix, identity
import sys


def Id(n):#nxn identity
    return matrix(identity(n),dtype=int)

'''This demonstrates the algorithm, but does not deal with precision
issues in the reals (use fractions.Fraction for this!)'''

def berk(input_matrix):
    A = input_matrix
    n,m = A.shape
    N = n
    if n!=m:
        raise ValueError('Input matrix must be square.')
    C = dict()
    i = 1
    while n > 0:
        a = A[0,0]
        R = A[0,1:]
        S = A[1:,0]
        A = A[1:,1:]
        c = dict()
        c[0] = 1
        c[1] = -a
        c[2] = -R*S
        M = Id(n-1)
        for l in range(2,n+1):
            M = M*A
            c[l] = -R*M*S
        C[i] = matrix([[0 for i in range(n)] for j in range(n+1)])
        for l in range(n):
            C[i][l,l] = c[0]
        for l in range(1,n+1):
            for k in range(0,n-l+1):
                C[i][l+k,0+k] = c[l]
        n,m = A.shape
        i += 1
    R = Id(N+1)
    for i in range(1,N+1):
        R = R*C[i]
    return R

#--------------------------------------------------------------------------main

if __name__=='__main__':
    if len(sys.argv)==2:
        file = open(sys.argv[1],'r')
        A = matrix(file.read().replace('\n','').replace(' ',''))
        file.close()
        n = len(A)
        A = berk(A).getA1()
        poly = str(A[0])+'\u00b7x^('+str(n)+')'
        i = 1
        # let's pretty up the polynomial print a bit this time...
        while i <= n:
            c = A[i]
            if c<0:
                poly += ' - '+str(-c)+'\u00b7x^('+str(n-i)+')'
            elif c>0:
                poly += ' + '+str(c)+'\u00b7x^('+str(n-i)+')'
            i += 1
        print('Characteristic polynomial:')
        print('   '+poly)
    else:
        print('berk.py expected 1 additional arguement.',len(sys.argv)-1,'given.')