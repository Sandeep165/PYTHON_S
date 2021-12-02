'''

Create a function which takes a list of objects from the class IceCream and returns the sweetness value of the sweetest icecream.
 Note that there is a class is provided for you in the Tests tab.

class IceCream:
  def __init__(self, flavor, num_sprinkles):
    self.flavor = flavor
    self.num_sprinkles = num_sprinkles


Each sprinkle has a sweetness value of 1
Check below for the sweetness values of the different flavors.
Flavors 	Sweetness Value
Plain	        0
Vanilla     	5
ChocolateChip	5
Strawberry  	10
Chocolate	    10
Examples
ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanilla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8
sweetest_icecream([ice1, ice2, ice3, ice4, ice5]) ➞ 23

sweetest_icecream([ice3, ice1]) ➞ 23

sweetest_icecream([ice3, ice5]) ➞ 17


'''

class IceCream:
  def __init__(self, flavor, num_sprinkles):
    self.flavor = flavor #1
    self.num_sprinkles = num_sprinkles #1

ice1 = IceCream("Chocolate", 13)         # value of 23
ice2 = IceCream("Vanilla", 0)           # value of 5
ice3 = IceCream("Strawberry", 7)         # value of 17
ice4 = IceCream("Plain", 18)             # value of 18
ice5 = IceCream("ChocolateChip", 3)      # value of 8



flavor_dict = {
        "Plain": 0,
        "Vanilla" :5,
        "ChocolateChip":5,
        "Strawberry" : 10,
        "Chocolate" : 10
    }

def sweetest_icecream(lst):
    return max(flavor_dict[i.flavor] + i.num_sprinkles  for i in lst)


sweetest_icecream([ice2,ice1,ice5])   # 23

'''
ice2  ->  vanila, 0

ice2.flavor -> vanila
ice2.num_sprinkle -> 0


max(flav_dict[vanila] + 0)
max(flav_dict[vanila] + 0)
max(5 + 0)
max(5 ,15,25)
25

'''
'''
linear :- 
stack
queue
linklist

ques/ans or tests


non linear ds :-
graphs
B
B+
Binary search tree
red black tree

keys = 12,2,3,5,9,7,11,16


insertion
updation 
deletion -> balancing

ques/ans or tests


DBMS:-
theory :
practicals based one queries
DDL,DML

ques/ans or test

mini proj


'''