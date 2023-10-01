# CS1210 Homework2
#
# This file should contain only your own work; there are no partners
# assigned or permitted for Homework assignments.
#
# I certify that the entirety of this file contains only my own work.
# I have not shared the contents of this file with anyone in any form,
# nor have I obtained or included code from any other source aside
# from the code contained in the original homework template file.
import sys
from datetime import datetime, timedelta

######################################################################
# Edit the following function definition so it returns a list
# containing a single string, your hawkid.
######################################################################
def hawkid():
    return(["glflores"])

######################################################################
# In this assignment, we'll be implementing the m-index calculation
# described in the associated reading. Like for HW1, much of the
# design work has already been done. Here, you'll implement some
# individual functions that, when assembled together, provide a final
# solution.
#
# There are a total of seven functions: six "utilities" that compute a
# little piece of the puzzle, and one "driver" that manages the
# overall computation. This file contains signatures for each file and
# explanations for how they function. You will need to complete each
# function. For the "driver" function, scanMeals(), you will need to
# replace the string 'FIXME' with the appropriate code wherever you
# find it.
#
######################################################################
# mIndex(D) computes the meal index from a dictionary, D, containing
# keys that correspond to subject ids and values corresponding to the
# number of meals consumed together. It returns an integer meal index.
#
# Implicit here is the fact that D is a record of the number of times
# an individual has swiped into the dining hall with the individuals
# identified by the keys of D. Note that you don't actually know the
# identifier of the individual D belongs to, but you do know the
# identifiers of the people he/she has swiped through with. So if D
# is: {26:5, 104:1, 117:1, 55:8, 142:5, 61:3}, it it means this
# indivudal has eaten 5 meals with #26, 1 meal with #104, 1 meal with
# #117, and so on. From this D we need to compute this person's
# m-index.
#
# To compute the m-index, construct a sorted (from largest to
# smallest) list of the values from D and return the largest index
# that is less than or equal to its corresponding (sorted) value.
# Careful! m-indexes rely on 1-indexed reasoning, even though Python
# is still 0-indexed; you will have to make some adjustments to get it
# right.
# 
# Example:
#   >>> mIndex({26:5, 104:1, 117:1, 55:8, 142:5, 61:3})
#   3
#   >>> mIndex({1452:14, 132:8, 98:1, 731:10, 64:2, 18:17, 244:4, 4:1, 445:2})
#   4
#
# For the first example above, the sorted counts (the dictionary
# values) are [8, 5, 5, 3, 1, 1]. We see that for i=3, the
# corresponding value (remember, 1-indexed, so 5) is greater than the
# index i, but for i=4, the corresponding value (again, 1-indexed, so
# 3) is no longer greater than the index i: hence, the m-index is 3,
# the largest index whose corresponding value that exceeds the index
# value.
#
def mIndex(D):
    D = sorted(D.values())[::-1] 
    for i in range(0,len(D)):
        if i<=D[i]:
            mIndex = i
    return mIndex
# it works, check efficiency

######################################################################
# parseRecord(record) takes a record, or list, of three strings read
# from a line in the input file, representing the timestamp, the sid
# (i.e., student identifier), and dining location, respectively.
#
# It returns an event, represented as a dictionary of three
# key/values: loc (the dining location as a string), time (the
# timestamp as an instance of the datetime object), and the sid (an
# integer student id).
#
# This function isn't particularly hard, because it mostly involves
# familiar type conversions. But dealing with dates and times is
# always tricky and ugly! Here, you will need to take a string that
# looks something like:
#    "8/22/2015 7:55"
# and return a datetime object. Fortunately, datetime.strptime() can
# be used to make this conversion, but you will have to first read and
# understand the Python documentation for datetime available here:
#    https://docs.python.org/3/library/datetime.html
# So:
#    >>> parseRecord(["8/22/2015 7:55", "08042950", "Barnett Cafe"])
#    {'loc':'Barnett Cafe', 'time':datetime.datetime(2015, 8, 22, 7, 55), 'sid':8042950}
#
# You will note that the datetime class has been imported for you from
# the datetime module, so datetime.strptime() refers to the strptime()
# method of the datetime class imported from the datetime module.
#
def parseRecord(record):
    return {"loc":record[2],"time":datetime.strptime(record[0], "%m/%d/%Y %H:%M"),"sid":int(record[1])}
