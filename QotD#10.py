# CS1210: QotD10
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
# showScores(nplayers, S) takes nplayers, an integer, and S, a list of
# integer values representing the current score in the game, and
# produces a string suitable for printing that represents the current state.
#
# For example:
#    >>> showScores(3, [10, 44, 13])
#    '1:10, 2:44, 3:13'
#    >>> showScores(4, [10, 44, 13, 0])
#    '1:10, 2:44, 3:13, 4:0'
# Pay close attention to the spacing and punctuation.
#
# See HW1 for additional context.
#
# Note: you will need to use a comprehension.
# 
def showScores(nplayers, S):
    return ', '.join([str(x)+":"+str(S[x-1]) for x in [i for i in range(1,nplayers+1)]])

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
    if showScores(3, [10, 11, 12]) is None:
        print("### Error: your definition of unfilled() doesn't return a value.")
    if showScores(3, [10, 11, 12]) != '1:10, 2:11, 3:12':
        print("### Error: showScores(3, [10, 11, 12]) != '1:10, 2:11, 3:12'")
    if showScores(7, [22, 14, 7, 18, 33, 15, 3]) != '1:22, 2:14, 3:7, 4:18, 5:33, 6:15, 7:3':
        print("### Error showScores(7, [22, 14, 7, 18, 33, 15, 3]) != '1:22, 2:14, 3:7, 4:18, 5:33, 6:15, 7:3'")
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
