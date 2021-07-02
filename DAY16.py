# recursion?
'''
def recu():
    # return  result
    rec()


5! = 5*4*3*2*1
4! = 4*3*2*1
'''

# fact=1
# my_var=int(input("Enter a number:"))
# for i in range(1,my_var+1):
#     fact=fact*i

# print(f"Factorial of {my_var} is:",fact)
# n =3

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n-1)   # 3 * 2 * 1  --->6

# lambda func :-

# def mul(a,b,c):
#     return a*b*c
# # print(mul(5,4,8))


# result = lambda a,b,c:a*b*c
# # print(result(5,1,3))

# def func1(n):
#     return lambda a : a*n

# res = func1(5)
# print(res())

# map, filter method

lst = [1,3,2,5,6,8,4,10,12,15,19,85,45,100]
# even = []
# odd = []
# def even_odd(lst):

#     lste=[]
#     lsto=[]
#     def res(n):
#         for i in n:
#             if(i%2==0):
#                 lste.append(i)
#             else:
#                 lsto.append(i) 
#         print(lste)
#         print(lsto)
#     res(lst)
# even_odd(lst)

# def even(lst):
#     for i in lst:
#         print(i%2 == 0)

# # filter(func,iterable)
# lst = [1,3,2,5,6,8,4,10,12,15,19,85,45,100]

# even = filter(even(),lst)


# my_age = [2,10,6,4,8,7,16,15,13,14,17,21,22]

# def check(x):
#     if x>=18:
#         return True
#     else:
#         return False

# adults = filter(check,my_age)
# # print(adults)
# for x in adults:
#     print(x)



'''
filter(function,iterable)


def func1(num):
    if num>10:
        return True
    else:
        return False
# 11 = True 12 = true 9= false
lst = [2,6,5,8,10,14,65,95]
filter(func1,lst)

# lst = [14,65,95]

'''

# lst = [1,3,2,5,6,8,4,10,12,15,19,85,45,100]

# def even(num):
#     if (num%2 == 0):
#         return True
#     else:
#         return False

# result = filter(even,lst)
# for i in result:
#     print(i)

# string = ["apple","mango","banana"]

# def check_mango(fruit):
#     if fruit == "mango":
#         return True
#     else:
#         return False
# god = filter(check_mango,string)
# for i in god:
#     print(i)


letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

def vowels(letter):
    vowels_val = ["a","e","i","o","u"]
    if letter in vowels_val:
        return True
    else:
        return False


vowel_res = filter(vowels,letters)


# set_1 = (1,2,3,6)
# lst_1 = list(set_1)

# let=['a','b','d','e','i','j','o']

# def vol(ans):
#     vowel=['a','e','i','o','u']
#     if(ans in vowel):
#         return True
#     else:
#         return False
# vol_result=filter(vol,let)
# for i in vol_result:
#     print(i)