#definitely good  

######################################################################
# manageWindows(W, event, delta) takes a dictionary of sliding windows
# W, indexed by dining hall location, where the values are lists
# maintained in sorted timestamp order containing dining events that
# occur within delta time of the last event.  Here, delta is an object
# of type timedelta, also from the datetime module, used for
# parseRecord().
#
# The W dictionary is one of the important data structures in this
# assignment. The keys are dining halls, and the values are ordered
# lists of events, where each event corresponds to a card swipe. We
# will maintain these lists in order exploiting the fact that the data
# we are given are already in sorted order. The trick to the lists is
# that we will only keep events that span an interval of time, an
# input parameter. So, for example, if the input interval is 4
# minutes, only the "last" 4 minutes of swipe card data will be kept
# in that window: thus the window "slides" forward in time as we
# process events.
#
# So as you process an event, you will need to add it to the end of
# the appropriate sliding window in W, and then remove any events from
# the beginning of that sliding window that have "aged out" according
# to the specified time interval delta, a timedelta object instance.
#
# We'll worry about constructing the timedelta object instance later,
# but for now, assume it is passed in appropriately, and know that you
# can do simple subtraction on datetime objects to get time intervals,
# which are represented as instances of timedelta objects. That means
# you can do things like ask if time1-time2<delta and expect to get a
# Boolean in return.
#
# Modifies W and returns the specific value of W (a sliding window)
# corresponding to the location of the event just processed.
#
# So, assuming a 4 minute window size, and an initially empty W:
#   >>> W={}
#   >>> manageWindows(W, parseRecord(["8/22/2015 7:55", "08042950", "Barnett Cafe"]), timedelta(minutes=4))
#   [{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 7, 55), 'sid': 8042950}]
#   >>> W
#   {'Barnett Cafe': [{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 7, 55), 'sid': 8042950}]}
#   >>> manageWindows(W, parseRecord(["8/22/2015 8:12", "00055531", "Barnett Cafe"]), timedelta(minutes=4))
#   [{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 8, 12), 'sid': 55531}]
#   >>> W
#   {'Barnett Cafe': [{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 8, 12), 'sid': 55531}]}
#   >>> manageWindows(W, parseRecord(["8/22/2015 8:15", "03134259", "Barnett Cafe"]), timedelta(minutes=4))
#   [{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 8, 12), 'sid': 55531}, 
#    {'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 8, 15), 'sid': 3134259}]
#   >>> W
#   {'Barnett Cafe': [{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 8, 12), 'sid': 55531},
#                     {'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 8, 15), 'sid': 3134259}]}
#
# Example Event: {'loc':'Barnett Cafe', 'time':datetime.datetime(2015, 8, 22, 7, 55), 'sid':8042950}

# passes tests 
 
def manageWindows(W, event, delta):
    locationKey = event["loc"]
    #corner case 
    if locationKey not in W:
        W[locationKey] = [event]
    else:
        for i in W[locationKey]:
            if event["time"]-i["time"]>delta:
                del(W[locationKey][0])      
        W[locationKey].append(event)
    return W[locationKey]
#good, but check efficiency  

######################################################################
# newWeek(old, new) takes two events (like those produced by
# parseRecord()) and returns True if and only if event new represents
# a "new week" with respect to event old.
#
# We define "new weeks" as beginning on a Monday, so whenever the new
# event occurs on or following at least one intervening Monday after
# old.
#
# So, a Sunday->Monday transition between old and new returns True,
# and so should a Friday->Tuesday transition (i.e., as if a dining
# hall was closed Saturday through Monday, so no swipes on those
# days).
#
# Note that by definition, the very first event in the file represents
# a new week, so be sure to handle the particular corner case where
# new is the first record and old is something else.
#
# This function will require some thought about the logic, as well as
# some tinkering with datetime arithmatic.

# Piecing things together:
#
# corner case - "old" starts as an empty dictionary {}
#
# weekday() - We can use this method to determine what day of the week it
# is. 0 - Monday, 1 - Tuesday, 2 - Wednesday, 3 - Thursday, 4 - Friday,
# 5 - Saturday, 6 - Sunday
#
# logic -   True if old is larger than new
#           True if difference of days from old to new is >= 7


