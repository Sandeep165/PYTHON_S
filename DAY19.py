#join()
lst = ["john","sam","cooper"]
'''
john#sam#cooper

'''
# print(lst)
# print(type(lst))
# res = "#".join(lst)
# print(res)
# print(type(res))

mydict = {
    "name" : "Sam",
    "age"   : 21,
    "one" : 1
}

var1 = "Test"
res1 = var1.join(mydict)
# print(res1)

#Head->1->2->3->4.....30->Tail
lst2 = ["Head","1","2","3","45","6","9","82","4","30","Tails"]


s = "->"
ans = s.join(lst2)
# print(ans)

lst_num = [1,2,3,4,5]
lst_str = ["1","2","3","4","5"]
lst_str = []
# print(lst_str)
# def change_str(lst):
#     for i in lst_num:
#         # print(i)
#         lst_str.append(str(i))

# change_str(lst_num)

lst_str = list(map(str,lst_num))
# print(lst_str)

str1 = ["s","a","n","d","e","e","p"]
ans1 = "".join(str1)
# print(ans1)
#sandeep
#SANDEEP

mydict = {
    "name" : "Sam",
    "age"   : 21,
    "one" : 1,
    True : "true",
    "5" : "five"
}

# var1 = "Test"
# res1 = var1.join(mydict)
# print(res1)


num = [1,2,3,4,5]
# print(num)
num_square= list(map(lambda x : x*x,num))
# print(num_square)

# sun_diff = [(2,0),(6,-2),(12,-6),(20,-12),(30,-20)]
sum_diff = list(map(lambda x,y: ((x+y),(x-y)), num,num_square))

# print(sum_diff)

#swap a,b
num1 = 15
num2 = 20
print(num1,num2)

#method 1
num1,num2 = num2,num1

#method2
temp = num1
num1 = num2
num2 = temp

#method3
num1 = num1 + num2 #35
num2 = num1 - num2 #15
num1 = num1 - num2 #20

#method4
num1 = num1 * num2 #35
num2 = num1 / num2 #15
num1 = num1 / num2 #20

#method5
# num1 = num1 ^  num2 #35
# num2 = num1 ^ num2 #15
# num1 = num1 ^ num2 #20

'''

Sum of Evenly Divisible Numbers from a Range

Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.

Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20 = 0

evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30

evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
'''
def evenly_divisible(a,b,c):
    return sum(i for i in range(a,b+1) if i%c == 0)
print(evenly_divisible(1, 10, 3)) 



def ques(a,b,c):
    l=[]
    for x in range(a,b+1,c):
        l.append(x)
    return sum(l)
# print(ques(1,50,7))

