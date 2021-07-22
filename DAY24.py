'''
Create a function (named fifth) that takes some arguments and returns the type of the fifth argument.
 In case the arguments were less than 5, return "Not enough arguments".

Examples
fifth(1, 2, 3, 4, 5) ➞ int

fifth("a", 2, 3, [1, 2, 3], "five") ➞ str

fifth() ➞ "Not enough arguments"
'''
# def fifth(*num):
#     x = [i for i in num]
#     if len(x)<5:
#         return "Not enough arguments"
#     else:
#         return type(x[4])

# print(fifth(1,2,3,4,5))
# print(fifth(1,2,3))

# print(fifth(1,2,3,4,"5",6,8,9))
'''
Your job is to create a function, that takes 3 numbers: 
a, b, c and returns True if the last digit of a * b = the last digit of c. 41,25,55...True
Check the examples below for an explanation.

Examples
last_dig(25, 21, 125) ➞ True
# The last digit of 25 is 5, the last digit of 21 is 1, and the last
# digit of 125 is 5, and the last digit of 5*1 = 5, which is equal
# to the last digit of 125(5).

last_dig(55, 226, 5190) ➞ True
# The last digit of 55 is 5, the last digit of 226 is 6, and the last
# digit of 5190 is 0, and the last digit of 5*6 = 30 is 0, which is
# equal to the last digit of 5190(0).

last_dig(12, 215, 2142) ➞ False
# The last digit of 12 is 2, the last digit of 215 is 5, and the last
# digit of 2142 is 2, and the last digit of 2*5 = 10 is 0, which is
# not equal to the last digit of 2142(2).
Notes
Numbers can be negative.

'''


'''
Create a function that takes a list of dictionaries (groceries) which calculates the total price and returns it as a number. A grocery dictionary has a product, a quantity and a price, for example:

{
  "product": "Milk",
  "quantity": 1,
  "price": 1.50
}
Examples
# 1 bottle of milk:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 }
]) ➞ 1.5

# 1 bottle of milk & 1 box of cereals:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Cereals", "quantity": 1, "price": 2.50 }
]) ➞ 4

# 3 bottles of milk:
get_total_price([
  { "product": "Milk", "quantity": 3, "price": 1.50 }
]) ➞ 4.5

# Several groceries:
get_total_price([
  { "product": "Milk", "quantity": 1, "price": 1.50 },
  { "product": "Eggs", "quantity": 12, "price": 0.10 },
  { "product": "Bread", "quantity": 2, "price": 1.60 },
  { "product": "Cheese", "quantity": 1, "price": 4.50 }
]) ➞ 10.4

# Some cheap candy:
get_total_price([
  { "product": "Chocolate", "quantity": 1, "price": 0.10 },
  { "product": "Lollipop", "quantity": 1, "price": 0.20 }
]) ➞ 0.3

'''

'''
Adv python
1)Iterators
2)Genrators
3)closures
4)Decorators

'''
# Iterators....iter()....next()

mylist = [1,2,3,4,5]

iter_obj = iter(mylist)

while(True):
    try:
        elements = next(iter_obj)
        print(elements)
    except StopIteration:
        break


# while(condition:True?False):
#     block code


# item1 = next(iter_obj)
# print(item1)

# item2 = next(iter_obj)
# print(item2)

# item3 = next(iter_obj)
# print(item3)

# item4 = next(iter_obj)
# print(item4)

# item5 = next(iter_obj)
# print(item5)

# item6 = next(iter_obj)
# print(item6)

# set1 = {1,2,3}

# print(type(set1))
# print(set1)

# list1 = list(set1)

# print(type(list1))
# print(list1)