# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to problem 4.23
## Timothy Indrieri,Brandon Artner, Edward Morkunas
## 11/09/2016
## python 3

from ast import literal_eval


def findDistincts(result):

    # now we are to find the distinct finishing times.
    distinctTime = [] # list of distinct times
    distinctTime.append(result[0][1])
    for x in range(1, len(result)):
        if result[x][1] not in distinctTime:
            distinctTime.append(result[x][1])
    return distinctTime


def selection(result):
    H = largestFinishTimes(result)					#array of indices
    J = []
    A = [0 for x in range(len(result))]				# array that holds profits?
    distinctTime = [result[0][0]]
    distinctTime.extend(findDistincts(result))
    for j in range(len(distinctTime)):
        maxN = 0
        for i in range(len(result)):
            if distinctTime[j] == result[i][1]:
                if (result[i][2] + A[H[i]]) > maxN:
                    if maxN == 0:
                        J.append(i+1)
                    else:
                        J.pop()
                        J.append(i+1)
                    maxN = result[i][2] + A[H[i]]
        if A[j - 1] > maxN:
            maxN = A[j-1]
        A[j] = maxN
    return A[-1], J[:-1]


def largestFinishTimes(result):
    # finds indices of the largest distinct finish time no greater than the start time of activity i
    H = []
    for t in range(len(result)):
        H.append(0)
    for i in range(len(result)):
        for j in range(len(result)):
            if result[i][0] >= result[j][1]:
                H.insert(i,j+1)
                del(H[i+1])
    return H


result = []
with open('input.txt', 'r') as f:
    for line in f:
        result.extend(literal_eval(line.strip()))

#sort finish times in ascending order
result = sorted(result, key= lambda x: x[1] )
print(result)
print(selection(result))