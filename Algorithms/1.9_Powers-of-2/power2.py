# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 1.9 - Powers of 2
## Ryan McIntyre
## 6/14/2017
## python 3.5.2

import sys

def power2(n):
    
    #check precondition
    try:
        if n!=int(n) or n<1:
            print(n,'is an invalid input')
            return None
        else:
            n = int(n)
    except:
        print(n,'is an invalid input')
        return None
    
    #the algorithm
    else:
        x = n
        while x > 1:
            if x%2==0:
                x = int(x/2)
            else:
                print(n,'IS NOT a power of 2.')
                return False
        print(n,'IS a power of 2.')
        return True


if __name__ == '__main__':
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            try:
                power2(int(arg))
            except:
                print(arg,'is an invalid input.')
    else:
        print('power2.py expected at least one additional input.')