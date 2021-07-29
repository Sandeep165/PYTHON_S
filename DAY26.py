'''

Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and
 returns a dictionary of objects like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
Notes
'''


def top_note1(dict1):
    name = dict1["name"]
    top_note = max(dict1["notes"])
    return ({"name":name , "top_note":top_note})

'''




Write a function that takes a list of two numbers and determines if the sum of the digits in each number are equal to each other.

Examples
is_equal([105, 42]) ➞ True
# 1 + 0 + 5 = 6
# 4 + 2 = 6

is_equal([21, 35]) ➞ False

is_equal([0, 0]) ➞ True


'''
# def sum_digits(n):
#     sum= 0
#     while(n):
#         sum += n%10
#         n //= 10
#     return sum

# myList= [105, 43]
# print("True") if(sum_digits(myList[0]) == sum_digits(myList[1])) else print("False")



'''

Given a list of even length, copy the half with the higher sum of numbers to the other half of the list. 
If the sum of the first half equals the sum of the second half, return the original list.

Examples
balanced([1, 2, 4, 6, 3, 1]) ➞ [6, 3, 1, 6, 3, 1]
# 1 + 2 + 4 < 6 + 3 + 1 sol = [6, 3, 1, 6, 3, 1]

balanced([88, 3, 27, 5, 9, 0, 13, 10]) ➞ [88, 3, 27, 5, 88, 3, 27, 5]
# 88 + 3 + 27 + 5 > 9 + 0 + 13 + 10  sol = [88, 3 ,27 ,5 ,88 ,3 ,27 ,5]

balanced([7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]) ➞ [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]
# 7 + 5 + 2 + 6 + 1 + 0 = 1 + 5 + 2 + 7 + 0 + 6 sol =  [7, 5, 2, 6, 1, 0, 1, 5, 2, 7, 0, 6]
Notes
The length of the list is even.
'''
def balanced(lst):
    list1 = sum(lst[:len(lst)//2]) #6 lst[0:3]
    list2 = sum(lst[len(lst)//2:]) #6 lst[3:]

    if list1 == list2:
        return lst
    elif list1<list2:
        return lst[len(lst//2):] * 2
    else:
        return lst[:len(lst)//2] *2


#Genrator

def my_genrator(max_num):
    n = 2

    while n<max_num:
        yield n
        n += 2
    # yield n

    # n += 2

    # yield n

    # n += 2
    # yield n

# result = my_genrator(20)
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
for i in my_genrator(20):
    print(i)


# def greet():
#     return "Goood Morninggg..."

# # print(greet())
# a = greet()
# print(a)