# Example events:
#   {'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 7, 55), 'sid': 8042950} #starting with Saturday
#   {'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 8, 00), 'sid': 8042951} #still Saturday, different time
#   {'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 23, 8, 00), 'sid': 8042952} #Sunday
#   {'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 24, 8, 00), 'sid': 8042953} #Monday
#   {'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 25, 8, 00), 'sid': 8042954} #Tuesday
#   {'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 9, 5, 8, 00), 'sid': 8042955}  #next week Saturday
#   
# Examples:
#   >>> newWeek({'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 7, 55), 'sid': 8042950},{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 8, 00), 'sid': 8042951})
#   False
#   >>> newWeek({'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 7, 55), 'sid': 8042950},{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 23, 8, 00), 'sid': 8042952})
#   False
#   >>> newWeek({'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 7, 55), 'sid': 8042950},{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 24, 8, 00), 'sid': 8042953})
#   True
#   >>> newWeek({'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 23, 8, 00), 'sid': 8042952},{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 25, 8, 00), 'sid': 8042954})
#   True
#   >>> newWeek({'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 7, 55), 'sid': 8042950},{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 9, 5, 8, 00), 'sid': 8042955})
#   True

# Example events (redone because of attribute error to datetime):
#   parseRecord(["8/22/2015 7:55", "08042950", "Barnett Cafe"]) #starting with Saturday
#   parseRecord(["8/22/2015 8:00", "08042950", "Barnett Cafe"]) #still Saturday, different time
#   parseRecord(["8/23/2015 7:55", "08042950", "Barnett Cafe"]) #Sunday
#   parseRecord(["8/24/2015 7:55", "08042950", "Barnett Cafe"]) #Monday
#   parseRecord(["8/25/2015 7:55", "08042950", "Barnett Cafe"]) #Tuesday
#   parseRecord(["9/5/2015 7:55", "08042950", "Barnett Cafe"])  #next week Saturday
#
# Examples:
#   >>> newWeek(parseRecord(["8/22/2015 7:55", "08042950", "Barnett Cafe"]),parseRecord(["8/22/2015 8:00", "08042950", "Barnett Cafe"])) #Saturday to Saturday(different time)
#   False
#   >>> newWeek(parseRecord(["8/22/2015 7:55", "08042950", "Barnett Cafe"]),parseRecord(["8/23/2015 7:55", "08042950", "Barnett Cafe"])) #Saturday to Sunday
#   False
#   >>> newWeek(parseRecord(["8/22/2015 7:55", "08042950", "Barnett Cafe"]),parseRecord(["8/24/2015 7:55", "08042950", "Barnett Cafe"])) #Saturday to Monday
#   True
#   >>> newWeek(parseRecord(["8/23/2015 7:55", "08042950", "Barnett Cafe"]),parseRecord(["8/25/2015 7:55", "08042950", "Barnett Cafe"])) #Sunday to Tuesday
#   True
#   >>> newWeek(parseRecord(["8/22/2015 7:55", "08042950", "Barnett Cafe"]),parseRecord(["9/5/2015 7:55", "08042950", "Barnett Cafe"]))  #Saturday to Saturday(next week)
#   True #fails this test
#
# Corner Case Example:
#   >>> newWeek({},parseRecord(["8/22/2015 7:55", "08042950", "Barnett Cafe"]))
#   True

def newWeek(old, new):
    # accounting for corner case
    if old=={}:
        return True
    else:
        # variable assignments 
        old_time = old["time"]
        new_time = new["time"]

        # basic solution 
        return  (old_time.weekday()>new_time.weekday()) or (new_time-old_time>=timedelta(days=7))
#definitely good 

