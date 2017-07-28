# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to Problem 8.21 / Implementation of DFA minimization
## Ryan McIntyre
## 7/27/2017
## python 3.5.2

import sys

#recursive for equivalence; l is list of rows, split by commas
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

if __name__ == '__main__':
    if len(sys.argv)==2:
        minimize(sys.argv[1])
    else:
        print('minimize.py expected 1 additional arguement.',len(sys.argv)-1,'given.')