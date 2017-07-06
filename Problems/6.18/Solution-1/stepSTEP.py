# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Implementation of Algorithm 6.4 - Shank's babystep-giantstep
## Ryan McIntyre
## 7/05/2017
## python 3.5.2

from math import sqrt
import sys

#our handy euclid recursive, for computation of the multiplictive inverse mod p
def euc(m,n):
    if n==0:
        return(m,1,0)
    else:
        (d,x,y) = euc(n,m%n)
        return (d,y,x-int(m/n)*y)


#the algorithm
def sS(p,g,h):

    #assume p is prime, g,h in Zp, and g generates Zp
    n = 1 + int(sqrt(p))
    L1 = [1]
    i = 1
    while i <= n:
        L1.append((L1[-1]*g)%p)
        i += 1
    gm = euc(L1[-1],p)[1]%p
    L2 = [h]
    i = 0
    while i <= n:
        L2.append((L2[-1]*gm)%p)
        i += 1
    i = 1
    while i <= n:
        if L1[i] in L2:
            j = L2.index(L1[i])
            x = j*n+i
            return x
        i += 1
    print('No solution found; maybe',g,'is not a generator modulus',str(p)+'?')
    return None


if __name__ == '__main__':
    if len(sys.argv) == 4:
        p,g,h = sys.argv[1:]
        p,g,h = int(p),int(g),int(h)
        r = sS(p,g,h)
        if r != None:
            print(g,'^',r,'=',h,'mod('+str(p)+')')
    else:
        print('stepSTEP.py expected 3 additional inputs.',len(sys.argv)-1,'given.')