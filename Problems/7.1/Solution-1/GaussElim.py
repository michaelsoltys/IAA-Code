# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 7.1 / Algorithm 7.1 - Gaussian Elimination
## Ryan McIntyre
## 8/23/2017
## python 3.5.2

#note: sympy has utilities for rref.

from numpy import matrix, identity, insert #thanks numpy
import sys

#---------------------------------------------Identity and Elementary functions

def Id(n):#nxn identity
    return matrix(identity(n))

def E1(n,a,i,j):
    if i==j:
        raise ValueError('i can\' equal j for E1.')
    E = Id(n)
    E[i,j] += a
    return E

def E2(n,i,j):
    E = Id(n)
    if i==j:
        return E
    E[i,j] += 1
    E[j,i] += 1
    E[i,i] -= 1
    E[j,j] -= 1
    return E

def E3(n,c,i):
    E = Id(n)
    E[i,i] += c-1
    return E

#----------------------------------------------------------Gaussian Elimination

def gauss(input_matrix):
    
    M = input_matrix
    (n,m) = M.shape
    
    V = M.getA1() # get flattened array of values
    if n==1: # if only 1 row...
        if all(v==0 for v in V):
            return matrix('1')*M
        
        l = 0
        while True:
            if V[l]!=0:
                return matrix([1/V[l]])*M
            l += 1
    
    if all(v==0 for v in V): # if we have the 0 matrix...
        return Id(n)
    
    TA = M.transpose().getA() # for easily indexing columns
    
    if all(v==0 for v in TA[0]): #if first column is 0...
        j = 1
        while True:
            if any(v!=0 for v in TA[j]):
                break
            j += 1
        i = 0
        while True:
            if M.item((i,j))!=0:
                break
            i += 1
        if i==0:
            if all(M[l,j]==0 for l in range(1,n)):
                E = Id(n)
            else:
                a_ij = M[i,j]
                L = [l for l in range(1,n) if M[l,j]!=0]
                A = [-M[l,j]/a_ij for l in L]
                es = [E1(n,A[l],L[l],i) for l in range(len(L))]
                E = Id(n)
                for e in es:
                    E = E*e     
    
    else:
        i = 0
        while True:
            if M[i,0]!=0:
                a = M[i,0]
                break
            i += 1
        J = [j for j in range(i+1,n) if M[j,0]!=0]
        k = len(J)
        EE = E2(n,i,0)
        EEE = E3(n,1/a,i)
        if k==0:
            E = EEE*EE
        else:
            A = [-M[j,0] for j in J]
            es = [E1(n,A[j],J[j],0) for j in range(k)]
            E = Id(n)
            for e in es:
                E = E*e
            E = E*EE*EEE
    
    X = E*M
    X = X.getA()
    Xt = X[0]
    X = matrix([x[1:] for x in X[1:]])
    X = gauss(X)
    X = insert(X,0,0,axis=1)
    X = insert(X,0,Xt,axis=0)
    return X
    

if __name__=='__main__':
    if len(sys.argv)==2:
        input_matrix = matrix(sys.argv[1].replace(':',';'))
        result = gauss(input_matrix).round(2)
        maxlength = max(max(len(str(value)) for value in row) for row in result)
        print('Result from Gaussian Elimination:')
        for row in result:
            print(''.join([str(value).rjust(maxlength+2) for value in row]))
    else:
        print('GaussElim.py expected 1 additional input.',len(sys.argv)-1,'given.')