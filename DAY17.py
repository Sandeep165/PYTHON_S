# lst = [1,2,3,4,5,6,7,-1,-2,-7,-8]

# def max_num(num):
#     if num>1:
#         return True
#     else:
#         return False

#new_lst = >1
# res = list(filter(lambda num: True if (num>1) else False,[1,2,3,4,5,6,7,-1,-2,-7,-8]))

# print(res)
# res =  lambda num: num>1
result = lambda num :  num>1
res = list(filter(result,[1,2,3,4,5,6,7,-1,-2,-7,-8]))
# print(res)

'''
lamda : one line, you dont need to call, take n numbs input

'''
add = lambda a,b: a+b
# print(add(4,6))




def add_num():
    print("hello")

var1 = add_num
var1()
# print(type(var1))



# map
# map(func,iter)

# list1 = [11,12,13,14,15,16,17]

# def inc(num):
#     if num>10:
#         return(num+1)
# # inc(5)

# res1 = list(map(inc,list1))   # same leng
# res2 = list(filter(inc,list1)) # len <= original list
# print(res1)
# print(res2)

# fruits = ["apple","mango","banana","cherry","GRAPES"]
# FRUITS = [...................]

# fruits= ["apple", "orange", "banana", "kiwi"]

# def upper_name(name):
#     return name.upper()

# FRUITS = list(map(upper_name,fruits))
# print(FRUITS)

res = map(lambda x:x.upper(), ["apple","mango","banana","cherry","GRAPES"])
# print(list(res))

#Q1

list1=[1,2,3]
list2=[4,5,6]
x=list(map(lambda a,b:a+b,list1,list2))
# print(x)


# Q2
lst = ["sat","sun"]

op_lst = [["s","a","t"],["s","u","n"]]
frt = list(map(list,lst))
# frt = "Saturday"
# frt = list(frt)
# print(frt)
