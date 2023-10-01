#Problem 1
#The inOrder(S) function takes a string, S, that can be divided into a list
#of words, and returns a list Booleans, where each True/False corresponds to
#whether or not the characters in the corresponding word in S are in
#alphabetical order (note: all comparisons are performed on lower case versions
# of the words in S).

# >>> inOrder('Do you know the way')
# [True, False, True, False, False]

# >>> inOrder('Billie Jean is not my lover')
# [False, False, True, True, True, False]


# Note: Use a comprehension and no other form of iteration or assignment.

#My Solution
#def inOrder(S):
    #return [(True for x if x==x.sort()) or (False for x if x!=x.sort())
            #for x in S.lower().split()]

#Solution
def inOrder(S):
    return [w==''.join(sorted(w)) for w in S.lower().split()]
#except this solution isn't working!!!






#Problem 2
#A sequence of numbers is biotic if it is of length 2 or more and there is
#some rotation, or "circular shift," of that sequence that first increases
#and then decreases. A "circular shift" is one where you remove numbers from
#one end of the list and introduce them in the same order on the other.
#Example:
#   [1,3,5,6,2] to [3,5,6,2,1] to [2,1,3,5,6]
#With this notion in mind, [5,8,9,7,4,3,1,2] is biotic, because rotating the
#sequence yields [1,2,5,8,9,7,4,3], which increases steadily from 1 to 9 and
#then decreases steadily back to 3. On the other hand, [1,3,12,4,2,10] is not
#biotic.
#Write a function that returns True if its arguement, L (a list or tuple of
#integers), is biotic, and False otherwise. You may assume all the elements
#of L are unique positive integers. Note also that there is no need to
#actually rotate L: it is sufficient to scan L and count how many times the
#sequence "changes direction." The only caveat is that you must remember to
#also check for a change in direction between the last and the first elements
#to account for the whole "rotation" idea. YOur solution should use the
#appropriate iterative form of your choice.

#My solution is not even near correct, so I will not write it here.

#Solution
def biotic(L):
    if len(L) < 2:
        return(False)
    count = 0
    for i in range(len(L)):
        if L[i-2] < L[i-1] != L[i-1] < L[i]:
            count = count + 1
        return(count ==2)






#Problem 3
#Write a recursive function digitSum(N) which takes an integer, N, and returns
#its digit sum, also, an integer. The digit sum is computed by summing the
#digits in an integer repeatedly until you're down to just one digit.
#Example:
#   34 is 3+4 is 7
#   520538 is 5+2+0+5+3+8 is 23 is 2+3 is 5

# Note: Solution must be recursive, although you may use a comprehension
# if you find that useful.

#My Solution
#def digitSum(N):
    #N = str(N)
    #if (len(N)==1):
        return(N)
    #else:
        #N=sum([int(x) for x in N])
        #return digitSum(N)
#this lowkey actually works except it returns a value as a string instead
#of an integer

#Solution#1
#def digitSum(N):
    #if N < 10:
        #return(N)
    #return digitSum(N%10 + N//10)

#Solution#2
def digitSum(N):
    if N < 10:
        return(N)
    return digitSum(sum([int(d) for d in str(N)]))
    


        

    
