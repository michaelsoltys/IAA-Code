# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 2.15 - Grid spanning forest
## Ryan McIntyre
## 6/3/2017
## python 3.5.2

import sys

def kruskal_grid(input_text):
    
    #check that input is a grid
    grid = [s.strip() for s in ''.join(open(input_text,'r').readlines()).split(':')]
    n = int(grid[0])#grid size
    if n != int(n):
        raise ValueError('Grid size should be a positive integer.')
    v = n*n#vertex count
    edges = eval('['+grid[1]+']')
    i = 0
    while i < len(edges):
        (a,b,w) = edges[i]
        if any([a!=int(a), b!=int(b), a<0, b<0, a>=v, b>=v, w<0]):
            raise ValueError('Invalid vertex index or weight.')
        if a==b:
            raise ValueError('Vertices may not be connected to themselves.')
        if a>b:
            a,b = b,a
            edges[i] = (a,b,w)
        if b!=a+4 and (b!=a+1 or a%4==3):
            raise ValueError('Input is not a grid or is not in the specified form.')
        i += 1
    
    #kruskals
    edges.sort(key = lambda x : x[2])
    F = set()#forest
    C = dict([(i,i) for i in range(v)])#components
    c = 0#cost
    for e in edges:
        (a,b,w) = e
        k = C[a]
        l = C[b]
        if l!=k:
            F.add((a,b))
            for i in range(v):
                if C[i]==l:
                    C[i]=k
            c += w
    
    #display
    D = ''
    i = 0
    while i < n:
        l1 = ''
        l2 = ''
        j = 0
        while j < n:
            a = 4*i+j
            b = a+1
            c = a+4
            if (a,b) in F:
                l1 += 'o--'
            else:
                l1 += 'o  '
            if (a,c) in F:
                l2 += '|  '
            else:
                l2 += '   '
            j += 1
        D += l1 +'\n'
        if i<n-1:
            D += l2 + '\n'
        i += 1
    
    print(D)
    print('Total Cost of Span:',c)
    return F
    
if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        raise ValueError('Wrong number of inputs for kruskal\'s - 1 expected.')
    kruskal_grid(args[1])