# CS1210: Lab8 [3 functions to complete]
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
# Specification: fprint(w) takes a string, w, representing a single
# word and returns a "fingerprint" of that word consisting of an
# ordered string of its constituent lower-case letters.
#
# Example:
#   >>> fprint('bottle')
#   'belot'
#   >>> fprint('obstinate')
#   'abeinost'
#   >>> fprint('bookkeeper')
#   'bekopr'
#
# my solution:
def fprint(w):
    return ''.join(sorted(set([x for x in w.lower()]))) 
# good
# Correction: comprehension was unnecessary, just say set(w.lower())

######################################################################
# Specification: findex(S) takes a series of words (like a short
# story) and returns a dictionary where the key is the fingerprint of
# the a word and the value is a list of indexes into the story wher
# words matching the fingerprint occur.
#
# Example:
#   >>> findex('Red red wine goes to my head')
#   {'der': [0, 1], 'einw': [2], 'egos': [3], 'ot': [4], 'my': [5], 'adeh': [6]}
#   >>> findex('Wise men say only fools rush in')
#   {'eisw': [0], 'emn': [1], 'asy': [2], 'lnoy': [3], 'flos': [4], 'hrsu': [5], 'in': [6]}
#
# Hint: feel free to make use of the fprint() function above.
#
# my solution:
def findex(S):
    L = S.lower().split()
    index = -1  # I randomly included this part for no reason. 
    return {fprint(x):[y for y in range(0,len(L)) if L[y]==x] for x in L}     
# good

# Corrections:
# possible problem with dictionary comprehension:
# If the key matches, and the words will have the same fingerprint, the
# last word of that fingerprint will be remembered.
# I don't think this is a problem with my comprehension?

# I think my solution is better, assuming it works.

# Solution
def findex(S):
    D = []
    i = 0
    for w in S.lower().split():
        f = fprint(w)
        if f not in D:
            D[f] = [i]
        else:
            D[f].append(i)
        i = i + 1
    return D
    # use assignments when you must evaluate something once, but use it
    # multiple times 

######################################################################
# Specification: bet(S) takes a series of words and converts them into
# a Pig-latin-like language called "bet." To convert a sentence into
# bet, you need to replace each vowel with three letters: the vowel,
# the letter 'b', and the vowel repeated. So words like "cat" become
# "cabat" and "dog" becomes "dobog".
#
# Example:
#   >>> bet('Red red wine goes to my head')
#   'Rebed rebed wibinebe goboebes tobo my hebeabad'
#   >>> bet('Wise men say only fools rush in')
#   'Wibisebe meben sabay only foboobols rubush in'
#
# Hint: feel free to use a helper function.
#
# my solution:
def bet(S):
    L = list(S)
    for x in range(0, len(L)-1):
        if L[x] in 'aeiou':
            L[x] = L[x]+'b'+L[x]
    return ''.join(L)
# okayish, but not great
# this is the version I submitted, but it does not agree with the last example


# Corrections:
# he messed up the example, first vowel was not caught
# my code failed on this example:
#   Failed example:
#   bet('Cause uptown funk gonna give it to you')
#   Expected:
#   'Cabaubusebe ubuptobown fubunk gobonnaba gibivebe ibit tobo yoboubu'
#   Got:
#   'Cabaubusebe ubuptobown fubunk gobonnaba gibivebe ibit tobo yobou'
# It disregards the last element, and I'm not really sure why?

# my fixed solution:
def bet(S):
    L = list(S)
    for x in range(0, len(L)):
        if L[x] in 'aeiou':
            L[x] = L[x]+'b'+L[x]
    return ''.join(L)
# I made the mistake of thinking range was inclusive (probably thinking randint).


# Solution
def bet(S):
    def bethelp(w):
        for i in range(len(w)-1, -1, -1):
            if w[i] in 'aeiouAEIOU':
               w[i:i+1] = [w[i], 'b', w[i]]
        return ''.join(w)
    return ' '.join([ bethelp(list(w)) for w in S.split() ])
# For every word, we are testing for vowels and then returning the changed word.
# At the end, all the words are joined together.
# Scanning list from last element to first, so that you don't have to worry
# about list length growing behind you.
#
# This also accounts for uppercase vowels, but it's kind of funky. If you have
# "Ant", it will be returned as "AbAnt".

                
    

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
###################################################################### 
if __name__ == '__main__':
    L = list(range(15))
    if all([ "hawkid" in x for x in signed() ]):
        print('### Warning: Complete definition of signed() or no points will be awarded!')
    if fprint('bottle') != 'belot':
        print("### Error: fprint('bottle') != 'belot'")
    if fprint('obstinate') != 'abeinost':
        print("### Error:  fprint('obstinate') != 'abeinost'")
    if fprint('bookkeeper') != 'bekopr':
        print("### Error:  fprint('bookkeeper') != 'bekopr'")
    if findex('Red red wine goes to my head') != {'der': [0, 1], 'einw': [2], 'egos': [3], 'ot': [4], 'my': [5], 'adeh': [6]}:
        print("### Error:  findex('Red red wine goes to my head') != {'der': [0, 1], 'einw': [2], 'egos': [3], 'ot': [4], 'my': [5], 'adeh': [6]}")
    if findex('Wise men say only fools rush in') != {'eisw': [0], 'emn': [1], 'asy': [2], 'lnoy': [3], 'flos': [4], 'hrsu': [5], 'in': [6]}:
        print("### Error:  findex('Wise men say only fools rush in') != {'eisw': [0], 'emn': [1], 'asy': [2], 'lnoy': [3], 'flos': [4], 'hrsu': [5], 'in': [6]}")
    if bet('Red red wine goes to my head') != 'Rebed rebed wibinebe goboebes tobo my hebeabad':
        print("### Error:  bet('Red red wine goes to my head') != 'Rebed rebed wibinebe goboebes tobo my hebeabad'")
    if bet('Wise men say only fools rush in') != 'Wibisebe meben sabay only foboobols rubush in':
        print("### Error:  bet('Wise men say only fools rush in') != 'Wibisebe meben sabay only foboobols rubush in'")
    print('### Absence of errors does not guarantee correctness over all possible inputs.')
    print('### Check your work carefully against the specification before submitting to ICON.')
