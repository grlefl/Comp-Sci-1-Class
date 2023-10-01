 # CS1210: Lab9 [4 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partners, and
#  2) it has not been shared with anyone outside the instructional team.
# N.B., add a third string to the list if there are three of you.
#
# N.B., your hawkid is not the same as your student id number!
def signed():
    return(["glflores"])

######################################################################
# Specification: factorNext1(L) takes a list of integers and returns a
# new list containing all of the integers which were divisible by
# their predecessor.
#
# Hint: The first element has no predecessor, and so will never appear
# as part of the result.
#
# Your first solution, factorNext1() should use a comprehension.
#
# >>> factorNext1([1, 2, 4, 5, 16, 32, 2, 12])
# [2, 4, 32, 12]
# >>> factorNext1([5, 3, 2, 1])
# []
# >>> factorNext1([])
# []
# >>> factorNext1([3, 9, 18, 2, 6, 6])
# [9, 18, 6, 6]
#
# my solution:
def factorNext1(L):
    return [L[x] for x in range(1,len(L)) if L[x]%L[x-1]==0]
# good 

######################################################################
# Same specification, but use a non-comprehension iterative form of
# your choice.
#
# my 
def factorNext2(L):
    emptyList = []
    for x in range(1,len(L)):
        if (L[x]%L[x-1]==0):
            emptyList = emptyList + [L[x]] # or emptyList.append(L[i])
    return emptyList
# okay
# yeah, I can't really think of a cleaner way to do this

######################################################################
# Same specification, but use a recursive formulation.
#
# Hint: Think about what your base case should be first, e.g., returns
# an empty list.
#
# >>> factorNext3([1, 2, 4, 5, 16, 32, 2, 12])
# [2, 4, 32, 12]
#
# my solution 
def factorNext3(L):
    if (len(L)<=1):
        return []
    elif (len(L)==2):
        if (L[1]%L[0]==0):
            return [L[1]]
        return []
    else:
        return factorNext3(L[:2]) + factorNext3(L[1:])
# good

# Solution (yeah, this is way less complicated)
def factorNext3(L):
    if len(L) <= 1:
        return []
    elif L[1]%L[0] == 0:
        return [L[1]] + factorNext3(L[1:])
    else:
        return factorNext3(L[1:])

# Alternate Solution - where we descend into the recursion (with helper function)
def factorNext3c(L):
    def helper(L, R):
        if len(L) == 1:
            return R
        elif L[1]%L[0] == 0:
            return helper(L[1:], R + [L[1]]) # result is being built as we go, as opposed to
        else:                                   # being built at the very end as above 
            return helper(L[1:], R)
        return helper(L, [])

######################################################################
# Specification: perfect(n) returns True if n is a "perfect" number.
#
# A "perfect" number is a number whose proper divisors sum to the
# number itself. So 6 is perfect, because the proper divisors of 6
# (numbers that divide 6 evenly) are 1, 2 and 3, and 1+2+3=6.
#
# >>> [ i for i in range(1, 1000) if perfect(i) ]
# [6, 28, 496]
#
def perfect(n):
    totalSum = 0
    for x in range(1,n):
        if (n%x==0):
            totalSum = totalSum + x
    return totalSum==n
# okay, but is there a cleaner solution (comprehension)?
# Actually, I probably wouldn't use a comprehension because
# I'm not creating a new structure.

# Solution
def perfect(n):
    return n==sum([i for i in range(1,n) if n%i==0])

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
###################################################################### 
if __name__ == '__main__':
    if all([ "hawkid" in x for x in signed() ]):
        print('### Warning: Complete definition of signed() or no points will be awarded!')
    if factorNext1([1, 2, 4, 5, 16, 32, 2, 12]) != [2, 4, 32, 12]:
        print('### Error: factorNext1([1, 2, 4, 5, 16, 32, 2, 12]) != [2, 4, 32, 12]')
    if factorNext1([5, 3, 1, 2]) != [2]:
        print('### Error: factorNext1([5, 3, 1, 2]) != [2]')
    if factorNext1([2]) != []:
        print('### Error: factorNext1([2]) != []')
    if factorNext2([1, 2, 4, 5, 16, 32, 2, 12]) != [2, 4, 32, 12]:
        print('### Error: factorNext2([1, 2, 4, 5, 16, 32, 2, 12]) != [2, 4, 32, 12]')
    if factorNext2([5, 3, 1, 2]) != [2]:
        print('### Error: factorNext2([5, 3, 1, 2]) != [2]')
    if factorNext2([2]) != []:
        print('### Error: factorNext2([2]) != []')
    if factorNext3([1, 2, 4, 5, 16, 32, 2, 12]) != [2, 4, 32, 12]:
        print('### Error: factorNext3([1, 2, 4, 5, 16, 32, 2, 12]) != [2, 4, 32, 12]')
    if factorNext3([5, 3, 1, 2]) != [2]:
        print('### Error: factorNext3([5, 3, 1, 2]) != [2]')
    if factorNext3([2]) != []:
        print('### Error: factorNext3([2]) != []')
    if [ i for i in range(1, 1000) if perfect(i) ] != [6, 28, 496]:
        print('### Error: [ i for i in range(1, 1000) if perfect(i) ] != [6, 28, 496]')
    print('### Absence of errors does not guarantee correctness over all possible inputs.')
    print('### Check your work carefully against the specification before submitting to ICON.')
