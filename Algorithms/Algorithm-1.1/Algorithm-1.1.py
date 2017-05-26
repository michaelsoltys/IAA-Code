# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Implementation of Algorithm 1.1
## Ryan McIntyre
## 5/25/2017
## python 3.5.2

def div(x,y):
    
    #check pre-condition
    if x<0 or y<=0 or x!=int(x) or y!=int(y):
        raise ValueError('Invalid inputs for division.')
    
    #division algorithm
    q = 0
    r = x
    while y <= r:
        r -= y
        q += 1
    return (q,r)
    
