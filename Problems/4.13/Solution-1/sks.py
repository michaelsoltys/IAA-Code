# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Problem 4.13 / Algorithm 4.3 - Simple Knapsack
## Ryan McIntyre
## 6/11/2017
## python 3.5.2

import sys

def sksWeightOnly(W,C):#weight array, cost
    S = [True] + [False for j in range(1,C+1)]
    for i in range(len(W)):
        for j in range(C,0,-1):
            if j>=W[i]:
                if S[j-W[i]]:
                    S[j] = True
    S = {i:S[i] for i in range(len(S))}
    m = max([j for j in S if S[j]])
    return m

def sks(W,C):#return max weight and corresponding w_i's used
    S = [True] + [False for j in range(1,C+1)]
    A = [[] for j in range(C+1)]
    for i in range(len(W)):
        for j in range(C,0,-1):
            if j>=W[i]:
                if S[j-W[i]]:
                    S[j] = True
                    A[j] = A[j-W[i]] + [W[i]]
    S = {j:S[j] for j in range(len(S))}
    m = max([j for j in S if S[j]])
    print(m,A[m])
    return (m,A[m])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        try:
            file = open(sys.argv[1],'r')
            args = file.read().replace('\n','').replace(' ','').split(',')
        except FileNotFoundError:
            args = sys.argv[1].replace(' ','').split(',')
        try:
            args = [int(arg) for arg in args]
        except:
            print('Inputs in',sys.argv[1],'cannot be cast as integers.')
        else:
            if args[0] > 0:
                C = args[0]
                W = args[1:]
                sks(W,C)
            else:
                print('Knapsack must have positive capacity.')
    else:
        print('sks.py expected 1 additional input.',len(sys.argv)-1,'given.')