######################################################################
# endWeek(M, C) is called when we just prior to processing the first
# event of each new week, as well as when we are done processing the
# file (think of the corner case when you process the last event: the
# "next" event, which does not exist, is assumed to represent a "new
# week").
#
# endWeek() manipulates the other two important internal data
# structures C and M, where both of these, like W, are dictionaries.
#
#   C is a dictionary indexed by sid (student id) of dictionaries,
#     also indexed by sid, where C[sid1][sid2] keeps track of how many
#     swipes within the defined time interval occur between sid1 and
#     sid2, and C[sid2][sid1] keeps the same information for
#     sid2. You'll see later why its convenient to replicate these
#     numbers in a symmetric way later. For now, think of this as a 2
#     dimensional matrix that is sparsely populated (so dictionaries
#     require less storage than nested lists). So part of C might look
#     like: { 2169529:{ 2989659:1, ...}, ..., 2989659:{ 2169529:1,
#     ...} } if 2169529 and 2989659 had swiped once within the
#     interval.
#   Better Example:
#   {sid1:{sid2:1},sid2:{sid1:1}}
#
#   M is also a dictionary indexed by sid (student id) with values
#     that are lists of m-indexes, where each element of that list
#     corresponds to the cumulative m-index calculated at the end of
#     the week. So M might look like { 2169529:[1], 2989659:[1], ...}
#     after processing the first week of data.
#
# endWeek() steps through all the sid's in M and appends a new m-index
# value to M[sid] corresponding to the m-index computed on the data
# collected so far in C[sid], which, not coincidentally, has exactly
# the format required by the mIndex() function defined previously.
#

# Piecing things together:
#   First, we have to calculate the m index for each student. We do this
#   by using the value C[sid] and inputing it into the mIndex() function.
#   Second, we append this m index to the student in M.
#
# corner case - not accounted for!!!
# also, I'm not really sure what the corner case would be?

# Examples:
#   >>> C = {1:{2:5,3:1},2:{1:5,3:2,4:3},3:{1:1,2:2},4:{2:3}} # 1-1, 2-2, 3-1, 4-0
#   >>> M = {1:[1,2,3],2:[],3:[9],4:[]} 
#   >>> endWeek(C,M)
#   {1:[1,2,3,1],2:[2],3:[9,1],4:[0]}
#
# Corner Case Example:
# >>>

def endWeek(C, M):
    for x in C:
       M[x].append(mIndex(C[x]))
    return 
 
# Doesn't account for corner case!!!
# Otherwise, good. 

######################################################################
# dumpOutput(M, header) is called only once, at the end of
# processing. It's job is to produce comma-separated output consisting
# of (1) the header, and then (2) a series of rows where each row
# consists of an sid followed by its weekly m-indexes. The m-indexes
# are montonically increasing: one per week in the data (where week is
# defined as starting on Monday; see newWeek() above).
#
# Everything you will need to dump is contained in either the M data
# structure or the header string. If everything's gone right, the
# header will have the same number of comma-separated entries as each
# and every one of the rows that follow. 
#
# One final note: for a final touch, make sure the sid is printed out
# with exactly 8 digits, packed with leading 0's. You'll need to read
# up on the format() method for strings.
#
# Examples:
#   >>> header = "sid,week1,week2,week3"
#   >>> M = {1:[5,5,3],2:[4,5,8],3:[2,8,3],4:[5,6,6],5:[2,4,6]}
#           # this should work out montonically for the actual data
#   >>> dumpOutput(M,header)

def dumpOutput(M, header):
    print(header)
    for sid in sorted(M):
        print(sid, end='')
        for m in M[sid]:
            print(","+str(m),end='')
        print()
    return
#good 

