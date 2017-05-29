# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Algorithm 1.7 - Gale-Shapley
## Ryan McIntyre
## 5/27/2017
## python 3.5.2

import sys

def stable_marriage(input_text):    
    
    #read data, check that it's well-formed
    A = [] #proposing
    B = [] #accepting / declining
    file = open(input_text,'r')
    l = preference_list(eval(file.readline()))#see class def below
    n = len(l.list)
    if set(l.list)!=set(range(n)):
        raise TypeError('Invalid input for stable marriage.')
    A.append(l)
    i = 1
    while i < n:
        l = preference_list(eval(file.readline()))
        if set(l.list)!=set(range(n)):
            raise TypeError('Invalid input for stable marriage.')
        A.append(l)
        i += 1
    i = 0
    while i < n:
        l = preference_list(eval(file.readline()))
        if set(l.list)!=set(range(n)):
            raise TypeError('Invalid input for stable marriage.')
        B.append(l)
        i += 1
    file.close()
    
    #the algorithm
    bookmark = [0 for a in A]
    matchA = dict()
    matchB = dict()
    matchA[0] = A[0].get(0)
    matchB[matchA[0]] = matchA[0]
    bookmark[0] += 1
    i = 1
    while i < n:
        a = i
        while True:
            b = A[a].get(bookmark[a])#b will be proposed to
            bookmark[a] += 1
            if not b in matchB:#if b is not engaged...
                matchA[a] = b
                matchB[b] = a
                break
            else:
                a2 = matchB[b]
                #if a is better than current suitor
                if B[b].get_index(a) < B[b].get_index(a2):
                    matchA[a] = b
                    matchB[b] = a
                    matchA.pop(a2)
                    a = a2
        i += 1
    out = [(a,matchA[a]) for a in matchA]
    for pair in out:
        print('A'+str(pair[0])+' is matched with B'+str(pair[1])+'.')
    return out
    
    
class preference_list:
    
    def __init__(self,input_list):
        self.list = input_list
    
    def prefers(self,c1,c2):
        return(self.list.index(c1)<self.list.index(c2))
    
    def get(self,index):
        return self.list[index]

    def get_index(self,c):
        return self.list.index(c)
        
if __name__ == '__main__':
    if len(sys.argv) > 2:
        raise TypeError('Too many inputs for Stable Marriage.')
    elif len(sys.argv) < 2:
        raise TypeError('Stable Marriage requires an input file.')
    else:
        stable_marriage(sys.argv[1])