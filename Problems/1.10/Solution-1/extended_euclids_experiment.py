# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Sample code for Problem 1.10
## Ryan McIntyre
## 5/25/2017
## python 3.5.2

from random import randint
import matplotlib.pyplot as plt

'''Below we have the definition contain in 'extended_euclids.py',
for reference during the experiment.

def ext_euc(m,n):
    
    #check pre-conditions
    if m<=0 or n<=0 or m!=int(m) or n!=int(n):
        raise ValueError("Invalid inputs for Euclid's.")
    
    #algorithm
    c = m
    d = n
    a = 0
    x = 1
    b = 1
    y = 0
    while(True):
        q = int(c/d)#int(float) rounds the float down
        r = c%d
        if r == 0:
            print(str(a)+'*'+str(m),'+',str(b)+'*'+str(n),'=',d,'= gcf('+str(d)+')')
            return (a,b)            
        c = d
        d = r
        h = x
        x = a
        a = h - q * a
        h = y
        y = b
        b = h - q * b'''
        
#---------------------------------------------------------------Experiment
        
def ext_euc_step_count(m,n):
    
    steps = 4 #4 checks above
    if m<=0 or n<=0 or m!=int(m) or n!=int(n):
        raise ValueError("Invalid inputs for Euclid's.")
        
    c = m
    d = n
    a = 0
    x = 1
    b = 1
    y = 0
    steps += 6 #6 assignments above
    while(True):
        q = int(c/d) 
        r = c%d
        steps += 4 
        #2 assignments above, r==0 check below, 1 divsion (treating c%d as a by-product of the division)
        if r == 0:
            return steps            
        c = d
        d = r
        h = x
        x = a
        a = h - q * a
        h = y
        y = b
        b = h - q * b
        steps += 12 #8 assignments, 2 multiplications, 2 subtractions above

'''
In order to count the number of "steps" in the algorithm above,
it is necessary to choose an embed a method of division. It seems
fitting to use the division defined in Algorithm 1.1. You'll see that
it has been inserted, along with the variable "steps", which serves as
a step counter.
'''

#algorithm, with division and step counter
def ext_euc_step_count_with_division(m,n):
    
    if m<=0 or n<=0 or m!=int(m) or n!=int(n):
        raise ValueError("Invalid inputs for Euclid's.")
    steps = 4 #4 checks above
    
    c = m
    d = n
    a = 0
    x = 1
    b = 1
    y = 0
    steps += 6 #6 assignments before loop
    while(True):
        q = 0
        r = c
        steps += 4 #2 assignments above, first d<=r and r==0 check below
        while d <= r:
            r -= d
            q += 1
            steps += 3 #2 assignments, next d<=r check
        if r == 0:
            return steps #we only care how many steps were made, in the end
        c = d
        d = r
        h = x
        x = a
        a = h - q * a
        h = y
        y = b
        b = h - q * b
        steps += 12 #8 assignments, 2 multiplications, 2 subtractions

'''
Next, we gather some data. We'll fix m's size, and vary n<m randomly.
'''

data = dict()
size = 1
sample_size = 1000000
while size < 50:
    sample = 0
    sample_total = 0
    while sample < sample_size:
        m = randint(2**(size-1),(2**size)-1)
        n = randint(1,m)
        sample_total += ext_euc_step_count_with_division(m,n)
        sample += 1
    data[size] = sample_total/sample_size
    size += 1

'''
Finally, we'll plot the data. Note that even with very large sample sizes,
there is a lot of variation. We've saved the results for sample size = 1000000
'''

#organize data
X = list(data)
Y = [data[x] for x in X]

#setup figure
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('size of larger input')
ax.set_ylabel('number of steps')
fig.suptitle('Complexity of Extended Euclid\'s')

#plot data
ax.plot(X,Y,'o')

fig.savefig('results_steps_with_division.png') #save figure, if uncommented