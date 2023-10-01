# CS1210: QotD4
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
# Specification: wordCheck(w) takes a non-empty string, w, and returns
# True if and only if the first and last characters of w appear
# seqeuntially in w.
#
# Example:
#   >>> wordCheck('infer')
#   False
#   >>> wordCheck('success')
#   True
#   >>> wordCheck('is')
#   True
#
def wordCheck(w):
    return((w[0]+w[-1]) in w)

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
    if wordCheck('infer') is None:
        print("### Error: your definition of wordCheck() doesn't return a value.")
    if wordCheck('infer'):
        print("### Error: wordCheck('infer') returns True but should return False.")
    if not wordCheck('success'):
        print("### Error: wordCheck('success') returns False but should return True.")
    if not wordCheck('is'):
        print("### Error: wordCheck('is') returns False but should return True.")
    else:
        print('''\
### Your solution passes sample test cases, but this does not guarantee correctness over all inputs.
### Check your work carefully against the specification.
### When you are satisfied, download the file and submit it to ICON.''')
