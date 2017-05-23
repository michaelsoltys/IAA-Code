# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:34:13 2016

@author: arewh
"""
from math import floor
from collections import deque


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
                u = 1 + floor((i)/self.size)
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

graph = Graph('graph.txt') #input adjacency matrix filename
goTime = Savitch(graph,1,4) #(graph,vertexOne,vertexTwo) where the vertices are 1,2,...,n
#outputs "proof" of connection or "F" if no connection
