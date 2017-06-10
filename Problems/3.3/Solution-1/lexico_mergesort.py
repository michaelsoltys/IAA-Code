# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 3.3 / Algorithm 3.2 - Mergesort (lexicographic order)
## Ryan McIntyre
## 6/8/2017
## python 3.5.2

import sys

#first we establish al alphabet, and an order for that alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = alphabet + ALPHABET
order = dict()
i = 0
while i < 26:
    order[alphabet[i]] = i
    order[ALPHABET[i]] = i
    i += 1


#next, we establish a comparison method for strings in our chosen alphabet
#returns 1 if x is before y, 0 if they match, -1 if y is before x
def compare(x,y):
    if x == y:
        return 0
    l = min([len(x),len(y)])
    i = 0
    while i < l:
        Ox = order[x[i]]
        Oy = order[y[i]]
        if Ox < Oy:
            return 1
        elif Oy < Ox:
            return -1
        i += 1
    if len(x) < len(y):
        return 1
    elif len(x) > len(y):
        return -1
    else:
        return 0 #they were "equal", but with different capiltalization

#Merging algorithm
def merge(X,Y):
    i = 0
    ix = 0
    iy = 0
    Z = []
    while i<len(X)+len(Y) and ix<len(X) and iy<len(Y):
        if compare(X[ix],Y[iy]) in [1,0]:
            Z.append(X[ix])
            ix += 1
        elif compare(X[ix],Y[iy]) == -1:
            Z.append(Y[iy])
            iy += 1
        else:
            print('Something went wrong #2.')
        i += 1
    if ix < len(X):
        Z += X[ix:]
    if iy < len(Y):
        Z += Y[iy:]
    return Z


#and, finally, mergesort
def mergesort(L):
    l = len(L)
    if l <= 1:
        return L
    else:
        r = l%2 #1 if odd, 0 if even...
        n = int(l/2) #int rounds down...
        L1 = L[:n+r] #first ceil(n/2)
        L2 = L[-n:]
        return merge(mergesort(L1),mergesort(L2))


#and we'll make a minimal main loop
if __name__ == '__main__':
    a = len(sys.argv)
    if a == 1:
        while True:
            inp = input('\nEnter a space-separated list of words for sorting.\n... ')
            args = [arg for arg in inp.split(' ') if arg]
            if args[0] in ['q','quit','Quit','QUIT','Q'] and len(args)==1:
                break
            else:
                omit = []
                i = 0
                while i < len(args):
                    toggle = True
                    for char in args[i]:
                        if not char in alpha:
                            omit.append(args[i])
                            del args[i]
                            toggle = False
                            break
                    if toggle:
                        i += 1
                ms = mergesort(args)
                print('\nSorted list:')
                print('   '+', '.join(ms)+'\n')
                if len(omit):
                    print('The following were omitted, as they contained unsupported characters:')
                    print('   '+'  '.join(omit)+'\n')
    else:
        args = sys.argv[1:]
        omit = []
        i = 0
        while i < len(args):
            toggle = True
            for char in args[i]:
                if not char in alpha:
                    omit.append(args[i])
                    del args[i]
                    toggle = False
                    break
            if toggle:
                i += 1
        ms = mergesort(args)
        print('\nSorted list:')
        print('   '+', '.join(ms)+'\n')
        if len(omit):
            print('The following were omitted, as they contained unsupported characters:')
            print('   '+'  '.join(omit)+'\n')