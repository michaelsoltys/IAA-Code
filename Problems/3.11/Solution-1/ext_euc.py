# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 3.10 - Recursive Extended Euclid's
## Ryan McIntyre
## 6/10/2017
## python 3.5.2

import sys

def euc(m,n):
    if n==0:
        return(m,1,0)
    else:
        (d,x,y) = euc(n,m%n)
        return (d,y,x-int(m/n)*y)
#5 lines :)

#5 line main loop please? no? no :(
if __name__ == '__main__':
    if len(sys.argv) == 1:
        while True:
            inp = input('Enter two space-separated positive integers, or enter "q" to quit:\n... ')
            args = [arg.replace(' ','') for arg in inp.split(' ') if arg]
            if args[0] in ['q','quit','Quit','QUIT']:
                break
            if len(args) == 2:
                try:
                    m = eval(args[0])
                    n = eval(args[1])
                except:
                    print('\nInvalid input. Try positive integers.\n')
                else:
                    if m < n:
                        m,n = n,m
                    if m<=0 or n<0:
                        print('\nLarger input must be positive, smaller must be non-negative.\n')
                    elif m!=int(m) or n!=int(n):
                        print('\nInputs must be integers.')
                    else:
                        (d,x,y) = euc(int(m),int(n))
                        print(str(x)+'('+str(m)+') + '+str(y)+'('+str(n)+') = '
                                +str(d)+' = gcd('+str(m)+','+str(n)+')')
            else:
                print('Expected 2 arguements, got '+str(len(args))+'.' )
    elif len(sys.argv) == 3:
        try:
            m = eval(sys.argv[1])
            n = eval(sys.argv[2])
        except:
            print('\nInvalid input. Try positive integers.\n')
        else:
            if m < n:
                m,n = n,m
            if m<=0 or n<0:
                print('\nLarger input must be positive, smaller must be non-negative.\n')
            elif m!=int(m) or n!=int(n):
                print('\nInputs must be integers.')
            else:
                (d,x,y) = euc(int(m),int(n))
                print(str(x)+'('+str(m)+') + '+str(y)+'('+str(n)+') = '
                        +str(d)+' = gcd('+str(m)+','+str(n)+')')
    else:
        print('\nInvalid number of arguements for Euclid\'s.\n'
            + 'Enter two positive integers.' )