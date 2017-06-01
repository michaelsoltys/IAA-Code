# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Algorithm 1.6 - Ulam's
## Ryan McIntyre
## 5/26/2017
## python 3.5.2

import sys

def ulam(a,limit=20,display=True):
    
    #check pre-conditions
    if a!=int(a) or a<=0:
        raise ValueError('Input',a,'is not a natural number.')
    
    #get first 3 values
    x = ulist([int(a)])#see class definition below
    i = 0 #iteration counter
    while x.get(-1)!=4:
        x.get_next()
        i += 1
    x.get_next()
    x.get_next()
    i += 2
    #once the last is 4, the next two will be 2, 1.
    if display:
        print('Iterations for',str(a)+':',i)
    if i<=limit and display:
        print('Sequence for',str(a)+':',x.list)
    return i#we don't necessarily need any return, but why not
    

class ulist:
    
    def __init__(self,input_list):
        self.list = input_list

    def get_next(self):
        x = self.list[-1]
        if x%2==0: #"if x is even"
            self.list.append(int(x/2))
        else:
            self.list.append(3*x+1)
    
    def get(self,i):
        return self.list[i]

if __name__ == '__main__':
    if len(sys.argv) > 2:
        if sys.argv[-1][:6] == 'limit=':
            limit = int(sys.argv[-1][6:])
            for arg in sys.argv[1:-1]:
                ulam(int(arg),limit)
        else:
            for arg in sys.argv[1:]:
                ulam(int(arg))
    elif len(sys.argv) == 2:
        ulam(int(sys.argv[1]))
    else:
        raise TypeError('Ulam\'s requires an integer input.')