######################################################################
# scanMeals(filename, wsize=4) opens the specified file, containing
# comma-separated values, reads the content (a list of dining hall
# swipes), and constructs internal data structures (actually, the
# three dictionaries W, C and M described above), along with the
# header (a string) from which we can produce the desired output (see
# dumpOutput()).
#
def scanMeals(filename='test.csv', wsize=2, W={}, C={}, M={}, header='SID'):
    # First, create a timedelta object instance that reflects the
    # specified window size (expressed in minutes). We'll use this
    # interval to regulate the window size at each dining location.
    delta = timedelta(minutes=wsize) 

    # OK, open the speficied file for reading.
    with open(filename, 'r') as f:
        # We're going to keep track of a few things as we scan the
        # records, including how many weeks of data we read (see
        # newWeek() above, where a new week is defined as starting on
        # or after the following Monday).
        week = 0

        # Also we'll initialize a variable that will always contain
        # the previous record; each time through the loop, we update
        # old to contain the current record. At the outset, old is
        # simply an empty dictionary, since the first record does not
        # have a corresponding previous record.
        old = {}

        # The header will be the first line of our output comma-separated
        # value file, and will label the columns of data. The leftmost
        # column will be the student id for the output record, and it will
        # be followed by a number of weekly m-index values. As we parse
        # the data and encounter a new week, we'll append the date of the
        # first day of the new week to header in order to label the new
        # column of data.
        header = 'SID'

        # Read each row/
        for line in f:
            # Turn the line into a list of three substrings by
            # breaking it apart at the commas, making sure to get rid
            # of any trailing newlines or similar.
            line = line.rstrip().split(",")

            #Use parseRecord()
            # to create the current event, which we'll call new.
            new = parseRecord(line) #FIXME
            #   >>> parseRecord(["8/22/2015 7:55", "08042950", "Barnett Cafe"])
            #   {'loc':'Barnett Cafe', 'time':datetime.datetime(2015, 8, 22, 7, 55), 'sid':8042950}
            
            # Does this new record refer to a previously unseen sid?
            # If so, create a new entry for it in M, being sure to pad
            # the value with enough 0's to reflect the m-indexes for
            # the weeks we've already processed (this is what that
            # week counter is for!).
            if new['sid'] not in M:
                M[new['sid']] = [0]*week #FIXME

            # Before we process this new record, does it represent a
            # new week?
            if newWeek(old, new):
                # Update the header. Each week's date should appear as
                # yyyy-mm-dd, so you'll need to study the strftime()
                # method of the datetime object. Finally, note that
                # header "grows" at the beginning of each new week, so
                # it "leads" data collection.
                header = header + ',' + new["time"].strftime("%Y-%m-%d") #FIXME

                # Now unless this is the very first record in the
                # file, update the M dictionary values with
                # the cumulative m-indexes for each sid up to this
                # point. Note that the list of M values "grows" at the
                # end of each old week, so it "lags" the header.
                if old != {}:
                    # Accumulate the last week's m-index data and
                    # append it to the corresponding M record.
                    endWeek(C,M) #FIXME
                    week = week + 1 #FIXME

            # Process the new event by adding it into the appropriate
            # window.  Recall manageWindows() returns the
            # appropriately updated window with the new event, which
            # we can now use to update C.
            window = manageWindows(W, new, timedelta(minutes=wsize)) #FIXME

            # Now for each subject j in the updated window, increment
            # both C[new['sid']][j] and C[j][new['sid']] by one, representing
            # the shared meal.

            # First, is new['sid'] in C? If not, initialize.
            if new['sid'] not in C:
                C[new['sid']] = {} #FIXME 

            # Recall window is a list of events, where the last event
            # in the window is the event we are presently processing.
            #   [{'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 8, 12), 'sid': 55531}, 
            #    {'loc': 'Barnett Cafe', 'time': datetime.datetime(2015, 8, 22, 8, 15), 'sid': 3134259}]
            for j in [ event['sid'] for event in window ]:
                #print("trying {} {}".format(id, j)) C[j] must already
                # exist by construction, but is does sid exist in
                # C[j]?
                if new['sid'] not in C[j]:
                    C[j][new['sid']] = 0 #FIXME
                C[j][new['sid']] += 1 #FIXME
                # Now handle the other direction of this meal edge. Is
                # C[new['sid']][j] new?
                if j not in C[new['sid']]:
                    C[new['sid']][j] = 0 #FIXME
                C[new['sid']][j] += 1 #FIXME

            # Update retain current row as old and iterate, reading a
            # new row.
            old = new

    # No more data, so the current week is complete: compute the final
    # m-index values.
    endWeek(C,M) #FIXME

    # Dump the output.
    dumpOutput(M,header)

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
######################################################################
# Allows you to invoke this file from the Unix/Mac command line,
# giving the name of the data file and the desired interval, in
# minutes, as follows:
#   % python hw2soln.py test.csv 3 > output.csv
#
#if __name__ == '__main__':
    #scanMeals(sys.argv[1], int(sys.argv[2]))
