# CS1210: QotD9
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
# unfilledTable(T) returns True if there are any unfilled slots in
# table T. Recall unfilled slots are slots where the card is facing
# down, that is, has not been revealed. Returns True or False.
#
# See HW1 for additional context.
#
# Example:
#   >>> unfilled([[False, (3, 'A')], [True, (2, 'C')], [False, (1, 'C')]])
#   True
#   >>> unfilled([[True, (1, 'C')], [True, (2, 'C')], [True, (3, 'B')]])
#   False
#
# Note: This is a simple Boolean function. It does not require 5 lines
# of code. It is a single return statement. Be concise.
#
# Hint: Use a comprehension and/or other, non for/while, types of
# iteration.
#
def unfilled(T):
    return [x[0] for x in T if x[0]==False] != []

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
    if unfilled([[False, (3, 'A')], [True, (2, 'C')], [False, (1, 'C')]]) is None:
        print("### Error: your definition of unfilled() doesn't return a value.")
    if unfilled([[False, (3, 'A')], [True, (2, 'C')], [False, (1, 'C')]]) is False:
        print("### Error: unfilled([[False, (3, 'A')], [True, (2, 'C')], [False, (1, 'C')]]) != True")
    if unfilled([[True, (1, 'C')], [True, (2, 'C')], [True, (3, 'B')]]) is True:
        print("### Error unfilled([[True, (1, 'C')], [True, (2, 'C')], [True, (3, 'B')]]) != False")
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
