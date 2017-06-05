# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Algorithm 2.3 / Problem 2.17 - Scheduling
## Ryan McIntyre
## 6/3/2017
## python 3.5.2

import sys

def scheduling(input_text):
    
    #check that input is well-formed, organize
    jobs = eval('['+''.join(open(input_text,'r').readlines())+']')
    profit = dict()
    D = -float('inf')#last deadline
    for i in range(len(jobs)):
        (d,p) = jobs[i]
        if type(d)!=int:
            raise ValueError('Deadline must be an integer.')
        if d > D:
            D = d
        if p<0:
            raise ValueError('Profit cannot be negative.')
        profit[i] = p
        jobs[i] = (d,p,i)#for reference after sorting
        
    #the algorithm
    jobs.sort(key = lambda x : x[1], reverse=True)
    Schedule = dict([(t,-1) for t in range(1,D+1)])
    Profit = 0
    for i in range(len(jobs)):
        (d,p,j) = jobs[i]
        while d > 0:
            if Schedule[d] == -1:
                Schedule[d] = j
                Profit += p
                break
            d -= 1
    
    #display
    l1 = 'Time:   |'
    l2 = 'Job:    |'
    l3 = 'Profit: |'
    lf = '         '
    for t in range(1,D+1):
        l1 += str(t).rjust(5) + ' |'
        lf += '------ '
        if Schedule[t] == -1:
            l2 += ' none |'
            l3 += '    0 |'
        else:
            j = Schedule[t]
            p = profit[j]
            l2 += str(j).rjust(5) + ' |'
            l3 += str(p).rjust(5) + ' |'
    l1 += ' Total'
    l3 += str(Profit).rjust(6)
    display = l1 + '\n' + lf + '\n' + l2 + '\n' + lf + '\n' + l3
    print(display)
    return [(t,Schedule[t]) for t in range(1,D+1)]
    
if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        raise ValueError('Scheduling expected 1 input, got 0 or >1.')
    scheduling(args[1])