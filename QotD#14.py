# CS1210: QotD14
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) it has not been shared with anyone outside the instructional team.
#
# Note: we are not asking for your password or your student ID number,
# just your login identifier: for example, mine is "segre".
#
def signed():
    return(["glflores"])

######################################################################
# Specification: rsum(S, min) takes a (possibly nested) sequence
# structure and returns the sum of the elements it contains that are
# greater than or equal to min.
#
# Example:
#   >>> rsum([1, (3,), 4, [5, 1, 4],(((4,)))])
#   22
#   >>> rsum([1, (3,), 4, [5, 1, 4],(((4,)))], 4)
#   17
#
#def rsum(S, min=0):
    #if (S == []) or (S == ()):
        #return 0
    #elif (not isinstance(S,list)) and (not isinstance(S,tuple)):
        #if (S>=min):
            #return S
        #else:
            #return 0
    #else:
        #return (rsum(S[0],min) + rsum(S[1:],min))

# my solution    
def rsum(S, min=0):
    if (S == []) or (S == ()):              # if len(S) == 0
        return 0
    elif isinstance(S,int):                 # I did not account for float values
        if (S>=min):
            return S
        else:
            return 0
    else:
        return (rsum(S[0],min) + rsum(S[1:],min))

# Corrections:


# Solution
def rsum(S, min=0):
    if len(S) == 0:                         # accounts for empty lists and tuples
        return 0
    elif type(S[0]) not in (int, float):    # accounts for ints and floats 
        return rsum(S[0]) + rsum(S[1:])
    elif S[0] >= min:                       # only keeping values > min                   
        return S[0] + rsum(S[1:])
    else:                                   # disregard 0th element 
        return rsum(S[1:])
# he structures it this way to avoid a nested if, it's more of a stylistic choice
# he also forgot to pass "min" to each recursive function


# Alternate Solution - more elegant
def rsum(S, min=0):
    if type(S) in (int, float):
        if S >= min:
            return S
        return 0
    return sum( [rsum(x, min) for x in S] )     # using a comprehension 


######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__':
    if type(signed()) is not list:
        print('### Error: Do not alter signed() other than to replace hawkid with your own.')
        exit()
    if signed()[0] == "hawkid":
        print('### Error: Replace the 6 characters in "hawkid" with your own hawkid in the signed() function.')
        exit()
    if rsum([1, (3,), 4, [5, 1, 4],(((4,)))], 4) != 17:
        print('### Error: rsum([1, (3,), 4, [5, 1, 4],(((4,)))], 4) != 17')
        exit()
    if rsum([1, (3,), 4, [5, 1, 4],(((4,)))], 4) != 17:
        print('### Error: rsum([1, (3,), 4, [5, 1, 4],(((4,)))], 4) != 17')
        exit()
    if rsum([[45, 28], [[11, 12], (13, (15,))]], 0) != 124:
        print('### Error: rsum([[45, 28], [[11, 12], (13, (15,))]], 0) != 124')
        exit()
    if rsum([[45, 28], [[11, 12], (13, (15,))]], 15) != 88:
        print('### Error: rsum([[45, 28], [[11, 12], (13, (15,))]], 15) != 88')
        exit()
    else:
        print('''\
### Your solution passes sample test cases.
### Doing so does not, however, guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
