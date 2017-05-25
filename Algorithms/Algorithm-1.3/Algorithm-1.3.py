# -*- coding: utf-8 -*-
"""
@author: Ryan McIntyre
"""

def isPalindrome(x):
    n = len(x)
    i = 0
    while i < int(n/2):
        if x[i]!=x[n-i-1]:
            return False
        i += 1
    return True

print(isPalindrome('racecar'))
print(isPalindrome('cheese'))