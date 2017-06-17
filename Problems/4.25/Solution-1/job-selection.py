# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 4.25 - Job Selection
## Ryan McIntyre
## 6/11/2017
## python 3.5.2

from copy import copy
import sys

def js(jobs):
    J = copy(jobs)
    J.sort(key = lambda x : x[1])
    tmax = J[-1][1]
    A = [0 for t in range(tmax+1)]
    B = [[] for t in range(tmax+1)]
    for i in range(len(J)):
        ti = J[i][1]
        di = J[i][0]
        for t in range(tmax,-1,-1):
            tmin = min(t,ti)
            if tmin >= di:
                pi = J[i][2]
                a = A[t]
                b = pi + A[tmin-di]
                if a < b:
                    A[t] = b
                    B[t] = B[t-di] + [i]
    A = A[tmax]
    B = [J[i] for i in B[tmax]]
    return(A,B)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            file = open(sys.argv[1],'r')
            inp = file.read().replace('\n','').replace(' ','')
            file.close()
        except FileNotFoundError:
            print('File',sys.argv[1],'not found.')
        else:
            args = []
            k = 0
            i = 0
            while i+1 < len(inp):
                if inp[i-1:i+2] == '),(':
                   args.append(inp[k:i])
                   k = i+1
                i += 1
            args.append(inp[k:])
            args = [arg for arg in args if arg]
            try:
                args = [eval(arg) for arg in args]
            except:
                print('Invalid or improperly formatted input.')
            else:
                if all([len(arg) == 3 for arg in args]):
                    try:
                        if all([all([x == int(x) and x > 0 for x in arg]) for arg in args]):
                            (A,B) = js(args)
                            print('Max profit,',str(A)+',','is reached with jobs in:',
                                  '\n  ',B)
                        else:
                            print('All input should be positive integers.')
                    except:
                        print('All input should be positive integers.')
                else:
                    print('All jobs should be tuples with 3 positive integers.')
    else:
        print('job-selection.py expected an additional input.')