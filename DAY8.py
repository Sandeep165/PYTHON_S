
#  dataset = [ 1,2,3,4]                     dataset = [1,2,3,4,5]           #modify (add,remove,update,pop)
#  datset1 = ["one","two","three"]          dataset1 = ["one",2,"three"]    #alter (dataset[1]="")

# add/update
fruits = {"apple", "mango", "banana"}
fruits.add("grapes")
# print(fruits)

# fruits = {"apple","mango","banana","apple"}
# print(fruits)
# fruits.update([1,2,3,4])

a = [1, 2, 3, 4]
fruits.update(a)
# print(fruits)

# pop/remove
# fruits.pop()
# fruits.remove("mango")
# print(fruits)


# clear/copy
# fruits.clear()
# print(fruits)
# print(type(fruits))

new_set = fruits.copy()

# print(new_set)
# print(fruits)


# set_int = {1,2,3}

# new = set_int.copy()
# print(new)
# print(set_int)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = set1.intersection(set2)
# set3 = set1.union(set2)
print(set3)


'''

add()	                 Adds an element to the set
clear() 	             Removes all the elements from the set
copy()	                 Returns a copy of the set
difference()	         Returns a set containing the difference between two or more sets
difference_update()             	Removes the items in this set that are also included in another, specified set
discard()	                          Remove the specified item
intersection()         	            Returns a set, that is the intersection of two other sets
intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                  Returns whether two sets have a intersection or not
issubset()	                     Returns whether another set contains this set or not
issuperset()	                Returns whether this set contains another set or not
pop()	                         Removes an element from the set
remove()	                     Removes the specified element
symmetric_difference()      	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                        Return a set containing the union of sets
update()	                    Update the set with the union of this set and others
'''
f = {"apple", "mango", "cherry", "facebook"}
c = {"apple", "facebook"}
# f.intersection_update(c)
# print(f)
let = {"a", "b", "c", "f", "e"}
let1 = {1, 2, 3}

# res = let1.issuperset(let1)
res = let.isdisjoint(let1)
# print(res)


# frozenset

vowels = ("a", "e", "i", "o", "u")
# print(vowels)
vowels = set(vowels)
# print(vowels)

# vowels.add("z")
# print(vowels)

vowels = frozenset(vowels)
# print(vowels)
# vowels.add("a")


#range
print(range(8))

print(type(range))
