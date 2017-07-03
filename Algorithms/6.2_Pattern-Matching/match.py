# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Algorithm 6.2 - Pattern matching
## Ryan McIntyre
## 6/17/2017
## python 3.5.2


#import Rabin Miller from our awkwardly named directories
#please do not import like this in practice, see __init__.py docs
import numpy as np
import sys
import imp
with open('../6.3_Rabin-Miller/Rabin-Miller.py', 'rb') as f:
    rabin_miller = imp.load_module(
        'rabin_miller', f, 'Rabin-Miller.py',
        ('.py', 'rb', imp.PY_SOURCE)
    )

Ma = dict()
Ma['0'] = np.array([[1,0],[1,1]])
Ma['1'] = np.array([[1,1],[0,1]])
Mainv = dict()
Mainv['0'] = np.array([[1,0],[-1,1]])
Mainv['1'] = np.array([[1,-1],[0,1]])

def pattern_matching(x,y):
    n = len(x)
    m = len(y)
    mm = n*m*m+1
    p = 4
    while not rabin_miller.RabinMiller(p):
        p = np.random.randint(2,mm)
    A = M(x)
    B = M(y[:n])
    i = 0
    while n+i < m:
        if np.array_equal(A,B):
            if x == y[i:n+i]:
                return (True,i)
        B = np.dot(np.dot(Mainv[y[i]],B),Ma[y[n+i]])        
        i += 1
    if np.array_equal(A,B):
        if x == y[-n:]:
            return (True,i)
    return False
        
def M(s):
    result = np.array([[1,0],[0,1]])
    i = 0
    while i < len(s):
        result = np.dot(result,Ma[s[i]])
        i += 1
    return result
    
if __name__ == '__main__':
    if len(sys.argv) == 3:
        result = pattern_matching(sys.argv[1],sys.argv[2])
        if result:
            print('Matching substring found starting at index '+str(result[1])+'.')
        else:
            print('No matching substring found.')
    else:
        print('match.py expected 2 binary string inputs.',len(sys.argv)-1,'args given.')