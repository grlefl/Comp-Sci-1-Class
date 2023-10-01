# CS1210: Lab6 [2 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partners, and
#  2) it has not been shared with anyone outside the instructional team.
# N.B., add a third string to the list if there are three of you.
#
# N.B., your hawkid is not the same as your student id number!
def signed():
    return(["glflores"])

######################################################################
# Specification: superSum(S) takes S, a list or tuple of integers
# and/or other lists/tuples, themselves packed with lists/tuples or
# integers, and returns a sum of all of the integers in S regardless
# of level of nesting.
#
# Example:
#   >>> superSum([1, 2, 3])
#   6
#   >>> superSum([[1, 2, 0], 3, (4, 5)])
#   15
#   >>> superSum(((0,), [14, -8], (((2,),),)))
#   8
#
# Note: your solution must be recursive. 
#
def superSum(S):
    if S==[] or S==():
        return(0)
    elif (not isinstance(S,list)) and (not isinstance(S,tuple)):
        return(S)
    else:
        return(superSum(S[0])+superSum(S[1:]))

######################################################################
# Specification: reverseAbjad(S) takes a sentence, S, and converts it
# into an equivalent sentence, written right-to-left, without any
# vowels. You can assume the usual set of vowels (a, e, i, o, and u),
# and should conserve all non-vowel characters (consonants,
# punctuation, numerals, etc.) as well as case.
#
# Background: A number of ancient writing scripts are abjadic, meaning
# that only consonants are written, leaving the reader to infer the
# vowels as they go. Modern Arabic, Hebrew, Persian and Urdu are
# abjadic; many ancient languages like Aramaic, Berber, Mandaic are
# also abjadic.  In fact, even some forms of English communication
# (usually over SMS) have become informal abjads! Consider "o rly?",
# "thx", or "r u nts?", and so on (although these tend to retain the
# ``most important'' letters rather than consonants specifically).
# Here, we have added a twist that the resulting script is to be read
# from right to left.
#
# Example:
#   >>> reverseAbjad("In a minute!")
#   '!tnm n'
#   >>> reverseAbjad('I think Python is fabulous.')
#   '.slbf s nhtyP knht'
#   >>> reverseAbjad('I think therefore I am')
#   'm rfrht knht'
#
# Your solution must use a comprehension and must be concise; you may
# freely use string methods. Unnecessary assignment statements or poor
# choice of iterative form will entail loss of credit.
#
# Warning: Note that some words, like "a" or "I" may disappear
# entirely, leaving extra spaces here and there. For full credit,
# flush these extra spaces.
#
def reverseAbjad(S):
    return ' '.join((''.join([x for x in S[::-1] if x not in 'aeiouAEIOU'])).split())
    #I tried this other return statement. It works, but it's way too long:
    #return ' '.join([r for r in [''.join(l) for l in [[z for z in y if z.lower() not in 'aeiou'] for y in [x for x in S[::-1].split()]]] if r !=''])  
######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
###################################################################### 
if __name__ == '__main__':
    L = list(range(15))
    if all([ "hawkid" in x for x in signed() ]):
        print('### Warning: Complete definition of signed() or no points will be awarded!')
    if superSum(((0,), [14, -8], (((2,),),))) != 8:
        print("### Error: superSum(((0,), [14, -8], (((2,),),))) != 8")
    if superSum([1, 2, 3, 4]) != 10:
        print("### Error: superSum([1, 2, 3, 4]) != 10")
    if reverseAbjad('Never let me go') != 'g m tl rvN':
        print("### Error: reverseAbjad('Never let me go') != 'g m tl rvN'")
    if reverseAbjad('I think therefore I am') != 'm rfrht knht':
        print("### Error: reverseAbjad('I think therefore I am') != 'm rfrht knht'")
    print('### Absence of errors does not guarantee correctness over all possible inputs.')
    print('### Check your work carefully against the specification before submitting to ICON.')
