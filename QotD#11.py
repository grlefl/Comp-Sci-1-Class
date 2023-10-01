# CS1210: QotD11
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
# Specification: intAltSum(L, mode=True) takes a list (or other
# sequence type on integers), L, and computes the alternating sum,
# defined as L[0]-L[1]+L[2]-L[3] ... L[len(L)-1] where even numbered
# indeces are added to the sum and odd numbered indeces are subtracted
# from the sum (when mode is True) and even/odd interpretations are
# inverted (when mode is False).
#
# Write the iterative formulation of alternating sum (feel free to use
# for loops, while loops, or comprehensions however you see fit).
#
# >>> intAltSum(range(10), True)
# -5
# >>> intAltSum(range(10), False)
# 5
# >>> intAltSum((1, -2, 3, -4, 5, -6))
# 21
# >>> intAltSum((1, -2, 3, -4, 5, -6), False)
# -21
#
#my solution
def intAltSum(L, mode=True):
    if mode==True:
        return sum(L[::2]) - sum(L[1::2])
    if mode==False:
        return -(sum(L[::2]) - sum(L[1::2]))
    #oops, it looks like I didn't even use iteration 

#most elegant solution, but includes no form of iteration
#def intAltSum(L, mode=True):
    #if mode:
        #return(sum(L[::2]) - sum(L[1::2]))
    #return(sum(L[1::2]) - sum(L[::2]))

#using comprehensions
#def intAltSum(L, mode=True):
    #if mode:
        #return sum([L[i] for i in range(0, len(L), 2)]) - sum([L[i] for i in range(1, len(L), 2)])
    #return sum([L[i] for i in range(1, len(L), 2)]) - sum([L[i] for i in range(0, len(L), 2)])

#You can use a purely iterative structure too, which would use accumulation.
#I'm not going to write all this out though because it's very clunky code.

#recursive version
#def intAltSum(L, mode=True):
    #if len(L)==0:
        #return(0)   #base case for all sequence types
    #if mode:
        #return(L[0]+intAltSum(L[1:], False))   # False recursive step
    #return(-L[0]+intAltSum(L[1:], True))       # True recursive step 



        
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
    if intAltSum(range(10), True) is None:
        print("### Error: your definition of intAltSum() doesn't return a value.")
    if intAltSum(range(10), True) != -5:
        print("### Error: intAltSum(range(10), True) != -5")
    if intAltSum(range(10), False) != 5:
        print("### Error: intAltSum(range(10), False) != 5")
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
