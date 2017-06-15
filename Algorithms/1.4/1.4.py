# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Algorithm 1.4
## Ryan McIntyre
## 6/14/2017
## python 3.5.2

import sys


#requires integer inputs. if both are positive, computes product
#otherwise, computs aboslute product, and + or - is dependent only on 2nd input.
def alg(m,n):
    x = m
    y = n
    z = 0
    i = 0
    while x != 0:
        print('Iteration '+str(i).rjust(3)+' : x = '+str(x)+', y = '+str(y)+',',
              'and z = '+str(z))
        if x%2==1:
            z += y
        x = int(x/2)
        y *= 2
        i += 1
    print('\nInput: m =',m,'and n =',n,
          '\nOutput: z =',z)
    return z
    

if __name__ == '__main__':
    if len(sys.argv) == 3:
        m = sys.argv[1]
        n = sys.argv[2]
        try:
            m = int(m)
            n = int(n)
        except:
            print('Invalid inputs for 1.4.py')
        else:
            alg(m,n)
    else:
        print('1.4.py expected 2 additional arguements.',len(sys.argv)-1,'given.')