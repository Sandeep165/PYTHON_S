'''
A built-in timer inside your car can count the length of your ride in minutes and you have started your ride at 00:00.

Given the number of minutes n at the end of the ride, calculate the current time. 
Return the sum of digits that the digital timer in the format hh:mm will show at the end of the ride.

Examples
car_timer(240) ➞ 4
# 240 minutes have passed since 00:00, the current time is 04:00....0+4+0+0...4
# Digits sum up is 0 + 4 + 0 + 0 = 4

car_timer(808) ➞ 14......hh:mm........h+h+m+m......

car_timer(14) ➞ 5................hh:mm.......00:14......0+0+1+4....5
car_timer(72) ➞ 4................hh:mm.......01:12......0+1+1+2..4


'''
# def sumDigit(n):
#     temp= 0
#     while(n):
#         temp += n%10
#         n //= 10
#     return temp

# def car_timer(n):
#     hour= n // 60
#     minutes= n - hour*60
#     return sumDigit(hour) + sumDigit(minutes)

# print(car_timer(808))

def add(n):
    return sum(map(int,str(n//60)+str(n%60)))


'''
Create a function that takes two parameters and, if both parameters are strings, add them as
 if they were integers or if the two parameters are integers, concatenate them.

Examples
stupid_addition(1, 2) ➞ "12"

stupid_addition("1", "2") ➞ 3

stupid_addition("1", 2) ➞ None
Notes
If the two parameters are different data types, return None.
All parameters will either be strings or integers.




In each input list, every number repeats at least once, except for two. Write a function that returns the two unique numbers.

Examples
return_unique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]

return_unique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]

return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]
Notes
Keep the same ordering in the output.
'''

def myFunc(a, b):
    if(type(a) is int and type(b) is int): return str(a)+str(b)
    elif(type(a) is str and type(b) is str): return int(a) + int(b)
    return "None"
    
print(myFunc(1, 2))




def add(a,b):
    if type(a)==type(b):
        if type(a) == int:
            return str(a) + str(b)
        return int(a)+int(b)

    
def return_unique(lst):
    ans= []
    for element in lst:
        if(lst.count(element) == 1):
            ans.append(element)
    return ans


def sample(lst):
    return [i for i in lst  if lst.count(i)==1]




# fruits = ["apple","banana","cheery","grapes"]
# f1 = []
# f1 = [i=="e" for i in fruits ]
# # print(f1)
# # for i in fruits:
# #     if "e" in i:
# #         f1.append(i)
# # print(f1)
