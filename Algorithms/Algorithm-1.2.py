# -*- coding: utf-8 -*-
"""
@author: Ryan McIntyre
"""

def euc(a,b):
    
    #check pre-condition
    if a<=0 or b<=0 or a!=int(a) or b!=int(b):
        raise ValueError("Invalid inputs for Euclid's.")
        
    #Euclid's algorithm
    m = int(a)
    n = int(b)
    r = m%n #python for rem(m,n)
    while r>0:
        m = n
        n = r
        r = m%n
    return n