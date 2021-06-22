#Tuple ()
'''
immutable, collection of diff data type
'''

my_tuple = ()  # empty tuple
my_tuple = (1,2,3,"Harry",[1,2,True])

my_int = (1,2,3,4)  #packing
# my_int = 1,2,3,4  #packing
# print(type(my_tuple))

a,b,c,d = my_int

print(c)


lst = ["John"]
# print(type(lst))  # cls<list>



tuple1 = ("John",) # tuple
tuple1 = "John", # tuple
tuple1 = ("John") # str
tuple1 = "John" # str
# print(type(tuple1))

my_tuple = (1,2,3,"Harry",[1,2,True])

# print(my_tuple[0])
# print(my_tuple[4][1])

# print(my_tuple[:3])
# print(my_tuple[::-1])
#[start:end:step]
# my_tuple[0] = "one"
my_tuple[4][2] = False

# print(my_tuple)

# print((1,2,3) + (4,5,6))  # tuple concatenation
# print((1,2)*4)  # tuple concatenation (1,2,1,2,1,2,1,2)
# print(("hello",)*5)
#("hello","hello","hello","hello","hello")

# del my_tuple

# count
my_tuple = (1,2,3,"Harry",2,[1,2,True])

# print("Harry" in my_tuple)

# print(my_tuple.count(1))

# #index
# print(my_tuple.index(2))   #1 / 4 / 1,4


# set {}
'''
immutable , unordered , duplication are not allowed
modify ----- alter
'''
my_set = {5,1,"mumabi","pune","delhi",(1,2,3)}
print(my_set)
my_set = {}
my_set = {1,2,3,4,5}

lst1 = [1,2,3,4]
print(type(lst1))
print(lst1)
mySet = set(lst1)
print(type(mySet))
print(mySet)


# {key:value}   {set}
mySet = {}  
# If you are declaring empty obj with {}    first pref dict then set
mySet = set(mySet)
print(type(mySet))   # class<set>

