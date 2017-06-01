# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Algorithm 2.1 - Kruskal's minimum cost spanning tree
## Ryan McIntyre
## 5/31/2017
## python 3.5.2

import sys

def kruskal(input_text):
    
    #read input, make sure it's valid
    lines = [line[:-1].split(',') for line in open(input_text,'r').readlines()]
    n = len(lines)
    if any([len(line)!=n for line in lines]):
        raise ValueError('Invalid input for Kruskal.')
    lines = [[float(value) for value in line] for line in lines]
    if any([any([value<0 for value in line]) for line in lines]):
        raise ValueError('Weights must be positive.')
    if any([lines[i][i]!=0 for i in range(n)]):
        raise ValueError('Nodes may not be connected to themselves.')
    if any([lines[i][j]!=lines[j][i] for i in range(n) for j in range(i+1,n)]):
        raise TypeError('Input graph must be undirected.')
    
    #convert to list of edges
    edges = []
    for i in range(n):
        for j in range(i+1,n):
            c = lines[i][j]
            if c!=0:
                edges.append((i,j,c))
                
    #sort edges by ascending cost
    edges.sort(key = lambda x: x[2])
    
    #define component dictionary ('D' in text)
    C = dict([(i,i) for i in range(n)])
    
    #the algorithm
    Tree = []
    cost = 0
    m = len(edges)
    for i in range(m):
        e = edges[i]
        k = C[e[0]]
        l = C[e[1]]
        if k != l:
            Tree.append((e[0],e[1]))
            cost += e[2]
            for j in range(n):
                if C[j] == l:
                    C[j] = k
    print('The edges',Tree,'form a MCST with total cost',str(round(cost,2))+'.')
    return(Tree,cost)

if __name__ == '__main__':
    if len(sys.argv)==2:
        kruskal(sys.argv[1])
    else:
        raise ValueError('Expected 1 argument, got',str(len(sys.argv))+'.')