# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Implementation of Algorithm 1.3
## Ryan McIntyre
## 5/25/2017
## python 3.5.2

def isPalindrome(x):
    n = len(x)
    i = 0
    while i < int(n/2):
        if x[i]!=x[n-i-1]:
            print('"',str(x),'" IS NOT a palindrome.')
            return False
        i += 1
    print('"',str(x),'" IS a palindrome.')
    return True

isPalindrome('racecar')
isPalindrome('cheese')
isPalindrome([1,2,3,4,1])
isPalindrome([1,2,3,2,1])