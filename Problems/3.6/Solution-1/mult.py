# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 3.5 / Algorithm 3.3 - Recursive Binary Multiplication
## Ryan McIntyre
## 6/11/2017
## python 3.5.2

import sys

#for the book's algorithm, see the recursive portion below
def multiply(bx,by):
    n = max(len(bx),len(by))
    bx = bx.rjust(n,'0')
    by = by.rjust(n,'0')
    if n==1:
        if bx == by == '1':
            return '1'
        else:
            return '0'
    
    n2 = int(n/2)
    nu = n2 + n%2
    x1 = bx[:n2]
    x0 = bx[n2:]
    y1 = by[:n2]
    y0 = by[n2:]
    
    z1 = multiply(add([x1,x0]),add([y1,y0]))
    z2 = multiply(x1,y1)
    z3 = multiply(x0,y0)
    
    return add([z2+''.rjust(2*nu,'0'), add([z1,'-'+z2,'-'+z3])+''.rjust(nu,'0'), z3])

#and here we have the laziest binary addition imaginable
def add(bins):
    return format(sum([int(bi,2) for bi in bins]),'b')

if __name__ == '__main__':
    if len(sys.argv) > 2:
        prod = '1'
        valid = True
        for arg in sys.argv[1:]:
            try:
                prod = multiply(prod,arg)
            except:
                print('Invalid input',arg)
                valid = False
                break
        if valid:
            print('Product is',prod+', which is',int(prod,2),'in base 10.')
    else:
        print('mult.py expected at least 2 additional arguements.',len(sys.argv)-1,'given.')