# CS1210: QotD7
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
# Specification: filterWords(S, c1, c2) takes a string, S, and two
# lower-case characters, c1 and c2, and returns a list of words
# (subsequences of S separated by spaces or other whitespace
# characters) in S, converted to lower case, that contain both c1 and
# c2. Your solution must use a comprehension and contain no other form
# of iteration or assignment.
#
# Example:
#   >>> filterWords('To be or not to be', 'o', 't')
#   ['to', 'not', 'to']
#   >>> filterWords('The rain in spain falls mainly in the plains', 'a', 'l')
#   ['falls', 'mainly', 'plains']
#
# Note: The following additional example relies on a small (optional)
# change to the function signature.
#   >>> filterWords('To be or not to be', 'e')
#   ['be', 'be']
#
def filterWords(S, c1, c2=''):
    return [x for x in S.lower().split() if c1 in x and c2 in x]

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
    if filterWords('To be or not to be', 'o', 't') is None:
        print("### Error: your definition of filterWords() doesn't return a value.")
    if filterWords('To be or not to be', 'o', 't') != ['to', 'not', 'to']:
        print("### Error: filterWords('To be or not to be', 'o', 't') != ['to', 'not', 'to']")
    if filterWords('The rain in spain falls mainly in the plains', 'a', 'l') != ['falls', 'mainly', 'plains']:
        print("### Error: filterWords('The rain in spain falls mainly in the plains', 'a', 'l') != ['falls', 'mainly', 'plains']")
    if filterWords('To be or not to be', 'e') != ['be', 'be']:
        print("### Error: filterWords('To be or not to be', 'e') != ['be', 'be']")
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
