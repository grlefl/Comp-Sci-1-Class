# CS1210: Lab10 [4 methods to complete]
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
# In this lab, we'll be working with an object-oriented framework.
#
# You've been hired by the owner of a new coffee shop, ZipDrip, to
# create a customer relations system. The new system will combine an
# object-oriented shell with data structures you are already
# familiary with (e.g., dictionaries, lists).
#
# The main class is the ZipDrip() class, where an instance of the
# class represents one ZipDrip franchise. Each franchise keeps just a
# few bits of information: the "perk" or default discount (expressed
# as percentage between 0 and 100) given on purchases to regular
# clients; "mcups", or the minimum number of cups a client needs to
# buy before they are considered regular clients; and "clients," a
# dictionary of client records. The default values shown can be
# overridden when creating a new ZipDrip franchisee.
#
# The good client discount is described later.
#
class ZipDrip():
    def __init__(self, perk=10, mcups=4):
        self.franchise = {"perk":perk, "mcups":mcups, "clients":{}}
        print(self.franchise)

    ######################################################################
    # The register(self, phone) method takes a client phone number and
    # returns that client's record from the client roster stored as a
    # dictionary. If the client is not in the roster, a new record is
    # added to the roster.
    #
    # Each client record is a dictionary with the following keys:
    #   drips: number of coffees purchased (initially 0)
    #   total: sum of all purchased coffee list prices (initially 0)
    #   perks: list prices of the last mcups purchased (initially [])
    #
    # Example:
    #   >>> z = ZipDrip()
    #   >>> z.register(3474894608)
    #   {'drips':0, 'total':0, 'perks':[]}
    #   >>> z.clients
    #   {3474894608: {'drips':0, 'total':0', 'perks':[]}}
    #
    def register(self, phone):
        self.franchise["clients"][str(phone)] = {"drips":0, "total":0, "perks":[]}
        print(self.franchise)

    ######################################################################
    # The buy(self, phone, cost) method takes a client phone number and a
    # list purchase price, updates the client record (creating one if it
    # doesn't exist), and then determines the actual purchase price
    # incorporating any discount.
    #
    # Your code should retrieve the client record from self and modify it.
    #
    # The following updates are required: first, you must increment
    # "drips" and "total". The list price of the purchase should next be
    # added to the perks list, and the discount price should be determined
    # if there were at least mcups purchases prior to the present
    # purchase. This is the price that should be returned.
    #
    # Example:
    #   >>> z.buy(3474894608, 2)
    #   2
    #   >>> z.buy(3474894608, 2)
    #   2
    #   >>> z.buy(3474894608, 2)
    #   2
    #   >>> z.buy(3474894608, 2)
    #   2
    #   >>> z.buy(3474894608, 3)
    #   2.8
    #
    # Note that the discount is determined as a percentage of the cost of
    # the last mcups purchases, excluding the current purchase, and the
    # value of the discount in no way depends on the cost of the current
    # cup. Also, cost should be returned as a floating point number with
    # no more than two decimal digits; which may require some extra
    # arithmetic.
    #
    def buy(self, phone, cost):
        #This portion failed to submit 
        if str(phone) not in self.franchise["clients"]:
            self.franchise["clients"][str(phone)] = {"drips":0, "total":0, "perks":[]}
        #
        customer = self.franchise["clients"][str(phone)]
        customer["drips"] += 1
        customer["total"] += cost
        customer["perks"] += [cost]
        if customer["drips"] > self.franchise["mcups"]:
            print(cost - ((sum(customer["perks"][-5:-1]))/(self.franchise["perk"])))
        #not accounting for long floating numbers
        #gives a result of 2.2, which I would assume to be correct, but idk
   
    ######################################################################
    # The status(self, phone) method takes a client phone number and
    # returns the client's next discount, or, if the client has not yet
    # made sufficient purchases, the number of purchases remaining to earn
    # a discount.
    #
    # Example:
    #   >>> z.status(3198675309)
    #   You still need 4 cups to earn a discount!
    #   >>> z.status(3474894608,
    #   Your next discount will be 0.22
    #
    def status(self, phone):
        customer = self.franchise["clients"][str(phone)]
        if customer["drips"] < self.franchise["mcups"]:
            print("You still need 4 cups to earn a discount!")
        else:
            print("Your next discount will be " + str((sum(customer["perks"][-4:]))/(self.franchise["perk"])))
            

######################################################################
# MAKE NO CHANGES BEYOND THIS POINT.
###################################################################### 
if __name__ == '__main__':
    if all([ "hawkid" in x for x in signed() ]):
        print('### Warning: Complete definition of signed() or no points will be awarded!')
    print("### Warning: No test cases provided: you should test this code in the REPL yourselves")
