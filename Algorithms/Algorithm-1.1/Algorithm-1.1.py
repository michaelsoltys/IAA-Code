# -*- coding: utf-8 -*-
"""
@author: Ryan McIntyre
"""

def div(x,y):
    
    #check pre-condition
    if x<0 or y<=0 or x!=int(x) or y!=int(y):
        print('invalid input')
        return None
    
    #division algorithm
    q = 0
    r = x
    while y <= r:
        r -= y
        q += 1
    return (q,r)