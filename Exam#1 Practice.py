# Exam1 Practice Problems
######################################################################
# Specification: sumByproduct(i, j) takes two integers, i and j, and
# returns the sum of i and j times the product of i and j.
#
# Example:
#   >>> sumByProduct(-3, 7)
#   -84
#
def sumByProduct(i, j):
    return(i+j)*(i*j)
######################################################################
# Specification: extendSequence(S, i, j) takes a sequence, S, and two
# integers, i < len(S) and j >= 0, and returns a (new) sequence
# consisting of S with the last i elements repeated exactly j times.
# Note: your solution should not use if/elif/else; rather it should
# return the value of a single expression.
#
# Examples:
#   >>> extendSequence((1, 3, 5, 6), 2, 3)
#   (1, 3, 5, 6, 5, 6, 5, 6)
#   >>> extendSequence("yes", 1, 10)
#   'yessssssssss'
#   this example doesn't work; error from teacher? i = 2?
#   I also don't know what any corner cases would be. 
#
# Hint: beware corner cases.
#
def extendSequence(S, i, j):
    return S[:i]+(S[i:])*j
######################################################################
# Specification: spliceEnds(S, i) takes a sequence, S, and an integer,
# i, and returns a (new) sequence consisting of the last i elements of
# S spliced with S spliced with the first i elements of S.
#
# Note: no assignment is needed: your solution should not use
# if/elif/else, and should function appropriately even if i > len(S):
# in other words, a single expression in the return suffices.
#
# Examples:
#   >>> spliceEnds((1, 3, 5, 6), 2)
#   (5, 6, 1, 3, 5, 6, 1, 3)
#   >>> spliceEnds("0123456", 3)
#   '4560123456012'
#   Another error from teacher? I am so confused. These examples
#   don't share the same specification. 
#
# Hint: beware corner cases.
#
def spliceEnds(S, i):
    return S[i:]+S+S[:i]
######################################################################
# Specification: eviscerateList(L, i, j) takes a list, L, and two
# integers, i and j, and modifies the list, L, such that j elements
# starting at index location i are surgically removed from L. The
# function should then return the new value of L.
#
# You may assume 0<=i<len(L) and 0<j.
#
# Examples:
#   >>> L=list(range(10))
#   >>> L
#   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#   >>> eviscerateList(L, 6, 2)
#   [0, 1, 2, 3, 4, 5, 8, 9]
#   >>> L
#   [0, 1, 2, 3, 4, 5, 8, 9]
#   >>> eviscerateList(eviscerateList(L, 7, 1), 1, 3)
#   [0, 4, 5, 8]
#   not working for this one!?!?!?!
#
def eviscerateList(L, i, j):
    return L[:i]+L[i+j:]
######################################################################
# Specification: nearAnagram(S1, S2) takes two sequences, S1 and S2,
# and returns True if the two sequences are possible anagrams of each
# other.
#
# Recall an anagram is simply a permutation of the characters of one
# string to make another word, such as "servant" and "taverns" (here,
# we'll extend the notion from strings to sequences, including lists
# and tuples).
#
# A "near anagram" are two sequences that share the same length and
# are made of identical elements, but my differ in how many times each
# element occurs.
#
# Example:
#    >>> nearAnagram('taverns', 'servant')
#    True
#    >>> nearAnagram([1, 2, 3, 1], (2, 2, 1, 3))
#    True
#    >>> nearAnagram([1, 2, 3, 1], [3, 2, 1])
#    False
#
# Hint: do not use assignment or conditionals.
#
def nearAnagram(S1, S2):
    return len(S1)==len(S2) and (sorted(list(set(S1))))==(sorted(list(set(S2))))
