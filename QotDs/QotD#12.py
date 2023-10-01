# CS1210: QotD12
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
# In QotD12 we're going to play a little with non-determinism, that
# is, writing code that incorporates some form of random
# behavior. Randomness, as we'll see shortly in lecture, can actually
# help you write better, more efficient, code -- but today we'll only
# start with some simple notions.
#
# Recall the solution to the scramble() function in HW1, which
# shuffles a list by swapping elements. It creates no new structure,
# but rather modifies the original existing list.
#
from random import randint
#
def scramble(L):
    for i in range(len(L)-1, 0, -1):
        j = randint(0, i)
        L[i], L[j] = L[j], L[i]  # swap elements i and j
    return(L)

# There are two things we would like to know about scramble() which
# become important considerations when presented with an alternative
# method for destructively (i.e., by modification) "scrambling" or
# "shuffling" a list. First, we'd like some measure of "how shuffled"
# the result is, on average, with respect to the input list. And
# second, we'd like to know that the algorithm is "fair," that is,
# that every permutation of the original list is equally likely.
#
# For this QotD, you will implement a function that measures how
# "sorted" the result of scramble is. The idea is simple: scan the
# resulting list and count the number of "inversions" in it. An
# "inversion" is a pair of elements in the list where L[i]<L[j] but
# i>j. The inversion index is the ratio of inversions over the number
# possible comparisons between two elements in the list (note that for
# a list L of length len(L), there are (len(L)*(len(L)-1))/2 unique
# combinations of i and j).
#
# Note that you will need to methodically compare every element L[i]
# with every other element L[j] in L, and count the number of
# inversions you observe. You can assume all elements of the list are
# unique, so there are no duplicate entries.
#



# Specification: L[i]<L[j] and i>j, OR L[i]>L[j] and i<j





def iindex(L):
    #my original solution 
    return (len([[i]+[j] for i in L for j in L[L.index(i):] if i!=j and L[i]<L[j] and i>j]))/((len(L)*(len(L)-1))/2)
        # I believe I had i<j but tested for L[i]<L[j]. The signs should be opposite. This solution
        # is also just generally wonky.
        # Also, this is giving an out of range error, so I don't even know why I submitted it in the first place. 

    #Solution
    inv = 0;
    for i in range(0, len(L)-1):
        for j in range(i+1, len(L)):
            if L[i] > L[j]: 
                inv = inv + 1
    return(2*inv/(len(L)*len(L)-1))

#Random Thoughts:
#so i has to come before j, and the value at i has to be greater than
#the value at j to have it count as an inversion
#On average, the inversion ration should be around 0.5 for it to be
#faily sorted. 

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
    if iindex(list(range(10))) is None:
        print("### Error: your definition of iindex() doesn't return a value.")
        exit()
    if iindex(list(range(10))) != 0:
        print("### Error: iindex(list(range(10)) != 0")
    if not (0 <= iindex(scramble(list(range(10)))) <= 1):
        print("### Error: iindex() should return a value between 0 and 1.")
    else:
        print('''\
### Your solution passes sample test cases.
### Doing so does not, however, guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
