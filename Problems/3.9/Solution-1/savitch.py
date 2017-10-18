# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to problem 3.8
## Ryan McIntyre
## 11/03/2016
## python 3.5.2

from collections import deque
import sys


class Graph(object):
    def __init__(self,stringFileName):
        f = open(stringFileName,'r')
        adjacencyString = ''
        self.size = 0
        for line in f:
            adjacencyString += line[:-1]
            self.size += 1
        self.vertices = list(range(1,self.size+1))
        self.edges = []
        i = 0
        while i < len(adjacencyString) :
            if  adjacencyString[i:i+1] == '1':
                u = 1 + int((i)/self.size)
                v = 1 + i%self.size
                self.edges.append([u,v])
            i += 1

class Savitch(object):
    def __init__ (self,G,u,v):
        self.g = G
        j = 1
        i = 0
        while j < G.size:
            j *= 2
            i += 1
        self.moves = dict()
        check = self.R(u,v,i)
        if check:
            stack = deque()
            stack.appendleft((u,v,i))
            while len(stack):
                self.display(stack)
                if stack[-1] != 'T':
                    print('----------------')
                node = stack.popleft()
                if node != 'T':
                    new = self.moves[node]
                    if new == 'T':
                        stack.appendleft(new)
                    else:
                        stack.appendleft(new[1])
                        stack.appendleft(new[0])
        else:
            print('F')
                        
                
    def R(self,u,v,i): #savitch recursive
        if i==0:
            if u==v:
                self.moves[(u,v,i)] = 'T'
                return True
            elif [u,v] in self.g.edges:
                self.moves[(u,v,i)] = 'T'
                return True
        else:
            for w in self.g.vertices:
                if self.R(u,w,i-1) and self.R(w,v,i-1):
                    self.moves[(u,v,i)] = [(u,w,i-1),(w,v,i-1)]
                    return True
        return False
    def display(self,stack):
        for item in stack:
            if item == 'T':
                print(item)
            else:
                print('R(G,',item[0],',',item[1],',',item[2],')')

#graph = Graph('graph.txt') #input adjacency matrix filename
#goTime = Savitch(graph,1,4) #(graph,vertexOne,vertexTwo) where the vertices are 1,2,...,n
#outputs "proof" of connection or "F" if no connection

if __name__ == '__main__':
    if len(sys.argv) == 1:
        while True:
            inp = input('Enter the location of the adjacency matrix and '+
                        'two integer indices of vertices, for Savitch\'s\n... ')
            args = [x.replace(' ','') for x in inp.split(' ') if x]
            if args[0] in ['q','Q','quit','Quit','QUIT']:
                break
            if len(args) == 3:
                graph = None
                try:
                    graph = Graph(args[0])
                except:
                    print('Invalid input',args[0])
                else:
                    u = 0
                    v = 0
                    try:
                        u = int(args[1])
                        v = int(args[2])
                    except:
                        print('Non-integer vertex index',args[1],'or',args[2])
                    else:
                        n = graph.size
                        if u<1 or v<1 or u>n or v>n:
                            print('Invalid vertex index',args[1],'or',args[2])
                        else:
                            Savitch(graph,u,v)
                            break
            else:
                print('\nExpected 4 arguements.',len(args),'given.\n')
        