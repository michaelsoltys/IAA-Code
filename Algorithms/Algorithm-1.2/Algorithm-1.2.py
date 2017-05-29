# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Implementation of Algorithm 1.2
## Ryan McIntyre
## 5/25/2017
## python 3.5.2

import sys

def euc(a,b):
    
    #check pre-condition
    if a<=0 or b<=0 or a!=int(a) or b!=int(b):
        raise ValueError("Invalid inputs for Euclid's.")
        
    #Euclid's algorithm
    m = int(a)
    n = int(b)
    r = m%n #python for rem(m,n)
    while r>0:
        m = n
        n = r
        r = m%n
    print('The GCF of',a,'and',b,'is',str(n)+'.')
    return n
    
if __name__ == '__main__':
    if len(sys.argv) > 3:
        raise TypeError('Too many inputs for Euclids GCF.')
    elif len(sys.argv) < 3:
        raise TypeError('Too few inputs for Euclids GCF.')
    else:
        euc(int(sys.argv[1]),int(sys.argv[2]))