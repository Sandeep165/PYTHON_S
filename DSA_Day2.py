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

# class book:
#     # constructor (self,title,author)
#     # get title :- "Title: " + the instance title.
#     #get author

# PP = book("Pride and Prejudice" ,"Jane Austen" )
# H = 
# WP = 



'''


Create a class that takes the following four arguments for a particular football player:

name
age
height
weight
Also, create three functions for the class that returns the following strings:

get_age() returns "name is age age"
get_height() returns "name is heightcm"
get_weight() returns "name weighs weightkg"
Examples
 p1 = player("David Jones", 25, 175, 75)

 p1.get_age() ➞ "David Jones is age 25"
 p1.get_height() ➞ "David Jones is 175cm"
 p1.get_weight() ➞ "David Jones weighs 75kg"





Create a Person class which will have three properties:

Name
List of foods they like
List of foods they hate
In this class, create the method taste():

It will take in a food name as a string.
Return {person_name} eats the {food_name}.
If the food is in the person's like list, add 'and loves it!' to the end.
If it is in the person's hate list, add 'and hates it!' to the end.
If it is in neither list, simply add an exclamation mark to the end.
Examples
p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"

p1.taste("cheese") ➞ "Sam eats the cheese!"

p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"

'''

class Person:
    def __init__(self,name,like_list = [],hate_list = []):
        self.name=name
        self.like_list=like_list
        self.hate_list=hate_list
    

    def taste(self,item):
        if item in self.like_list:
            return f"{self.name} Eat {item} and Loves it!"
        elif item in self.hate_list:
            return f"{self.name} Eat {item} and Hate it!"
        else:
            return f"{self.name} Eat the {item}!"

p=Person('Sam',['ice cream','cake'],['carrot'])
print(p.taste('cake'))
print(p.taste('ice cream'))
print(p.taste('carrot'))
print(p.taste('cheese'))


class person:
    def __init__(self,name,like_list,hate_list):
        self.name = name
        self.like_list = like_list
        self.hate_list = hate_list

    def taste(self,item):
        if item in self.like_list:
            print(self.name + " Likes " + item + "and loves it!")
        elif item in self.hate_list:
            print(self.name + " Hates " + item + "and hates it!")
        else:
            print(self.name + item + "!")


    
p1 = person('Peter', ["sandwitch","samosa"], ["carrot"])

p1.taste("sandwitch")
p1.taste("roti")

