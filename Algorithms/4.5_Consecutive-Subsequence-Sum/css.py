# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Algorithm 4.5 - Consecutive subsequence sum
## Ryan McIntyre
## 6/17/2017
## python 3.5.2

import sys

def css(R):
    M = [R[0]]
    for j in range(1,len(R)):
        if M[j-1] > 0:
            M.append(M[j-1]+R[j])
        else:
            M.append(R[j])
    s = max(M)
    i = M.index(s)
    ss = []
    while R[i]!=M[i]:
        ss = [R[i]] + ss
        i -= 1
    ss = [R[i]] + ss
    return (s,ss)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        arg1 = ''.join(sys.argv[1:])
        try:
            file = open(arg1,'r')
            args = file.read().replace('\n','')
            file.close()
        except FileNotFoundError:
            args = arg1
        try:
            args = [arg.replace(' ','') for arg in args.split(',')]
            args = [eval(arg) for arg in args if arg]
            args = [arg for arg in args if arg<=float('inf')]
        except:
            print('css.py expected a sequence of real numbers, separated by commas.')
        else:
            (s,ss) = css(args)
            print('The largest sum,',str(s)+',','results from subsequence:\n  ',ss)
    else:
        print('css.py expected an additional input.')