# CS1210: Lab7 [4 functions to complete]
######################################################################
# Complete the signed() function, certifying that:
#  1) the code below is entirely the work of you and your partners, and
#  2) it has not been shared with anyone outside the instructional team.
# N.B., add a third string to the list if there are three of you.
#
# N.B., your hawkid is not the same as your student id number!
def signed():
    return(["yalzhao","rocheng","glflores"])

######################################################################
# Specification: np(S) takes a lower case string, S, and returns True
# if S is a "near palindrome", and False otherwise.
#
# A "near palindrome" is a string that reads the same forwards or
# backwards when it is off by one. In other words, there is an extra
# letter that you ignore at either the beginning or the end of S, but
# not both.
#
# Example (note 'ailipilia' is indeed a palindrome):
#   >>> np('ailipilia')
#   False
#   >>> np('ailipilias')
#   True
#   >>> np('pailipilia')
#   True
#   >>> np('ailipixlia')
#   False
#
# You are free to use any approach you like, although one suggestion
# is to use slices.
#
def np(S):
    if S[0] == S[-1]:
        if S == S[::-1]:
            return(False)
    if S[0] != S[-1]:
        if S[1:]==S[1:][::-1] or S[:-1]==S[:-1][::-1]:
            return(True)
    else:
        return(False)
    
#Solution
#def np(S):
    #return S[1:]==S[1:][::-1] or S[:-1]==S[:-1][::-1]


######################################################################
# Specification: iqp(S) takes a lower case string, S, and returns True
# if S is a "quasi palindrome", and False otherwise.
#
# A "quasi palindrome" is like a "near palindrome" except you can skip
# up to one letter anywhere in the string -- not just at the beginning
# or the end of S! So:
#
# Example:
#   >>> iqp('ailipilia')
#   True
#   >>> iqp('ailipilias')
#   True
#   >>> iqp('pailipilia')
#   True
#   >>> iqp('aixlipilia')
#   True
#   >>> iqp('aixlipilixa')
#   False
#
# Your function should use iteration; feel free to make use of np()
# defined above.
#
def iqp(S):
    S = S.lower()
    if S==S[::-1]:
        return(True)
    else:
        while S[0]==S[-1]:
            S = S[1:-1]
    return(np(S))

#Solution
#def iqp(S):
    #for i in range(len(S)//2):
        #if S[i]!=S[len(S)-i-1]
            #return np(S[i:len(S)-i])
    #return True    #if there's not a mismatch, it is immediately True

######################################################################
# Specification: rqp(S) takes a lower case string, S, and returns True
# if S is a "quasi palindrome", and False otherwise.
#
# This is just a recursive rewrite of iqp(). Again, feel free to use
# np() defined above.
#
def rqp(S):
    pass

#Solution
#def rqp(S):
    #if len(S) < 2:
        #return True
    #elif S[0]!=S[-1]:
        #return np(S)
    #return rqp(S[1:-1])

######################################################################
# Specification: kqp(S, k=0) takes a lower case string, S, and returns
# the minimum number of skipped characters that are required to treat
# S as a palindrome.
#
# This is essentially an extension of rqp(). We'll use k, initially 0
# by default, to count how many "bad" characters you had to skip while
# trying to force S into that palindrome idea. Obviously, you won't be
# able to use np() here, because it doesn't do any "counting" but
# looking at np() may help you extend kqp() to its logical conclusion.
#
# Example:
#   >>> kqp('ailipilia')
#   0
#   >>> kqp('aixlipilia')
#   1
#   >>> kqp('aixlipilixa')
#   2
#   >>> kqp('aixlipdeilixa')
#   4
#
﻿def kqp(S, k=0):
    for i in range(len(S)):
        if S.lower()[i] != S.lower()[::-1][i] and S.lower()[i+1] == S.lower()[::-1][i+1]:
            k = k+1
        return(k)

#Solution
#def kqp(S,k=0):
    #if len(S) < 2:
        #return k
    #elif S[0]!=S[-1]:
        #return min(kqp(S[1:],k+1), kqp(S[:-1],k+1))
    #return kqp(S[1:-1],k)
#This solution is hard for me to understand. 

    
    

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
###################################################################### 
if __name__ == '__main__':
    L = list(range(15))
    if all([ "hawkid" in x for x in signed() ]):
        print('### Warning: Complete definition of signed() or no points will be awarded!')
    if np('ailipilia')!=False:
        print("### Error: np('ailipilia')!=False")
    if np('ailipilias')!=True:
        print("### Error: np('ailipilias')!=True")
    if iqp('ailipilia')!=True:
        print("### Error: iqp('ailipilia')!=True")
    if iqp('ailipilias')!= True:
        print("### Error: iqp('ailipilias')!=True")
    if iqp('pailipilia')!= True:
        print("### Error: iqp('pailipilia')!= True")
    if iqp('aixlipilia')!= True:
        print("### Error: iqp('aixlipilia')!= True")
    if iqp('aixlipilixa')!= False:
        print("### Error: iqp('aixlipilixa')!= False")
    if rqp('ailipilia')!=True:
        print("### Error: rqp('ailipilia')!=True")
    if rqp('ailipilias')!= True:
        print("### Error: rqp('ailipilias')!=True")
    if rqp('pailipilia')!= True:
        print("### Error: rqp('pailipilia')!= True")
    if rqp('aixlipilia')!= True:
        print("### Error: rqp('aixlipilia')!= True")
    if rqp('aixlipilixa')!= False:
        print("### Error: rqp('aixlipilixa')!= False")
    if kqp('ailipilia')!=0:
        print("### Error: kqp('ailipilia')!=0")
    if kqp('aixlipilia')!=1:
        print("### Error: kqp('aixlipilia')!=1")
    if kqp('aixlipilixa')!=2:
        print("### Error: kqp('aixlipilixa')!=2")
    if kqp('aixlipdeilixa')!=4:
        print("### Error: kqp('aixlipdeilixa')!=4")
    print('### Absence of errors does not guarantee correctness over all possible inputs.')
    print('### Check your work carefully against the specification before submitting to ICON.')
