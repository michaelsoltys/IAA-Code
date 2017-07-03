# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Implementation of binary integer operations
## Ryan McIntyre
## 7/2/2016
## python 3.5.2
import numpy as np

add_base = {'111':('1','1'),'110':('1','0'),'101':('1','0'),'011':('1','0'),
            '100':('0','1'),'010':('0','1'),'001':('0','1'),'000':('0','0')}
def add_two(X,Y):#X,Y are bin strings

    #deal with negatives
    if X[0] == '-':
        if Y[0] == '-':
            return '-'+add_two(X[1:],Y[1:])
        else:
            return sub_two(Y,X[1:])
    elif Y[0] == '-':
        return sub_two(X,Y[1:])
    
    #pad smaller input
    n = len(X)
    m = len(Y)
    NM = max(n,m)
    X = X.rjust(NM,'0')
    Y = Y.rjust(NM,'0')
    c = '0'
    S = ''
    
    i = NM-1
    while i >= 0:
        c,s = add_base[c+X[i]+Y[i]]
        S += s
        i -= 1
    if c == '1':
        S += c
    S =  S[::-1].lstrip('0')
    if S:
        return S
    return '0'

def sub_two(X,Y):#two positive inputs
    n = len(X)
    m = len(Y)
    if m > n:
        print(X)
        print(Y)
        return '-'+sub_two(Y,X)
    elif m == n:
        i = 0
        while i < m:
            if X[i] != Y[i]:
                if X[i] == '1':
                    break
                else:
                    print(X)
                    print(Y)
                    return '-'+sub_two(Y,X)
            i += 1
    Y = Y.rjust(n,'0')
    X = list(X)
    Y = list(Y)
    S = ''
    i = n - 1
    while i >= 0:
        x,y = X[i],Y[i]
        if x == y:
            S += '0'
        elif x == '1':
            S += '1'
        else:
            j = i-1
            while True:
                if X[j] == '1':
                    X[j] = '0'
                    j += 1
                    while j < i:
                        X[j] = '1'
                        j += 1
                    X[i] = '1'
                    S += '1'
                    break
                j -= 1
        i -= 1
    S = S[::-1]
    S = S.lstrip('0')
    if S:
        return S
    return '0'

def add(Z):#Z is list of bin strings
    S = '0'
    for X in Z:
        if X:
            S = add_two(S,X)
    if S:
        return S
    return '0'

#and we'll copy our recursive binary multiplication over from algorithm 3.6
#with a few edits to match "notation" of course
def multiply(X,Y):
    if X[0] == '-':
        if Y[0] == '-':
            return multiply(X[1:],Y[1:])
        return '-'+multiply(X[1:],Y)
    elif Y[0] == '-':
        return '-'+multiply(X,Y[1:])
    NM = max(len(X),len(Y))
    X = X.rjust(NM,'0')
    Y = Y.rjust(NM,'0')
    if NM==1:
        if X == Y == '1':
            return '1'
        else:
            return '0'
    n = int(NM/2)
    nu = n + NM%2
    x1 = X[:n]
    x0 = X[n:]
    y1 = Y[:n]
    y0 = Y[n:]
    
    z1 = multiply(add([x1,x0]),add([y1,y0]))
    z2 = multiply(x1,y1)
    z3 = multiply(x0,y0)
    
    S = add([z2+''.rjust(2*nu,'0'), add([z1,'-'+z2,'-'+z3])+''.rjust(nu,'0'), z3]).lstrip('0')
    if S:
        return S;
    return '0'

def ge(X,Y):# X >= Y
    if X[0] == '-':
        if Y[0] == '-':
            return ge(Y[1:],X[1:])
        return False
    if Y[0] == '-':
        return True
    X = X.lstrip('0')
    if not X:
        X = '0'
    Y = Y.lstrip('0')
    if not Y:
        Y = '0'
    if X == Y:
        return True
    n = len(X)
    m = len(Y)
    if n>m:
        return True
    if n==m:
        i = 0
        while True:
            if X[i] != Y[i]:
                if X[i] == '1':
                    return True
                return False
            i += 1
    return False

def g(X,Y):#X > Y
    if X[0] == '-':
        if Y[0] == '-':
            return g(Y[1:],X[1:])
        return False
    if Y[0] == '-':
        return True
    X = X.lstrip('0')
    if not X:
        X = '0'
    Y = Y.lstrip('0')
    if not Y:
        Y = '0'
    if X == Y:
        return False
    n = len(X)
    m = len(Y)
    if n>m:
        return True
    if n==m:
        i = 0
        while True:
            if X[i] != Y[i]:
                if X[i] == '1':
                    return True
                return False
            i += 1
    return False

def mod(X,Y):# X%Y
    if ge(Y,'0') and ge(X,'0'):
        m = len(Y)
        Y = Y.ljust(len(X),'0')
        while len(Y) >= m:
            while ge(X,Y):
                X = sub_two(X,Y)
            Y = Y[:-1]
        return X
    else:
        print('Modulus of negatives not supported.')
        return None

#and finally, exponentiation mod p
def exp(a,b,p):#a,b, p are bin strings
    A = [a]
    i = 1
    while i <= len(b):
        new = mod(multiply(A[-1],A[-1]),p)
        A.append(new)
        i += 1
    result = '1'
    i = 1
    while i <= len(b):
        if b[-i] == '1':
            result = mod(multiply(result,A[i-1]),p)
        i += 1
    return result