# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to Problem 9.12 - Infix, Prefix, Postfix
## Ryan McIntyre
## 7/8/2017
## python 3.5.2

import sys

#assume inputs are given as lists
def get_inf(pref,postf):
    top = pref[:1]
    left = []
    right = []
    p1 = pref.index(postf[-2])
    p2 = postf.index(pref[1])+1
    left_pref = pref[1:p1]
    left_postf = postf[0:p2]
    if left_pref == left_postf:
        left += left_pref
    else:
        left += get_inf(left_pref,left_postf)
    right_pref = pref[p1:]
    right_postf = postf[p2:-1]
    if right_pref == right_postf:
        right += right_postf
    else:
        right += get_inf(right_pref,right_postf)
    return left+top+right

def get_pref(inf,postf):
    if inf:
        top = postf[-1]
        p = inf.index(top)
        left_inf = inf[:p]
        left_postf = postf[:p]
        left = get_pref(left_inf,left_postf)
        right_inf = inf[p+1:]
        right_postf = postf[p:-1]
        right = get_pref(right_inf,right_postf)
        return [top]+left+right
    else:
        return []

def get_postf(inf,pref):
    if inf:
        top = pref[0]
        p = inf.index(top)
        left_inf = inf[:p]
        left_pref = pref[1:p+1]
        left = get_postf(left_inf,left_pref)
        right_inf = inf[p+1:]
        right_pref = pref[p+1:]
        right = get_postf(right_inf,right_pref)
        return left+right+[top]
    else:
        return []


if __name__ == '__main__':
    if len(sys.argv) == 2:
        file = open(sys.argv[1],'r')
        lines = file.readlines()
        file.close()
        if len(lines) == 2:
            good = ['prefix','infix','postfix']
            args = [line.split(':') for line in lines]
            a = dict()
            for arg in args:
                cl = arg[0].replace(' ','')
                if cl in good:
                    desc = arg[1].replace('\n','').replace(' ','').split(',')
                    a[cl] = desc
            if len(a) == 2:
                if 'prefix' in a and 'postfix' in a:
                    print('The infix is :',','.join(get_inf(a['prefix'],a['postfix'])))
                elif 'prefix' in a:
                    print('The postfix is :',','.join(get_postf(a['infix'],a['prefix'])))
                else:
                    print('The prefix is :',','.join(get_pref(a['infix'],a['postfix'])))
            else:
                print('Invalid input.')
            
        else:
            print('Input should be text with 2 lines, defining 2',
                  'of "infix", "prefix" and "postfix".')
    else:
        print('fix.py expected 1 additional input.',len(sys.argv)-1,'given.')