# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 4.9 - Bellman-Ford
## Ryan McIntyre
## 6/11/2017
## python 3.5.2

from math import sqrt
import sys

def bf(input_text,s,t):
    
    #open text, establish cost dictionary
    inp = open(input_text,'r').read().replace('\n','').split(',')
    args = [arg.replace(' ','') for arg in inp if arg]
    n = sqrt(len(args))
    if n != int(n):
        print('Invalid number of costs.')
        return None
    else:
        n = int(n)
    if not t in range(n):
        print('Invalid index',t,'for graph with',n,'vertices.')
        return None
    if not s in range(n):
        print('Invalid index',s,'for graph with',n,'vertices.')
        return None
    C = dict([ ((i,j),eval(args[n*i+j])) for i in range(n) for j in range(n) ])
    valid = True
    for edge in C:
        if C[edge] == 0:
            C[edge] = float('inf')
        elif C[edge]<0 or edge[0]==edge[1] :
            valid = False
    
    if valid:
        Opt = []
        for j in range(n):
            Opt.append(C[(j,t)])
    
        for i in range(n):
            for v in range(n):
                Opt[v] = min( Opt[v], min( [C[v,w]+Opt[w] for w in range(n)] ) )
        print('The shortest path from',s,'to',t,'has total cost',Opt[s])
        return Opt[s]
    
    else:
        print('No single-vertex cycles or negative costs please thanks.')
        return None

if __name__ == '__main__':
    if len(sys.argv) == 4:
        g = sys.argv[1]
        try:
            s = int(sys.argv[2])
            t = int(sys.argv[3])
        except:
            print('Vertices are input as integer indices from 0 to n-1.')
        else:
            bf(g,s,t)
    else:
        print('Bellman-Ford expected 3 additional arguements.',len(sys.argv)-1,'given.')