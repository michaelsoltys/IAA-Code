# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 9.6 - Matrix generation of Fibonacci numbers
## Ryan McIntyre
## 7/7/2017
## python 3.5.2

import numpy as np
import sys

core = np.array([[1,1],[1,0]])

#numpy is a very nice library, so this only takes 3 lines!
def fib(n):#return the nth fibonacci number
    if n in [0,1]: return n
    return np.linalg.matrix_power(core,n-1)[0][0]


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('fib.py expected at least 1 additional input.')
    else:
        args = sys.argv[1:]
        try:
            args = [int(arg) for arg in args]
        except:
            print('All fib.py inputs should be non-negative integers.')
        else:
            if all([arg>=0 for arg in args]):
                for arg in args:
                    print(('f('+str(arg)+')').rjust(10),':',fib(arg))
            else:
                print('All fib.py inputs should be non-negative integers.')