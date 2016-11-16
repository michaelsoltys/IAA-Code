# To change this template, choose Tools | Templates
# and open the template in the editor.
#
# Original here:
# https://github.com/mmoniz/Minimum-Spanning-Tree---Kruskal

__author__="Mike Moniz"
__date__ ="$31-Jan-2011 7:49:45 PM$"

from os.path import exists
from sys import stdout
import re
import copy
import os.path


def MergingComponents(grid,index):
    k = D[grid.edges[index].v1 -1]
    l = D[grid.edges[index].v2 -1]

    for j in range(len(D)):
        if(D[j] == l):
            D[j] = k

def hasNoCycle(r,s):
    if(D[r] == D[s]):
        return False
    else:
        return True

def Kruskal(grid):
    insertSort(grid)
    T = Grid(grid.degree,[])
    for i in range(len(grid.edges)):
        if (hasNoCycle(grid.edges[i].v1 -1,grid.edges[i].v2 -1)):
                T.addEdge(grid.edges[i])
                MergingComponents(grid,i)
        display(T)
    return T

# Reads the file; returns a Grid
def getGridFromFile(filepath = "graph.txt"):
	if not exists(filepath): return None
	f = open(filepath, 'r')
	s = f.read()
	f.close()

	if not re.match('^\s*\d+\s*:(\s*\(\s*\d+\s*,\s*\d+\s*;\s*\d+\s*\)\s*,?)*$', s): return None

	t = s.partition(':')
	degree = int(t[0].strip(), 10)
	s = t[2]

	edges = []

	for e in re.findall('\d+\s*,\s*\d+\s*;\s*\d+', s):
		args = []

		for n in re.findall('\d+', e):
			args.append(int(n, 10))

		edges.append(Edge(*args))

	return Grid(degree, edges)

class Grid:
	"""Represents an n-grid."""

	def __init__(self, degree, edges = []):
		"""Creates a new n-grid of the specified
		degree,and containing the specified edges."""

		self.degree = degree
		self.edges = edges

	def addEdge(self, edge):
		"""Adds the specified edge to this n-grid."""

		self.edges.append(edge)

	def hasEdge(self, v1, v2):
		for edge in self.edges:
			if (edge.v1 == v1 and edge.v2 == v2) or (edge.v2 == v1 and edge.v1 == v2):
				return True

		return False


class Edge:
	"""Represents a weighted graph edge."""

	def __init__(self, v1, v2, cost):
		self.v1 = v1
		self.v2 = v2
		self.cost = cost

def isAllowed(vertex, degrees):
    if(vertex < 0 or vertex > degrees*degrees):
        return False
    else:
        return True

def isConnected(grid):
    T = []
    Edges = copy.deepcopy(grid.edges)
    T.append(Edges[0].v1)
    T.append(Edges[0].v2)
    Edges.remove(Edges[0])
    t = 0
    while(t < len(T)):
        u = 0
        while (u < len(Edges)):
            if (len(Edges) > 0 and Edges[u].v1 == T[t]):
                    T.append(Edges[u].v2)
                    Edges.remove(Edges[u])
            if(0 < len(Edges) and Edges[u].v2 == T[t]):
                    T.append(Edges[u].v1)
                    Edges.remove(Edges[u])
            u = u + 1
        t = t + 1
    T = sorted(T)
    Nodes = []
    for i in range(1,len(T)):
        if (T[i] == T[i-1]):
            pass
        else:
            Nodes.append(T[i-1])
    if (len(Nodes) >= grid.degree):
        return True
    else:
        return False

# This grid check returns false if:
#   1. A node is connected to a node that is not allowed
#   2. A node is not attached to any other node
#   3. A node is connected to itself

def isGrid(grid):
    for i in range(0,len(grid.edges)):
        # Makes sure the nodes in the edge in question are allowed
        if(isAllowed(grid.edges[i].v1,grid.degree) and isAllowed(grid.edges[i].v2, grid.degree)):
            # If the difference between the nodes is 1 then they are adjacent to one another
            if(abs(grid.edges[i].v1 - grid.edges[i].v2) == 1):
                pass
            #
            elif(abs(grid.edges[i].v1 - grid.edges[i].v2) == grid.degree):
                pass
            else:
                return False
        #
        else:
           return False
    # If the algorithim makes it to this point then each edge is an allowable edge
    if (isConnected(grid)):
        return True
    else:
        return False

# Algorithim for sorting edges by cost
def insertSort(myGrid):
    for i in range(len(myGrid.edges)):
        for j in range(len(myGrid.edges)):
            if (myGrid.edges[i].cost < myGrid.edges[j].cost):
                temp = myGrid.edges[j]
                myGrid.edges[j] = myGrid.edges[i]
                myGrid.edges[i] = temp

def display(graph):
	for i in range(graph.degree):
		if i > 0:
			for j in range(graph.degree):
				if j > 0:
					stdout.write(' ')

				if graph.hasEdge(graph.degree * (i-1) + j + 1, graph.degree * i + j + 1):
					stdout.write('|')
				else:
					stdout.write(' ')

			print

		for j in range(graph.degree):
			if j > 0:
				if graph.hasEdge(graph.degree * i + j, graph.degree * i + j + 1):
					stdout.write('-')
				else:
					stdout.write(' ')

			stdout.write('*')

		print

def AuxiliaryArray(D,n):
    for i in range(n*n):
        D.append(i)

filename = "C:\Users\MPrime\Desktop\graph.txt"
print os.path.exists(filename)
grid = getGridFromFile(filename)
if(grid == None):
    print "No File"
else:
    display(grid)
    if(isGrid(grid)):
        D = []
        AuxiliaryArray(D,grid.degree)
        display(Kruskal(grid))
    else:
        print "Not a grid"
