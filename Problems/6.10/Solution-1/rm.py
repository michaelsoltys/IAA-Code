# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Implementation of Algorithm 6.3 - Rabin-Miller
## Ryan McIntyre
## 7/2/2016
## python 3.5.2

import binary
from random import choice
import sys

'''For this version of Rabin-Miller, we've defined our own binary string
operations. Note that it is actually much slower than the "naive" version;
I'd assume that the writer(s) of Python's integer operations were pretty
smart people. Moreover, our "source of randomness" relies on ints, so they
both go out of bounds simultaneously. However, the naive version does output
false negatives with the message "the impossible has happened" for primes
small enough to be ints, but large enough to cause issues with exponentiation.
This version avoids this issue.'''

#assuming n is a positive integer encoded as a binary string
def isPrime(n,iter_count=20,display=False):
    n = n.lstrip('0')
    if n:
        if n == '10':
            return True
        elif binary.mod(n,'10') == '0':
            return False
        else:
            
            i = 0
            while i < iter_count:
                if not rm_core(n):
                    if display:
                        print(n,'is NOT prime.')
                    return False
                i += 1
            if display:
                print(n,'IS prime.')
            return True
    else:
        return False

def rm_core(n):
    a = format(choice(range(2,int(n,2))),'b') #hail the magic conch!
    s = binary.sub_two(n,'1')
    S = list(s)
    if binary.exp(a,s,n) != '1':
        return False
    h = '0'
    while S[-1] == '0':
        S.pop()
        h = binary.add_two(h,'1')
    s = ''.join(S)
    a = binary.exp(a,s,n)
    if a == '1' or a == binary.sub_two(n,'1'):
        return True
    i = '0'
    while binary.ge(h,i):
        a = binary.mod(binary.multiply(a,a),n)
        if a == binary.sub_two(n,'1'):
            return True
        elif a == '1':
            return False
        i = binary.add_two(i,'1')
    print('Party like it\'s 1999!')
    return False

if __name__ == '__main__':
    if len(sys.argv) == 2:
        isPrime(sys.argv[1],display=True)
    else:
        print('rm.py expected 1 additional arguement.',len(sys.argv)-1,'given.')