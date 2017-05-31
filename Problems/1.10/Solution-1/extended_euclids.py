# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## The Extended Euclid's Algorithm
## Ryan McIntyre
## 5/25/2017
## python 3.5.2

import sys

def ext_euc(m,n):
    
    #check pre-conditions
    if m<=0 or n<=0 or m!=int(m) or n!=int(n):
        raise ValueError("Invalid inputs for Euclid's.")
    
    #algorithm
    c = m
    d = n
    a = 0
    x = 1
    b = 1
    y = 0
    while(True):
        q = int(c/d)#int(float) rounds the float down
        r = c%d
        if r == 0:
            print(str(a)+'*'+str(m),'+',str(b)+'*'+str(n),'=',d,
                  '= gcf('+str(m)+','+str(n)+')')
            return (a,b)
        c = d
        d = r
        h = x
        x = a
        a = h - q * a
        h = y
        y = b
        b = h - q * b

if __name__ == '__main__':
    if len(sys.argv)!=3:
        raise TypeError('Euclid\'s requires two inputs.')
    else:
        ext_euc(int(sys.argv[1]),int(sys.argv[2]))