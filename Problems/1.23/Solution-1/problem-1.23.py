#Author: Chris Kuske
#COMP 545
#Assignment 1
#2/16/2015
#This is an implementation of the Gale-Shapley algorithm
#aka the 'Stable Marriage'

import sys

class AGirl():
    def __init__(self,girlName,preferences):
        self.name = girlName
        self.preferences = preferences #a list of the boys she would like to marry, in preferred order
        self.spouse = None
        self.ranking = {}
        for rank in range(len(preferences)): #initialize the girls suitor preferences
            self.ranking[preferences[rank]] = rank

class ABoy():
    def __init__(self,name,preferences):
        self.name = name #the boys name
        self.preferences = preferences #a list of the girls he would like to marry, in preferred order
        self.spouse = None #no spouse to start
        self.candidatePos = 0                   # next Girl in the list we can propose to in preferences
    def GetNextProposal(self):
        nextGirl = self.preferences[self.candidatePos] #who the Boy should propose to next
        self.candidatePos += 1
        return nextGirl

def LoadSimData(fName):
    peopleSet = []
    fStream = file(fName)
    boys = sum(1 for line in open(fName)) / 2
    j = 0
    k = 0
    for personData in fStream:
        name = "b" + str(j + 1)
        if j >= boys:
            name = "g" + str(k + 1)
            k += 1
        if name:
            preferences = personData.strip().split('<')
            for i in range(len(preferences)):
                preferences[i] = preferences[i].strip()
            peopleSet.append((name.strip(),preferences))
        j += 1
    fStream.close()
    return peopleSet
 
#algorithm implementation
def runAlgo():
    people = LoadSimData(sys.argv[1])#load data into the 'people' list
    boysList = people[0:(len(people) / 2)]#boys are the first half of the file
    boys = dict()
    for boy in boysList:
        boys[boy[0]] = ABoy(boy[0],boy[1]) #name, and preferences
    suitors = sorted(boys.keys())
        
    girlsList = people[len(people) / 2:]#girls are the second half of the file
    girls = dict()
    for girl in girlsList:
        girls[girl[0]] = AGirl(girl[0],girl[1]) #name then suitor preferences

    iterations = 1
    while len(suitors) > 0:
        
        print "Iteration #", iterations
        boy = boys[suitors[0]]  # pick the first suitor (Stage 1) (b*)
        girl = girls[boy.GetNextProposal()]      # identify highest-rank woman to which the current boy has not yet
                                              # proposed
        print boy.name, 'proposed to', girl.name

        if girl.spouse is None or (girl.ranking[boy.name] < girl.ranking[girl.spouse]): #girl accepts proposal from b* as long as she is either not engaged or prefers
                                                                                        #b* to her current partner
            print ' ', girl.name, 'accepts the proposal from',boy.name #M(s+1) = M union (b*,g)
                
            if girl.spouse: # previous spouse is getting dumped
                boys[girl.spouse].spouse = None #M = M - (b,g) union (b*,g)
                suitors.append(boys[girl.spouse].name) #add this boy back to the suitors
                print girl.name, 'traded up'
            suitors.remove(boy.name) #now that a pair is made, remove the boy from the list of suitors
            girl.spouse = boy.name #set the girls agreed upon suitor
            boy.spouse = girl.name #set the girl that accepted the proposal
        else:
            print '\t', girl.name, 'does not want to become engaged to', boy.name.strip(),',she prefers',girl.spouse
        iterations += 1

        print "Potential Marriages:"
        for boy in sorted(boys.keys()):
            print boys[boy].name.strip() + '-' + str(boys[boy].spouse).strip()
        print #newline

    #all suitors have had successful proposals, print the results
    print "'Stable' Marriages after", iterations, "iterations:"
    for boy in sorted(boys.keys()):
        print boys[boy].name + '-' + boys[boy].spouse

#run the code
runAlgo()