######################################################################
# Specification: invert(L) takes a list L and modifies it by
# exchanging its first and last halves while also reversing the last
# (now first) half, and returning the new value of L.
#
# Example:
#   >>> L=list(range(12))
#   >>> invert(L)
#   [11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]
#   >>> L
#   [11, 10, 9, 8, 7, 6, 0, 1, 2, 3, 4, 5]
#   >>> L=[]
#   >>> invert(L)
#   []
#   >>> L=[1, 2]
#   >>> invert(L)
#   [2, 1]
#   >>> L
#   [2, 1]
#
# Hint: no iteration.
#
# Hint: list operations must be destructive.
#
def invert(L):
    pass
######################################################################
# Specification: Write a function rotateLeft(S, k) that takes a
# sequence, S, and an integer, 0 <= k < len(S) and returns a new
# sequence of the same type of S containing all of the elements of S
# rotated to the left.
#
# Example:
#   >>> rotateLeft(list(range(10)), 1)
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#   >>> rotateLeft(tuple(range(10)), 8)
#   (8, 9, 0, 1, 2, 3, 4, 5, 6, 7)
#   >>> rotateLeft('foobarbaz', 3)
#   'barbazfoo'
#   >>> rotateLeft('foobarbaz', 1)
#   'oobarbazf'
#
def rotateLeft(S, k):
    pass
                 
######################################################################
# Specification: Write a function rotateRight(S, k) that takes a
# sequence, S, and an integer, 0 < k < len(S) and returns a new sequence
# of the same type of S containing all of the elements of S rotated to
# the right.
#
# Example:
#   >>> rotateRight(list(range(10)), 1)
#   [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
#   >>> rotateRight(tuple(range(10)), 8)
#   (2, 3, 4, 5, 6, 7, 8, 9, 0, 1)
#   >>> rotateRight('foobarbaz', 3)
#   'bazfoobar'
#   >>> rotateRight('foobarbaz', 1)
#   'zfoobarba'
#
def rotateRight(S, k):
    pass
######################################################################
# Specification: Write a function reverseInt(n) that takes a positive
# integer n and returns the integer that has the same digits of n
# but in reverse order.
#
# Example:
#   >>> reverseInt(7102)
#   2017
#   >>> reverseInt(1024)
#   4201
#   >>> reverseInt(5255498)
#   8945525
#   >>> reverseInt(100)#
# Hint: no iteration.
#
# Hint: list operations must be destructive.
#
def invert(L):
    pass
######################################################################
# Specification: Write a function rotateLeft(S, k) that takes a
# sequence, S, and an integer, 0 <= k < len(S) and returns a new
# sequence of the same type of S containing all of the elements of S
# rotated to the left.
#
# Example:
#   >>> rotateLeft(list(range(10)), 1)
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#   >>> rotateLeft(tuple(range(10)), 8)
#   (8, 9, 0, 1, 2, 3, 4, 5, 6, 7)
#   >>> rotateLeft('foobarbaz', 3)
#   'barbazfoo'
#   >>> rotateLeft('foobarbaz', 1)
#   'oobarbazf'
#
def rotateLeft(S, k):
    pass
                 
######################################################################
# Specification: Write a function rotateRight(S, k) that takes a
# sequence, S, and an integer, 0 < k < len(S) and returns a new sequence
# of the same type of S containing all of the elements of S rotated to
# the right.
#
# Example:
#   >>> rotateRight(list(range(10)), 1)
#   [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
#   >>> rotateRight(tuple(range(10)), 8)
#   (2, 3, 4, 5, 6, 7, 8, 9, 0, 1)
#   >>> rotateRight('foobarbaz', 3)
#   'bazfoobar'
#   >>> rotateRight('foobarbaz', 1)
#   'zfoobarba'
#
def rotateRight(S, k):
    pass
######################################################################
# Specification: Write a function reverseInt(n) that takes a positive
# integer n and returns the integer that has the same digits of n
# but in reverse order.
#
# Example:
#   >>> reverseInt(7102)
#   2017
#   >>> reverseInt(1024)
#   4201
#   >>> reverseInt(5255498)
#   8945525
#   >>> reverseInt(100)
#   1
#
# Note: it's OK if leading zeros disappear (last example)
#
def reverseInt(n):
    pass
