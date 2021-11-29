# Oops
'''

Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class.
 You will make variables (self.ones, self.threes, self.nines) to do this. (n)
 n = 21

 ones = n = 21
 three = int(21/3) = 7 or 7.0
 nines = 21//9 = 2

Examples
n1 = ones_threes_nines(5) 5-3 = 2 
n1.nines ➞ 0

n1.ones ➞ 5


n1.threes ➞ 1
# '''
# class ones_threes_nines:
#     def __init__(self,n):
#         self.one = n
#         self.three = n//3
#         self.nine = n//9
#         print("Good morning !")

# n1 = ones_threes_nines(5)
# print(n1.one)
# print(n1.three)
# print(n1.nine)

# def display(name):
#     print("Good morning")


'''

Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:

"nines:your answer, threes:your answer, ones:your answer"
You need to find out how many ones, threes, and nines it would at least take for the number of each to add up to the given integer 
when multiplied by one, three or nine (depends).

Examples
ones_threes_nines(10) ➞ "nines:1, threes:0, ones:1"

ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"

ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"

'''
# # str 
# class ones_threes_nines:
#     def __init__(self,n):

#         self.answer = "nines: {}, threes: {}, ones: {} ".format(n//9 , n//3, n)

# n1 = ones_threes_nines(5)



'''
Create a class named User and create a way to check the number of users (number of instances) were created, 
so that the value can be accessed as a class attribute.

Examples
u1 = User("johnsmith10")
User.user_count ➞ 1

u2 = User("marysue1989")
User.user_count ➞ 2

u3 = User("milan_rodrick")
User.user_count ➞ 3
Make sure that the usernames are accessible via the instance attribute username.

u1.username ➞ "johnsmith10"

u2.username ➞ "marysue1989"

u3.username ➞ "milan_rodrick"
'''

class User:
    user_count = 0
    def __init__(self,u_name):
        self.username = u_name
        User.user_count += 1

u1 = User("johnsmith10")
print(User.user_count)
u2 = User("marysue1989")
print(User.user_count)


print(u1.username)
print(u2.username)


'''

oops :- java
dsa :- C/C++ ,php

oops

stack
queue
linkedlist

practice que / 1

B tree
B+ tree
Red black

pract que / 1

linear search
quick sort
...

prac que / 1

Dbms
query

projects



'''
'''


Create a Book class that has two attributes:

.title
.author
and two methods:

A method named .get_title() that returns: "Title: " + the instance title.
A method named .get_author() that returns: "Author: " + the instance author.
and instantiate this class by creating 3 new books:

Pride and Prejudice - Jane Austen (PP)
Hamlet - William Shakespeare (H)
War and Peace - Leo Tolstoy (WP)
Name the new instances should be PP, H, and WP, respectively.

For instance, if I instantiated the following book using this Book class:

Harry Potter - J.K. Rowling (HP)
I would get the following attributes and methods:

Examples
HP.title ➞ "Harry Potter"
HP.author ➞ "J.K. Rowling"
HP.get_title() ➞ "Title: Harry Potter"
HP.get_author() ➞ "Author: J.K. Rowling"
'''

class book:
    # constructor (self,title,author)
    # get title :- "Title: " + the instance title.
    #get author

PP = book("Pride and Prejudice" ,"Jane Austen" )
H = 
WP = 