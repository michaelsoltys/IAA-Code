# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 6.22 - ElGamal digital signature scheme
## Ryan McIntyre
## 7/6/2017
## python 3.5.2

import sys

#our exponent utility
def exp(a,n,m):#a^n mod m (a^n if m==0)
    nB = "{0:b}".format(int(n))
    A = [a]
    i = 1
    while i < len(nB):
        new = A[i-1]**2
        new = new%m
        A.append(new)
        i += 1
    i = 1
    output = 1
    while i <= len(nB):
        if int(nB[-i]) == 1:
            output *= A[i-1]
            output = output%m
        i += 1
    return output
    
#our handy euclid recursive, for computation of the multiplictive inverse mod p
def euc(m,n):
    if n==0:
        return(m,1,0)
    else:
        (d,x,y) = euc(n,m%n)
        return (d,y,x-int(m/n)*y)


#-------------------------------------------------------------------the scheme
def sign(message,p,g,x,k):
    h = 1
    i = 0
    while i < len(message):
        c = ord(message[i])
        h = h*c%p
        i += 1
    r = exp(g,k,p)
    s = euc(k,p-1)[1]*(h-x*r)%(p-1)
    if s == 0:
        print('Invalid value',k,'for k.')
        return None
    return(r,s)


if __name__ == '__main__':
    if len(sys.argv) == 5:
        p,g,x,k = [int(arg) for arg in sys.argv[1:]]
        inp = input('What message would you like to encode?\n... ')
        out = sign(inp,p,g,x,k)
        if out:
            print('Signature:',out)
    else:
        print('sign.py expected 4 additional arguements.',len(sys.argv)-1,'given.')