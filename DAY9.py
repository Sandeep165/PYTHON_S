'''
dict : {key:value}
'''
my_dict = {}
# print(type(my_dict))

my_dict = { 1:"one", 2:"two", 3: "three"}
# print(my_dict)

my_dict1 = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : [1,2,3,4],
    5 : (1,2,3,4)
}
# print(my_dict1)

fruits = [(1,"apple"), (2,"mango")]

fruits = dict(fruits)
# print(fruits)


my_dict1 = {
    1 : "bool",
    2 : "two",
    3 : "three",
    4 : [1,2,3,4],
    5 : True,
    6 : "six"
}
my_dict1[5] = True     # updating[key] = ""
# print(my_dict1)

my_dict1[6] = "six"     #adding[6] = "six"
# print(my_dict1)

my_dict1[True] = "bool"  #updating
# print(my_dict1)
# my_dict1[1] = "bool"  #updating
# print(my_dict1)


my_dict2 = {
    1 : "bool",
    2 : "two",
    3 : "three",
    4 : [1,2,3,4],
    5 : True,
    6 : "six"
}

# removing : pop/popitem/clear/del/copy/=
print(my_dict2)
# print(my_dict2.pop(6))     # 
# print(my_dict2)
# print(my_dict2.popitem())  #

# formkey(key,value)  value = vowels
key = {"a","e","i","o","u"} 
value = ["vowel"]
vowels = dict.fromkeys(key,value)
# vowels = dict.fromkeys({"a","e","i","o","u"} ,"vowel")
# value.append("set")


# print(vowels)
my_dict2 = {
    1 : "bool",
    2 : "two",
    3 : "three",
    4 : [1,2,3,4],
    5 : True,
    6 : "six"
}

#key/value
# print(my_dict2.keys())
# print(my_dict2.values())

#get
# print(my_dict2.get(10)) #none
# print(my_dict2[10]) #keyerror

#item
# print(my_dict2.items())

'''
clear()        	Removes all the elements from the dictionary
copy()      	Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''

dict1 = { 1 : 1, 2 : 4, 3 : 9, 4 : 16}

# print(dict1.setdefault(5,25))
# print(dict1)


family = { "Parent1" : { "name" : "John", "age": 21}, "Parent2" : { "name" : "Sam", "age": 22} }

family = {
    "Parent1" : {
        "name" : "John",
        "age"  : 21
    },
    "Parent2" : {
        "name" : "Sam",
        "age"  : 22
    },
    "Parent3" : {
        "name" : {
            1 : "one",
            2 : "two"
        }
    }
}
print(family["Parent1"]["name"])

family["Parent4"] = {}

family["Parent4"]["name"]  = "tom"
family["Parent4"]["age"]  = 15

print(family)




