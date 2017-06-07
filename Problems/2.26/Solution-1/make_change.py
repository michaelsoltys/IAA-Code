# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Algorithm 2.4 / Problem 2.25 - Scheduling
## Ryan McIntyre
## 6/4/2017
## python 3.5.2

#n is a positive integer, in "cents" or least common divisor of currency
#change should be decreasing sequence of positive integers
def make_change(n,change):
    
    #well-formed...
    if any([c!=int(c) or c<1 for c in change]):
        raise ValueError('make_change accepts positive denominations only.')
    if n!=int(n) or n<1:
        raise ValueError('make_change accepts positive sum only.')
    change.sort(key = lambda x : x, reverse = True)
    
    #the algorithm
    L = dict([(c,0) for c in change])
    s = 0
    i = 0
    while s < n and i < len(change):
        x = change[i]
        while s + x <= n:
            L[x] += 1
            s += x
        i += 1
    
    #display
    l1 = 'Increment:  |'
    l2 = ' Quantity:  |'
    l3 = '   Amount:  |'
    lf = '          -- '
    for c in change:
        l1 += str(c).rjust(5).ljust(6) + '|'
        l2 += str(L[c]).rjust(5).ljust(6) + '|'
        l3 += str(c*L[c]).rjust(5).ljust(6) + '|'
        lf += '------ '
    l1 += '  Total'
    l2 += str(sum([L[c] for c in L])).rjust(6).ljust(7)
    l3 += str(s).rjust(6).ljust(7)
    lf += '--'
    l1 += '\n'
    l2 += '\n'
    l3 += '\n'
    lf += '\n'
    l1 += lf
    l2 += lf
    display = '\n'+lf+l1+l2+l3+lf
    if s!=n:
        display += 'Warning: '+str(s)+' is not '+str(n)+'.\n'
        display += 'Greedy approach didn\'t work,\n'
        display += 'or change increments don\'t span the natural numbers.'
    print(display)


#and we'll do a more robust main this time, for kicks
if __name__ == '__main__':
    
    change = []
    while True:
        try:
            change = [int(n.strip()) for n in 
            input('Input comma separated change increments: ').split(',')]
            break
        except:
            print('Invalid input.')
        if any([value<1 for value in change]):
            print('Invalid input; positive integers only.')
    
    while True:
        print('\n change =',str(change))
        print('Type "change" to enter new change increments.')
        print('Type "q" to quit.')
        inp = input('Or, enter a positive integer to make change: ')
        if inp in ['q','quit','"q"']:
            break
        elif inp in ['change','"change"']:
            while True:
                try:
                    change = [int(n.strip()) for n in 
                    input('Input comma separated change increments: ').split(',')]
                    break
                except:
                    print('Invalid input.')
                if any([value<1 for value in change]):
                    print('Invalid input; positive integers only.')
        else:
            try:
                make_change(int(inp),change)
            except:
                print('Invalid input.')