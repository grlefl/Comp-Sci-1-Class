# CS1210: Lab4 [3 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partners, and
#  2) it has not been shared with anyone outside the instructional team.
# N.B., add a third string to the list if there are three of you.
#
# N.B., your hawkid is not the same as your student id number!
def signed():
    return(["glflores","sfdennis"])

######################################################################
# Specification: reverseWords(S) takes a string, S, and returns a new
# string that consists of the same words as S but with each word
# individually reversed. Make no other changes: conserve upper/lower
# case, etc., avoid unnecessary assignments, and be sure to use a
# comprehension!
#
# Example:
#   >>> reverseWords('To be or not to be')
#   'oT eb ro ton ot eb'
#   >>> reverseWords('The rain in Spain')
#   'ehT niar ni niapS'
#   >>> reverseWords('Help! I need somebody!')
#   '!pleH I deen !ydobemos'
#
def reverseWords(S):
    return ' '.join([x[::-1] for x in S.split()])

######################################################################
# Specification: isogram(S) returns True if no character in S (apart
# from the space character) appears more than once in S. Otherwise, it
# returns false.
#
# Hint: stop and think, carefully, about whether you need a
# comprehension to construct a short, concise, and elegant
# solution. Less-than-elegant solutions may not earn full credit, so
# avoid extra assignments and other unnecessary structure.
#
# Example:
#   >>> isogram('brick house')
#   True
#   >>> isogram("Wise men say")
#   False
#   >>> isogram('tears flow up')
#   True
#
def isogram(S):
    return all([S.count(x)==1 for x in S if x!=' '])

######################################################################
# Specification: neighbor(S1, S2) takes two sequences (you can assume
# len(S1)==len(S2)) and returns True if and only if the two sequences
# differ in one and only one element. Note that upper/lower case
# versions of the same character are not considered different.  Use a
# comprehension.
#
# Example:
#   >>> neighbor('cat', 'dog')
#   False
#   >>> neighbor('houSe', 'Mouse')
#   True
#   >>> neighbor('Dubble', 'BUBBLE')
#   True
#
def neighbor(S1, S2):
    return sum([S1.lower()[x]==S2.lower()[x] for x in range(len(S1))]) == (len(S1)-1)

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
#####################################################################
if __name__ == '__main__':
    if all([ "hawkid" in x for x in signed() ]):
        print('### Warning: Complete definition of signed() or no points will be awarded!')
    if reverseWords('Help! I need somebody!') != '!pleH I deen !ydobemos':
        print("### Error: reverseWords('Help! I need somebody!') != '!pleH I deen !ydobemos")
    if not isogram('brick house'):
        print("### Error: isogram('brick house') should be True")
    if isogram('Wise men say'):
        print("### Error: isogram('Wise men say') should be False")
    if neighbor('cat', 'dog'):
        print("### Error: neighbor('cat', 'dog') should be False")
    if not neighbor('Dubble', 'BUBBLE'):
        print("### Error: neighbor('Dubble', 'BUBBLE') should be print('### Absence of errors does not guarantee correctness over all possible inputs.')
    print('### Check your work carefully against the specification before submitting to ICON.')
