# CS1210: QotD13
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
# Building on QotD12, implement randInsert(L, r=1), a new shuffle
# routine that removes a randomly chosen element of L and reinserts
# it in a random location. This action is repeated r (default 1)
# times, to produce a scrambled list. 
#
# Example:
#   >>> L=list(range(10))
#   >>> L
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   >>> randInsert(L)
#   [0, 1, 2, 3, 5, 4, 6, 7, 8, 9]
#   >>> randInsert(L, 50)
#   [1, 2, 0, 3, 5, 4, 6, 7, 8, 9]
#   >>> randInsert(L, 50)
#   [8, 0, 9, 7, 2, 5, 6, 1, 3, 4]
#   >>> L
#   [8, 0, 9, 7, 2, 5, 6, 1, 3, 4]
#
# Note that your code should both destructively modify the input list,
# L, as well as return it. If you are creating new list structure your
# code is not correct. Note also that its quite possible to randomly
# choose to remove an element and then reinsert it exactly where it
# was before.
#
# Hint: you will likely need to use randint from random. Also, review
# your list methods.
#
# my solution - I'm pretty sure this works, it's just not very concise. 
import random
def randInsert(L, r=1):
    for i in range(r):
        x = random.randint(0,len(L)-1)
        y = random.randint(0,len(L)-1)
        L[x],L[y] = L[y],L[x]   
    return L
# This uses a simultaneous assignment, so I don't really have to worry about
# the length of L changing.
# Okay, I actually think this solution isn't correct. I'm switching elements
# instead of randomly deleting one and inserting it in a different spot. 


# Solution
from random import randint
def randInsert(L, r=1):
    for i in range(r):
        L.insert(randint(0, len(L)-2), L.pop(randint(0,len(L)-1)))
    return L
# L.pop(randint(0, len(L)-1)) removes and returns random element from L
    # Example: L goes from [0,1,2,3,4,5] to [0,1,3,4,5] (returns x=2)
# L.insert(randint(0, len(L-2), x) inserts x in random position (L is shorter)


# Can't we use x.pop() with open parenthesis? This would still be random?
# I will post this question to Piazza. 


# Solution - possible improvement
from random import randint
def randInsert(L, r=1):
    for i in range(r):
        L.insert(randint(0, len(L)-2), L.pop())
    return L



######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
if __name__ == '__main__':
    L=list(range(10))
    if type(signed()) is not list:
        print('### Error: Do not alter signed() other than to replace hawkid with your own.')
        exit()
    if signed()[0] == "hawkid":
        print('### Error: Replace the 6 characters in "hawkid" with your own hawkid in the signed() function.')
        exit()
    if randInsert(L) is None:
        print("### Error: your definition of randInsert() doesn't return a value.")
        exit()
    if set(randInsert(L, 100)) != set(range(10)):
        print("### Error: L is losing elements.")
    else:
        print('''\
### Your solution passes sample test cases.
### Doing so does not, however, guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
