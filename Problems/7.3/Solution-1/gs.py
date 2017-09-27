# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 7.3 / Algorithm 7.2 - Graham Schmidt
## Ryan McIntyre
## 8/24/2017
## python 3.5.2

# fractions help us avoid rounding issues
from fractions import Fraction as frac
import sys

#--------------------------------------------------------------vector utilities

def dot(X,Y):
    sum = 0
    for x,y in zip(X,Y):
        sum += x*y
    return sum

def norm(X): #actually norm squared...
    return dot(X,X)

def mult(s,X):
    return [s*x for x in X]

#-----------------------------------------------------------------the algorithm

# it is assumed that the input is well-formed, no checks are done
def gram_schmidt(B):
    B = [[frac(float(a)) for a in b] for b in B]
    O = [B[0]]
    n = len(B)
    u = dict()
    for i in range(1,n):
        V = B[i]
        for j in range(i):
            u[(i,j)] = dot(B[i],O[j]) / norm(O[j])
            V = [v-u[(i,j)]*o for v,o in zip(B[i],O[j])]
        O.append(V)
    return [[float(a) for a in o] for o in O]
    # return floats because they're prettier when printed...

#--------------------------------------------------------------------------main

if __name__=='__main__':
    if len(sys.argv)==2:
        file = open(sys.argv[1],'r')
        B = [[eval(x) for x in vector.split(',')] for vector in file.read().replace('\n','').replace(' ','').split(';') if vector]
        file.close()
        O = [str(v) for v in gram_schmidt(B)]
        m = max([len(v) for v in O])
        print('  Result from Gram-Schmidt:')
        for v in O:
            print(v.rjust(m+5))
    else:
        print('gs.py expected 1 additional input.',len(sys.argv)-1,'given.')