
#REPL -----> Read Eval Print Lopp  exit()
#inbuild package and some package you will import from google

# import os  #inbuild packages
# import tensorflow #give the pip command


# data types inside the python
'''
Text data type :  str
Numeric data type : int, float, complex(a) ai+bj
Sequence data type : list, tuple, range
Mapping data type : dict
Set data type : set, frozen set () #make your set as immutable obj
Boolean data type :  bool(True/False) #boolean values/ Boolean data type
Binary data type : bytes, bytearray, memoryview



#inside the set all the values are immutable(cannot change) but your set itself a mutable object(we can add or remove)
{
# set
fruits = {"apple", "mango","cherry"}  #set1
fruits.add("grapes")
#{"apple","mango","grapes","cherry"}  #set2
fruits.remove("apple")
print(fruits)
# print(type(fruits)}

'''

# set
fruits = {"apple", "mango","cherry"}  #set1
fruits = frozenset({"apple", "mango","cherry"}) #frozen set
#print(type(fruits))  # class frozenset
fruits.add("grapes")
#{"apple","mango","grapes","cherry"}  #set2
fruits.remove("apple")
print(fruits)
# print(type(fruits)}

#Binary data type : bytes, bytearray, memoryview

#  1)  byte
x = b"hello world"
print(x)
print(type(x))

string = "I love python"

#utf-8
arr = bytes(string, 'utf-8')
print(arr)

#  2) bytearray    ----> in the form zeros and x(x00/) {0<= x <= 256}
num1 = bytearray(1)
print(num1)
print(type(num1))


#  3)  memory view  ----->takes only the byte obj

num2 = memoryview(bytes(10))
num2 = memoryview(bytearray(5))
print(num2)
print(type(num2))