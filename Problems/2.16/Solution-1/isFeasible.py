# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 2.16 - Check schedule feasibility
## Ryan McIntyre
## 6/3/2017
## python 3.5.2

import sys

def isFeasible(input_text):
    
    [jobs,schedule] = [eval('['+s.strip()+']') for s in 
            ''.join(open(input_text,'r').readlines()).split(':')]
    deadline = dict()
    for i in range(len(jobs)):
        (d,p) = jobs[i]
        if type(d)!=int:
            #past deadlines just won't be scheduled, so negative deadline is fine
            raise ValueError('Deadline must be an integer.')
        deadline[i] = d
    I = set()
    T = set()
    for plan in schedule:
        (t,i) = plan
        if type(t)!=int or t<1:
            raise ValueError('Time must be a positive integer.')
        if type(i)!=int or i<0 or i>=len(jobs):
            raise ValueError('Invalid index.')
        if i in I:
            print('Job',i,'is scheduled more than once.')
            return False
        I.add(i)
        if t in T:
            print('Time',t,'is overbooked.')
            return False
        T.add(t)
        if deadline[i]<t:
            print('Job',i,'is scheduled after its deadline.')
            return False
    print('The schedule is feasible.')
    return True

if __name__ == '__main__':
    args = sys.argv
    if len(args)!=2:
        raise ValueError('Expected 1 input, got 2.')
    else:
        isFeasible(args[1])