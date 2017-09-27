# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Algorithm 7.3 - Gaussian Lattice Recuction
## Ryan McIntyre
## 8/25/2017
## python 3.5.2

from fractions import Fraction as frac
import sys

#--------------------------------------------------------------vector utilities

def dot(X,Y):
    sum = 0
    for x,y in zip(X,Y):
        sum += x*y
    return sum

def norm(X): # actually norm squared...
    return dot(X,X)

def mult(s,X):
    return [s*x for x in X]

#-----------------------------------------------------------------the algorithm

def reduce(v1,v2):
    v1 = [frac(v) for v in v1]
    v2 = [frac(v) for v in v2]
    while True:
        if norm(v2)<norm(v1):
            v1,v2 = v2,v1
        m = round(dot(v1,v2)/norm(v1),0)
        if m==0:
            return ([float(v) for v in v1],[float(v) for v in v2])
        v2 = [u2-m*u1 for u2,u1 in zip(v2,v1)]

#--------------------------------------------------------------------------main

if __name__=='__main__':
    if len(sys.argv)==2:
        file = open(sys.argv[1],'r')
        v1,v2 = ([eval(x) for x in vector.split(',')] for vector in file.read().replace('\n','').replace(' ','').split(';') if vector)
        file.close()
        R = [str(v) for v in reduce(v1,v2)]
        m = max([len(v) for v in R])
        print('  Result from lattice reduction:')
        for v in R:
            print(v.rjust(m+5))
    else:
        print('glr.py expected 1 additional input.',len(sys.argv)-1,'given.')