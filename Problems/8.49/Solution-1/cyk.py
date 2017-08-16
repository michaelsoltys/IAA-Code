# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to Problem 8.49 / Implementation of the CYK algorithm
## Ryan McIntyre
## 8/15/2017
## python 3.5.2

from collections import deque
from itertools import permutations as perm #don't worry, only permuting 2
import sys


#---------------------------------------------------------------------------CFG
# metasymbols :;,| and \n should not be used in variables or terminals
# variables and terminals can have multiple characters, but should not be proper initial segments
# TODO, add support for user-chosen metasymbols
class CFG:
    
    # assumes input is well-formatted, and only checks for use of unassigned variables and terminals
    def __init__(self,V='',T='',P='',S='',filename=''):
        
        self.var = None
        self.term = None
        self.prod = None
        self.st = None
        
        # if inputs are supplied in V,T,P,S:
        if all([V,T,P,S]):
            self.setup(V,T,P,S)
        
        # if input is in the form of a filename
        elif filename:
            self.load_file(filename)
            
    def setup(self,V,T,P,S):
        
        # V is a string with variables as substrings separated by commas
        # spaces are ignored
        self.var = set([x.replace(' ','') for x in V.split(',') if x])
        
        # T is like V for terminals...
        self.term = set([x.replace(' ','') for x in T.split(',') if x])
        for t in self.term:
            if t in self.var:
                raise AttributeError('Terminals cannot be variables.')
        
        # P is comma separated list of terms like X:a|XY|aXa
        # i.e. X "to" a "and" XY "and" aXa, meaning X-->a, X-->XY,...
        self.prod = {y[0]:set(y[1].split('|')) for y in [x.split(':') for x in P.split(',')]}
        
        # check correctness of productions...
        if not all([p in self.var for p in self.prod]):
            raise AttributeError('A production cannot begin with a non-variable.')
        m = max(len(x) for x in set.union(self.var,self.term))
        for p in self.prod.values():
            for q in p:
                q = deque(q)
                sub = ''
                while q:
                    sub += q.popleft()
                    if sub in self.var or sub in self.term:
                        sub = ''
                    if len(sub) > m:
                        raise AttributeError('Unidentified term or variable beginning with "'+sub[:10]+'".')
                if not sub == '':
                    raise AttributeError('Unidentified term or variable beginning with "'+sub[:10]+'".')
        
        # S is the start variable...
        self.st = S
        if not self.st in self.var:
            raise AttributeError('The start variable must be a variable.')
    
    def load_file(self,filename):
        
        file = open(filename,'r')
        (V,T,P,S) = file.read().replace('\n','').split(';')
        file.close()
        self.setup(V,T,P,S)
    
    def display(self):
        print('  ','Variables'.ljust(12),':',','.join(self.var))
        print('  ','Terminals'.ljust(12),':',','.join(self.term))
        print('  ','Productions'.ljust(12),':')
        for p in self.prod:
            ex = ''
            if '' in self.prod[p]:
                ex = '\u03B5|'
            print(''.rjust(15),p.rjust(3),'-->',ex+'|'.join(self.prod[p]-{''}))
        print('  ','Start'.ljust(12),':',self.st)
    
    #check if in CNF
    def isCNF(self):
        pp = set([''.join(x) for x in perm(self.var,2)])
        for p in self.prod.values():
            for q in p:
                if not q in self.term and not q in pp:
                    return False
                if q == '':
                    return False
        return True


#---------------------------------------------------------------------------CYK
def cyk(cfg,w):
    n = len(w)
    assignments = {(i,j):set() for i in range(n) for j in range(i,n)}
    for i in range(n):
        for p in cfg.prod:
            if w[i] in cfg.prod[p]:
                assignments[(i,i)].add(p)
    d = 1 # d = j-i; i.e. d determines which diagonal we're on
    while d < n:
        for i in range(n-d):
            j = i+d
            for k in range(i,j):
                for Xp in assignments[(i,k)]:
                    for Xq in assignments[(k+1,j)]:
                        c = Xp+Xq # this triple nested loop could probably be
                        for p in cfg.prod: # replaced with a better alternative
                            if c in cfg.prod[p]:
                                assignments[(i,j)].add(p)
        d += 1
    if cfg.st in assignments[(0,n-1)]:
        return True
    return False


#--------------------------------------------------------------------------Main
# python cyk.py cfg.txt 'input_string'
if __name__ == '__main__':
    if len(sys.argv) == 3:
        x = CFG(filename=sys.argv[1])
        if x.isCNF():
            print(cyk(x,sys.argv[2]))
        else:
            print('CFG input is not in CNF.')
    else:
        raise ValueError('cyk.py expected 2 additional inputs.',len(sys.argv)-1,'given.')