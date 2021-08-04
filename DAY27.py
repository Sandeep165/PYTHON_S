'''
Given two strings, return a string containing only the letters shared between the two.

Examples
shared_letters("house", "home") ➞ "eho"

shared_letters("Micky", "mouse") ➞ "m"

shared_letters("house", "villa") ➞ ""
Notes
If none of the letters are shared, return an empty string.
The function should be case insensitive (e.g. comparing A and a should return a).
Sort the resulting string alphabetically before returning it.
'''
def shared(n1,n2):
    val=''
    for i in n1.lower():
        if i in n2.lower():
            val=val+i
    val="".join(sorted(set(val)))   
    return val

print(shared('Aa','Aa'))


def shared(n1,n2):
    return "".join(sorted(set(n1.lower()) & set(n2.lower())))

'''

Given a list and chunk size "n", create a function such that it divides the list into many
sublists where each sublist is of length size "n".
Examples
chunk([1, 2, 3, 4], 2) ➞ [
  [1, 2], [3, 4]
]

chunk([1, 2, 3, 4, 5, 6, 7], 3) ➞ [
  [1, 2, 3], [4, 5, 6], [7]
]

chunk([1, 2, 3, 4 ,5], 10) ➞ [
  [1, 2, 3, 4, 5]
]
Notes
Remember that number of sublists may not be equal to chunk size.

'''

def chunk(lst, size):
    ans= []
    for i in range(0, len(lst), size):
        ans.append(lst[i: i+size])
    return ans

def chunk(lst, size):
    return [lst[i : i+size] for i in range(0,len(lst),size)]   

'''

Create a function that takes an integer list and return the biggest between positive sum, negative sum, or 0s count. The major is understood as the greatest absolute.

l = [1,2,3,4,0,0,-3,-2], the function has to return 10, because:

Positive sum = 1+2+3+4 = 10
Negative sum = (-3)+(-2) = -5
0s count = 2 (there are two zeros in list)
Examples
major_sum([1, 2, 3, 4, 0, 0, -3, -2]) ➞ 10

major_sum([-4, -8, -12, -3, 4, 7, 1, 3, 0, 0, 0, 0]) ➞ -27

major_sum([0, 0, 0, 0, 0, 1, 2, -3]) ➞ 5
# Because -3 < 1+2 < 0sCount = 5
Notes
All numbers are integers.
There aren't empty lists.
All tests are made to return only one value.

'''

def num(lst):
    lst1=[]
    lst2=[]
    lst3=0
    for i in lst:
        if i>0:
            lst1.append(i)
        if i<0:
            lst2.append(i)
        if i==0:
            lst3=lst3+1
    sumadd=0
    summinus=0
    for i in lst1:
        sumadd=sumadd+i
    for i in lst2:
        summinus=summinus+i
    print("addition of positive = ",sumadd )
    print("addition of negative = ",summinus)
    print("No. of zeros =",lst3)

num([1,4,7,-1,-9,-6,0,-5,0,1])


def maxx(lst):
    positive, negative,zero = 0,0,0
    for i in lst:
        if i>0:
            positive += i
        elif i<0:
            negative += i

        else:
            zero += i
        return max(positive,negative,zero , key= abs)