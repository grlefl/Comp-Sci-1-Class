# CS1210: Lab3 [3 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partners, and
#  2) it has not been shared with anyone outside the instructional team.
# N.B., add a third string to the list if there are three of you.
#
# N.B., your hawkid is not the same as your student id number!
def signed():
    return(["hawkid1","hawkid2"])

######################################################################
# Specification: purgeSubstring(S, ss) takes a string, S, and a
# substring of S, ss, and returns a copy of S with that substring
# removed if it is found.
#
# Example:
#   >>> purgeSubstring("The rain in Spain", 'he ')
#   'Train in Spain'
#   >>> purgeSubstring("The rain in Spain", 'plains')
#   'The rain in Spain'
#
# Hint: do not use iteration; instead you will need to use the
# appropriate string search method from [TP] C8 and your cheatsheet.
#
# Your solution should only be a few lines long.
#
def purgeSubstring(S, ss):
    return(S.replace(ss,''))

######################################################################
# Specification: fresh(w1, w2) returns a string containing all the
# lower case characters that do not occur in either w1 or w2 in
# alphabetical order (i.e., they are "fresh"). The optional third
# argument, characters, will by default contain a string with all 26
# lower case Roman characters, derived from the built-in constant
# printable from the string library.
#
# Note that w1 and w2 may contain upper case and/or non-alpha
# characters; the former should be converted to lower case, and the
# latter should be ignored.
#
# Example:
#   >>> fresh('The rain in Spain', 'falls mainly in the plains')
#   'bcdgjkoquvwxz'
#
# Hint: You may need to review some of the string and/or container
# methods described on your exam cheatsheet.
#
from string import printable
#
def fresh(w1, w2, characters=printable[10:36]):
    alphabet = set(characters)

    return(''.join(sorted(list(alphabet-(set(w1)|set(w2))))))

   

######################################################################
# Specification: smoosh(S) takes a string consisting of space
# separated words and returns the same string having removed all
# spaces. Nothing else should change.
#
# Example:
#   >>> smoosh("CS1210 Midterm Exam 1 will take place TOMORROW")
#   'CS1210MidtermExam1willtakeplaceTOMORROW'
#
#
# Hint: Review the string methods in C10 of [TP] or yoru cheatsheet.
#
def smoosh(S):
    return(''.join(S.split()))

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
#####################################################################
if __name__ == '__main__':
    if all([ "hawkid" in x for x in signed() ]):
        print('### Warning: Complete definition of signed() or no points will be awarded!')
    if purgeSubstring("The rain in Spain", 'he ') != 'Train in Spain':
        print('### Error: purgeSubstring("The rain in Spain", "he ") does not return "Train in Spain"')
    if purgeSubstring("The rain in Spain", 'plains') != 'The rain in Spain':
        print('### Error: purgeSubstring("The rain in Spain", "plains") does not return "The rain in Spain"')
    if fresh('The rain in Spain', 'falls mainly in the plains') != 'bcdgjkoquvwxz':
        print('### Error: fresh("The rain in Spain", "falls mainly in the plains") does not return "bcdgjkoquvwxz"')

    if smoosh("CS1210 Midterm Exam 1 will take place TOMORROW") != 'CS1210MidtermExam1willtakeplaceTOMORROW':
        print('### Error: smoosh("CS1210 Midterm Exam 1 will take place TOMORROW") does not return "CS1210MidtermExam1willtakeplaceTOMORROW"')
    print('### Absence of errors does not guarantee correctness over all possible inputs.')
    print('### Check your work carefully against the specification before submitting to ICON.')
