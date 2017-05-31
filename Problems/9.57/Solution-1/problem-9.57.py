# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to problem 9.57
## Andrew Trow
## 3/15/2015
## python 3

import sys
import csv

class TransitionState(object):
    def __init__(self, position, zero, one, accepting=False):
        self.position = position
        self.zero = zero
        self.one = one
        self.accepting = accepting
    def position(self):
        return self.position
    def zero(self):
        return self.zero    
    def one(self):
        return self.one
    def accepting(self):
        return self.accepting
    def __repr__(self):
        return "{}, {}, {}, {}".format(self.position, self.zero, self.one, self.accepting)
       
        
def readInputFile(inputFile):
    with open(inputFile, 'r') as transitionInputFile:
        print("Reading file: ", transitionInputFile.name)
        lines = transitionInputFile.readlines()
        
        stateTable = []
        for i in range(len(lines)):
            line = lines[i]
            acceptingState = False

            zeroState = -1
            oneState = -1
            
            for string in csv.reader(line, delimiter = " "):
                if len(string) == 1:                    
                    if string[0] == '*':
                        acceptingState = True
                    else:
                        if zeroState == -1:
                            zeroState = int(string[0])
                        else:
                            if oneState == -1:
                                oneState = int(string[0])
                
            stateTable.append(TransitionState(i, zeroState, oneState, acceptingState))                
                    
        for state in stateTable:
            print(state)
    return stateTable
        
def findGroupWithInputZero(state, stateGroups): 
    for group in stateGroups:
        for groupState in group:
            if groupState.position == state.zero:
                return group
    print("ERROR: could not find input zero group: ", state)
    return None
    
    
def findGroupWithInputOne(state, stateGroups):        
    for group in stateGroups:
        for groupState in group:
            if groupState.position == state.one:
                return group
    print("ERROR: could not find input zero group: ", state)
    return None

def minimizationDFA(stateTable):
    stateGroups = []
    tempGroup = []
    for state in stateTable:
        if state.accepting:
            tempGroup.append(state)
    stateGroups.append(tempGroup)
    
    tempGroup = []
    for state in stateTable:
        if not state.accepting:
            tempGroup.append(state)
    stateGroups.append(tempGroup)
    
    madeSplit = True
    while madeSplit:        
        madeSplit = False;         
        for group in stateGroups:
            tempGroups = []
            tempGroup = []
            previousZeroGroup = None
            previousOneGroup = None
            for state in group:
                zeroGroup = findGroupWithInputZero(state, stateGroups)
                oneGroup = findGroupWithInputOne(state, stateGroups)
                if previousZeroGroup is not None and previousZeroGroup is not zeroGroup or previousOneGroup is not None and previousOneGroup is not oneGroup:
                    addedStateToGroup = False
                    for partitionedGroup in tempGroups:
                        if addedStateToGroup:
                            break
                        for partitionedState in partitionedGroup:
                            partitionedZeroGroup = findGroupWithInputZero(partitionedState, stateGroups)
                            partitionedOneGroup = findGroupWithInputOne(partitionedState, stateGroups)
                            if zeroGroup is partitionedZeroGroup and oneGroup is partitionedOneGroup:
                                #print("partitionedGroup appended: ", state)
                                partitionedGroup.append(state)
                                addedStateToGroup = True
                                break
                    if not addedStateToGroup:  
                        #print("tempGroup appended: ", state)                     
                        tempGroup.append(state)
                        tempGroups.append(tempGroup)
                        tempGroup = []
                        
                    madeSplit = True
                else:
                    previousZeroGroup = zeroGroup
                    previousOneGroup = oneGroup
                
            if len(tempGroups) is not 0:
                for tempGroupToAdd in tempGroups:
                    for tempStateToRemove in tempGroupToAdd:
                        group.remove(tempStateToRemove)
                    #print("tempGroupToAdd: ", tempGroupToAdd)
                    stateGroups.append(tempGroupToAdd)
                    
    return stateGroups
        
stateTable = readInputFile(sys.argv[1])
stateGroups = minimizationDFA(stateTable)

print()
print("Found Minimal DFA with size: ",len(stateGroups))
print("Final Blocks")
for group in stateGroups:
    print(group)
