L = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], ['g'], 'h']
# ddd  ff [g] h  (+ve/-ve)

# print(L[1][1][1]) #ddd
# print(L[1][3]) #ff
# print(L[2][0]) #g
# print(L[3]) #h

# print (L[-3][-3][-1], L[-3][-1], L[-2][-1], L[-1])

# append/insert push the value

L1 = [1,2,3,4]
print(L1)
# L1.append([2,4,6])
# print(L1)

# L1.insert(7,[1,3,5])
# print(L1)

#clear/count
# print(L1.count(10))

# L1.clear()
# print(L1)
my_list = [0,1,2,3,"Pune","Mumbai","Pune",True,False,15.5,1,2,3]
# print(my_list.count(0)) #
# copy/reverse
# cpy = my_list.copy()
cpy = my_list
cpy.append("Delhi")

print(my_list)
print(cpy)


#pop/remove
# print(my_list.pop(4))
my_list.remove("Pune")
print(my_list)


'''
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''

new_list = [5,4,2,1,8,10,4,11]
# new_list = ["apple","aaple","cherry","grapes","banana"]
new_list.sort(reverse=True)
print(new_list)



# List

# for i in range(1,10,2):
#     print(i)

# list1 = [x for x in new_list if x == 5]

fruits = ["apple","banana","cheery","grapes"]
f1 = []
print(f1)
# for i in fruits:
#     if "e" in i:
#         f1.append(i)
# print(f1)

f1 = [i.upper() for i in fruits ]
print(f1)

# integer = [i  for i in range(11) if i>5]
# print(integer)

sqr = [i*i for i in range(10)]
# for i in range(10):
#     sqr.append(i*i)
print(sqr)