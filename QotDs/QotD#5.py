# CS1210: QotD5
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely your own work, and
#  2) it has not been shared with anyone outside the instructional team.
#
# Note: we are not asking for your password or your hawkid ID number,
# just your login identifier: for example, mine is "segre".
#
def signed():
    return(["glflores"])

######################################################################
# Specification: wordOvlp(w1, w2) takes two strings, w1 and w2, and
# returns an integer representing the percentage of letters appearing
# in both w1 and w2 with respect to the longer of w1 and w2.
#
# Example:
#   >>> wordOvlp('computer', 'science')
#   25
#   >>> wordOvlp('raise','mouth')
#   0
#   >>> wordOvlp('gamma', 'lambda')
#   33
#
# Hint: duplicate characters that appear in both words count only
# once. Thus while 'gamma' and 'lambda' share an 'm' and 2 'a's, the
# percentage is calculated as 2/6 or 33%.
#
# Note: solutions that use iteration (e.g., for, while or similar)
# will not earn any credit.
#
def wordOvlp(w1, w2):
    if(w1=='' and w2==''):
        return("undefined")
    elif(len(w1)>=len(w2)):
        longerString = w1
    elif(len(w2)>=len(w1)):
        longerString = w2
    return int((len(set(w1)&set(w2))/(len(longerString)))*100)


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
    if wordOvlp('computer', 'science') is None:
        print("### Error: your definition of wordOvlp() doesn't return a value.")
    if wordOvlp('computer', 'science') != 25:
        print("### Error: wordOvlp('computer', 'science') != 25.")
    if wordOvlp('raise','mouth') != 0:
        print("### Error: wordOvlp('raise','mouth') != 0")
    if wordOvlp('gamma', 'lambda') != 33:
        print("### Error: wordOvlp('gamma', 'lambda') != 33")
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
