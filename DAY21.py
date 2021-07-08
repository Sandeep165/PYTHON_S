'''
Q1:-  Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other

# Q2:- Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once

Q3:- Write a Python program to compute the greatest common divisor (GCD) and LCD of two positive integers

Q4:-(edabit)
Write a function that returns the number of users in a chatroom based on the following rules:

If there is no one, return "no one online".
If there is 1 person, return "user1 online".
If there are 2 people, return user1 and user2 online".
If there are n>2 people, return the first two names and add "and n-2 more online".
For example, if there are 5 users, return:

"user1, user2 and 3 more online"

Example:- 
chatroom_status([]) ➞ "no one online"

chatroom_status(["paRIE_to"]) ➞ "paRIE_to online"

chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"

chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])
➞ "pap_ier44, townieBOY and 4 more online"


Q5:-(edabit)
Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.

Examples
check([1, 2, 3]) ➞ "increasing"

check([3, 2, 1]) ➞ "decreasing"

check([1, 2, 1]) ➞ "neither"

check([1, 1, 2]) ➞ "neither"

'''
# Q2:- Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once
'''
Method	        Description
seed()	             Initialize the random number generator
getstate()	         Returns the current internal state of the random number generator
setstate()	         Restores the internal state of the random number generator
getrandbits()	    Returns a number representing the random bits
randrange()     	Returns a random number between the given range
randint()	        Returns a random number between the given range
choice()	        Returns a random element from the given sequence
choices()	        Returns a list with a random selection from the given sequence
shuffle()	        Takes a sequence and returns the sequence in a random order
sample()	        Returns a given sample of a sequence
random()	        Returns a random float number between 0 and 1

'''
import random
# print(random.random())
random_number = random.randint(1,10)
# print(random_number)

lst = ["apple","mango","banana"]
# print(lst)
# random.shuffle(lst)
# print(lst)


# res = ".".join(lst)
# print(res)

list1= ['a', 'e', 'i', 'o', 'u']

random.shuffle(list1)
# print("Hit enter to see the diffrent combo:-")
# print("".join(list1))

# def func(a,b,c):
#   if(c>a and c>b and b>a):
#     print("Incresing")
#   elif(a>b and a>c and b>c):
#     print("Decresing")
#   else:
#     print("Neither")
# func(1,1,3)

# def myFunc(list1):
#     dec_count= 0; inc_count= 0
#     for i in range(0, len(list1)-1):
#         if( list1[i] < list1[i+1] ):
#             inc_count += 1
#         else:
#             dec_count += 1
#     if(dec_count == 0):
#         return "Strictly Increasing List"
#     elif(inc_count == 0):
#         return "Strictly Decreasing List"
#     else:
#         return "Neither"

# list1= [9, 8, 7, 6, 10, 4, 3, 2, 1]
# print(myFunc(list1))


# list1=['ABC','abc','DEF','cd','mt','kl']
# n=len(list1)
# if(n==1):
#     print(f'User {list1[0]} is online')
# elif(n==2):
#     print(f'User {list1[0]} and User {list1[1]} are online')
# elif(n>2):
#     print(f'User {list1[0]},{list1[1]} and {n-2} more online')
# else:
#     print('no online')

# def list_num(num):
#     if num==1:
#         print("one user online")
#     elif num==2:
#         print("user1 and user2 online")
#     elif num>=2:
#         print("user1 and user 2 and more online",num-2)
#     else:
#         print("no one online")
# num=int(input("enter num: "))
# list_num(num)

def myFunc(list1):
    if(len(list1) == 0):
        return "no one is online"
    if(len(list1) == 1):
        return f"{list1[0]} is online"
    if(len(list1) == 2):
        return f"{list1[0]} and {list1[1]} are online"

    return f"{list1[0]} {list1[1]} and {len(list1)-2} others are online"

list1= ["user1", "user2", "user3", "user4", "user5"]
list1= ["user1", "user2"]
print(myFunc(list1))
# for num ==2 it will fail

