# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 4.4 / Algorithm 4.1 - Longest Subsequence
## Ryan McIntyre
## 6/11/2017
## python 3.5.2


'''First we implement algorithm 4.1. Note that the second condition in the
"if" statement can be changed to solve many different problems.'''
def r(seq, s):
    R = dict()
    d = len(seq)
    R[0] = 1
    for j in range(d):
        m = 0
        for i in range(j):
            if R[i]>m and abs(seq[i]-seq[j])<=s:
                m = R[i]
        R[j] = m+1
    return R

#Next we create the utility for reconstructing the sequence from R
def get_subsequence(seq,s):
    R = r(seq,s)
    index = list(R)
    index.sort(key = lambda x : R[x], reverse=True)
    j = index[0]
    aj = seq[j]
    out = [aj]
    I = 1
    while R[j]>1:
        i = index[I]
        if R[i] == R[j]-1 and abs(seq[i]-seq[j])<=s:
            j = i
            aj = seq[j]
            out = [aj]+out
        I += 1
    return out
    

if __name__ == '__main__':
    g = True
    while True:
        inp = input('Enter a space-separated sequence:\n... ')
        args = [arg.replace(' ','') for arg in inp.split(' ') if arg]
        if len(args) == 0:
            print('\nSequence with cardinaltiy of at least 2 required.\n')
        elif len(args) == 1 and args[0] in ['q','Q','quit','Quit','QUIT']:
            g = False
            break
        elif len(args) >= 2:
            try:
                args = [eval(arg) for arg in args]
            finally: 
                c = True
                for i in range(len(args)-1):
                    try:
                        args[i] - args[i+1]
                    except TypeError: 
                        print('\nNo natural difference between ',args[i],'and',args[i+1],'.\n')
                        c = False
                        break
            if c:
                break
        else:
            print('\nSequence with cardinaltiy of at least 2 required.\n')
    if g:
        while True:
            inp = input('Enter a max absolute difference:\n... ')
            if inp in ['q','Q','quit','Quit','QUIT']:
                break
            else:
                try:
                    arg = eval(inp)
                except:
                    print('\nInvalid input.')
                else:
                    try:
                        args[0]-args[1] <= arg
                    except:
                        print('\nComparison',args[0],'-',args[1],'<=',arg,'is undefined.\n')
                    else:
                        seq = get_subsequence(args,arg)
                        print('\nA longest subsequence meeting the conditions is:\n   ',
                              str(seq)[1:-1],'\n')
                        break