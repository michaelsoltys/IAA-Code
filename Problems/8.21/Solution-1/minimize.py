# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to Problem 8.21 / Implementation of DFA minimization
## Ryan McIntyre
## 7/27/2017
## python 3.5.2

import sys
from collections import deque

#------------------------------------Lazy (but more readable) Recursive Version

#recursive for equivalence; l is list of rows, split by commas, from input text
def iseq(a,b,l,d=0):#d is depth, limited to number of states
    A = l[a]
    B = l[b]
    if A[0] != B[0]:
        return False
    if A[1:]==B[1:]:
        return True
    if d > len(l):
        return True
    return iseq(int(A[1]),int(B[1]),l,d+1) and iseq(int(A[2]),int(B[2]),l,d+1)

#use above to split into sets defined by equivalence, etc
def minimize(input_text_name):
    file = open(input_text_name,'r')
    lines = [line.split(',') for line in file.readlines() if line]
    file.close()
    assignments = {i:set([i]) for i in range(len(lines))}
    extras = set()
    i = 0
    while i < len(lines)-1:
        if not i in extras:
            j = i+1
            while j < len(lines):
                if not j in extras:
                    if iseq(i,j,lines):
                        assignments[i].add(j)
                        assignments[j] = assignments[i]
                        extras.add(j)
                j += 1
        i += 1
    groups = list(set([frozenset(x) for x in assignments.values()]))
    new_lines = []
    i = 0
    while i < len(groups):
        line = []
        a = next(iter(groups[i]))
        (acc,zero,one) = lines[a]
        line.append(acc)
        line.append(groups.index(assignments[int(zero)]))
        line.append(groups.index(assignments[int(one)]))
        new_lines.append(line)
        i += 1
    ext = input_text_name.index('.')
    file = open('output_of_'+input_text_name[:ext]+'.txt','w')
    for line in new_lines:
        s = ','.join([str(x) for x in line])
        print('   '+s)
        file.write(s+'\n')
    file.close()
    
#----------------------------------------------------Better Stack-based Version
def dfa_min(input_text_name,output_text_name=''):
    file = open('input.txt','r')
    lines = [line.split(',') for line in file.readlines() if line]
    file.close()
    n = len(lines)
    f0 = {}
    f1 = {}
    r0 = {i:set() for i in range(n)}
    r1 = {i:set() for i in range(n)}
    table = {i:{j:'o' for j in range(i+1,n)} for i in range(n-1)}
    queue = deque()
    i = 0
    while i < n-1:
        a = int(lines[i][1])
        b = int(lines[i][2])
        f0[i] = a
        f1[i] = b
        r0[a].add(i)
        r1[b].add(i)
        j = i+1
        while j < n:
            if lines[i][0]!=lines[j][0]:
                queue.append((i,j))
                table[i][j] = 'x'
            j += 1
        i += 1
    a = int(lines[n-1][1])
    b = int(lines[n-1][2])
    f0[n-1] = a
    f1[n-1] = b
    r0[a].add(n-1)
    r1[b].add(n-1)
    done = set()
    while queue:
        i,j = queue.popleft()
        if not (i,j) in done:
            done.add((i,j))
            for c in r0[i]:
                for l in r0[j]:
                    k = c
                    if k > l:
                        k,l = l,k
                    if table[k][l] == 'o':
                        table[k][l] = 'x'
                        queue.append((k,l))
            for c in r1[i]:
                for l in r1[j]:
                    k = c
                    if k > l:
                        k,l = l,k
                    if table[k][l] == 'o':
                        table[k][l] = 'x'
                        queue.append((k,l))
    assignments = {}
    groups = []
    i = 0
    while i < n:
        if not i in assignments:
            group = {i}
            assignments[i] = group
            j = i+1
            while j < n:
                if table[i][j] == 'o':
                    assignments[j] = group
                    group.add(j)
                j += 1
            groups.append(group)
        i += 1
    new_lines = []
    i = 0
    while i < len(groups):
        nl = []
        j = next(iter(groups[i]))
        nl.append(lines[j][0])
        nl.append(groups.index(assignments[f0[j]]))
        nl.append(groups.index(assignments[f1[j]]))
        new_lines.append(','.join([str(x) for x in nl]))
        i += 1
    if output_text_name == '':
        ext = input_text_name.index('.')
        output_text_name = 'output_of_'+input_text_name[:ext]+'.txt'
    file = open(output_text_name,'w')
    for line in new_lines:
        file.write(line+'\n')
        print('   ',line)

#--------------------------------------------------------------------------Main

if __name__ == '__main__':
    if len(sys.argv)==2:
        dfa_min(sys.argv[1])
    elif len(sys.argv)==3:
        dfa_min(sys.argv[1],sys.argv[2])
    else:
        print('minimize.py expected 1-2 additional arguements.',len(sys.argv)-1,'given.')
