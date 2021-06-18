#floor division   you will get lower bound values
#ceiling values   you will get higher bound values
num1 = 17
num2 = 10
# print(num1/num2)
# print(num1//num2)

import math
from typing import List

# print(math.floor(-23.12)) #-24 
# print(math.floor(400.15)) #400
# print(math.floor(400.70)) #400

# print(math.ceil(-23.12))  #-23
# print(math.ceil(400.15))  #401
# print(math.ceil(400.70))  #401



# -5 -4 -3 -2 -1 0 1 2 3 4 5
# string [start:end:step]

string = "India and USA"
# print(string[:5])  #India
# print(string[10:])  #USA

# string1 = "I live in Mumbai"
# print(string[::-1])  #-1 -2 -3 -4  

# name = input("Enter the name:- ")

# if (name == name[::-1]):
#     print("Given string is a palindrome")
# else:
#     print("Given string is not a palindrome")
print(string.count("India"))
print(string.islower())


fruit = "   apple     "
print(fruit)
print(fruit.rstrip())


'''

string methods:-

capitalize()	Converts the first character to upper case
casefold()  	Converts string into lower case
center()    	Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()    	Returns an encoded version of the string
endswith()  	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()    	Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isdecimal()	    Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()   	Returns True if all characters in the string are lower case
isnumeric()	    Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()          Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()    	Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()	        Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()     	Returns a trimmed version of the string
swapcase()  	Swaps cases, lower case becomes upper case and vice versa
title()     	Converts the first character of each word to upper case
translate() 	Returns a translated string
upper()	        Converts a string into upper case
zfill()	        Fills the string with a specified number of 0 values at the beginning
'''


#List :- [0......n-1]
'''
1) capable to hold multiple data type
2) Duplications are allowed inside the list
3) List mutable data type
4) Orderd, changable and duplication are allowed
'''

my_list = [1,2,3,"Pune","Mumbai",True,False,15.5,1,2,3]

print(my_list[-1])

print(len(my_list))  #11(1---n)

print(my_list[len(my_list)-1])

print(type(my_list))

print(my_list[0:3])


