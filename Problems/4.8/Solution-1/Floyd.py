# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 4.8 - Floyd
## Ryan McIntyre
## 6/11/2017
## python 3.5.2

from math import sqrt
import sys

def floyd(input_text):
    
    #we're going to assume, this time, that the input is well-defined
    #first we read the input, set up a dictionary from each ordered pair
    #of vertices to its corresponding cost / weight
    inp = open(input_text,'r').read().replace('\n','').split(',')
    args = [arg.replace(' ','') for arg in inp if arg]
    n = sqrt(len(args))
    if n != int(n):
        return None
    else:
        n = int(n)
    C = dict([ ((i,j),args[n*i+j]) for i in range(n) for j in range(n) ])
    
    
    #the algorithm
    B = dict()
    for i in range(n):
        for j in range(n):
            try:
                if eval(C[(i,j)]) > 0:
                    B[(i,j)] = eval(C[(i,j)])
                else:
                    B[(i,j)] = float('inf')
            except:
                B[(i,j)] = float('inf')
    for k in range(n):
        for i in range(n):
            for j in range(n):
                B[(i,j)] = min([B[(i,j)],B[(i,k)]+B[(k,j)]])
    return B

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Floyd expected 1 additional arguement, a text file.')
    else:
        B = floyd(sys.argv[1])
        n = int(sqrt(len(B)))
        m = max([len(str(s)) for s in list(B.values())+[i for i in range(n)]])+1
        display = ['|'.rjust(m+2)+''.join([str(i).rjust(m) for i in range(n)])]
        display.append(' '.rjust(m+2,'-').ljust(len(display[0]),'-'))
        for i in range(n):
            display.append(str(i).rjust(m)+' |'+''.join([str(B[(i,j)]).rjust(m) for j in range(n)]))
        for line in display:
            line = line.replace('inf'.rjust(m),'__'.rjust(m))
            print(line)
        