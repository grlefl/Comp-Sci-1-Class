# CS1210: QotD15
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
# Specification: overhand(L, r=1) is yet another shuffling algorithm,
# like scramble() and randInsert(). Inspired by the (physical)
# overhand shuffle, the algorithm repeatedly performs a three-segment
# reordering of the deck as follows. First, pick two indexes at
# random; call the lesser one i and the larger one j (note your code
# should also work for i==j). Exchange the first i elements of L with
# the last len(L)-j elements of L. So, for example, if the list is
# initially
#    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# and i=3, j=8, we would restructure the list as follows:
#    [0, 1, 2 | 3, 4, 5, 6, 7 | 8, 9]
# to yield
#    [8, 9, 3, 4, 5, 6, 7, 0, 1, 2]
# To shuffle perform this operation r (default 1) times.
#
# Example:
#   >>> L=list(range(10))
#   >>> L
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   >>> overhand(L)
#   [4, 5, 6, 7, 8, 9, 2, 3, 0, 1]
#   >>> overhand(L, 100)
#   [6, 2, 4, 9, 8, 0, 5, 1, 7, 3]
#
# Hint: Careful! The two sections you swap may not be the same
# length. To avoid going crazy, I'd avoid parallel assignment to start
# with, as it may not operate the way you might expect it to. This one
# is tricky!
#
from random import randint
def overhand(L, r=1):
    i = randint(0,len(L)-1)
    j = randint(i,len(L)-1)
    L = (L[i:]).append(L[:i])
    return 0

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
    if overhand(L) is None:
        print("### Error: your definition of overhand() doesn't return a value.")
        exit()
    if set(overhand(L, 100)) != set(range(10)):
        print("### Error: L is losing elements.")
    else:
        print('''\
### Your solution passes sample test cases.
### Doing so does not, however, guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
