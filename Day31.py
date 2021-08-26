'''
Create a function that takes two strings as arguments and return either True or False depending on whether the total number of
characters in the first string is equal to the total number of characters in the second string.

Examples
comp("AB", "CD") ➞ "True"

comp("ABC", "DE") ➞ "False"

comp("hello", "edabit") ➞ "False"

def comp(n1,n2):
    c1,c2=0,0
    for i in n1:
        c1+=1
    for i in n2:
        c2+=1
    
    if(c1==c2):
        return True
    else:
        return False

print(comp('Ab','ab'))



Write a function that takes a string and calculates the number of letters and digits within it. Return the result in a dictionary.

Examples
count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }

count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }

count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }




def count_all(given_str):
    ref= {
        "LETTERS": 0,
        "DIGITS": 0
    }
    for letter in given_str:
        if(letter.isdigit()):
            ref["DIGITS"] += 1
        if(letter.isalpha()):
            ref["LETTERS"] += 1
    return ref

print(count_all("H3llo World"))


clone list
clone([1, 1]) ➞ [1, 1, [1, 1]]

clone([1, 2, 3]) ➞ [1, 2, 3, [1, 2, 3]]

clone(["x", "y"]) ➞ ["x", "y", ["x", "y"]]

def clone_lst(lst):

    lst.append(list(lst1))
    return lst

print(clone_lst([1,1])


def clone_list(lst):
    lst.append([element for element in lst])
    return lst

print(clone_list([1, 2, 3, 4]))


Create a function that takes a string as an argument and returns a coded (h4ck3r 5p34k) version of the string.

Examples
hacker_speak("javascript is cool") ➞ "j4v45cr1pt 15 c00l"

hacker_speak("programming is fun") ➞ "pr0gr4mm1ng 15 fun"

hacker_speak("become a coder") ➞ "b3c0m3 4 c0d3r"
Notes
In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5.


def hacker_speak(given_str):
    ref= {
        "a": "4",
        "e": "3",
        "i": "1",
        'o': "0",
        "u": "5"
    }
    for letter in given_str:
        if(letter in ref):
            given_str= given_str.replace(letter, ref[letter])
    return given_str


print(hacker_speak("Javascript is cool"))



Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects
 like { "name": "John", "top_note": 5 }.

Examples
top_note({ "name": "John", "notes": [3, 5, 4] }) ➞ { "name": "John", "top_note": 5 }

top_note({ "name": "Max", "notes": [1, 4, 6] }) ➞ { "name": "Max", "top_note": 6 }

top_note({ "name": "Zygmund", "notes": [1, 2, 3] }) ➞ { "name": "Zygmund", "top_note": 3 }
'''
def replace1(str1):
    return str1.replace("a","4").replace("e","3").replace("i","1").replace("o","0").replace("u","5")


def top_note(dict1):
    dict1["top_note"]= dict1.pop("notes")
    temp= dict1["top_note"]
    dict1["top_note"]= sorted(temp)[-1]
    return dict1

print(top_note({"name": "John", "notes": [7, 4, 6]}))



def top_note(n):
    n['notes']=max(n['notes'])
    n['top_note']=n['notes']
    del n['notes']
    return n

print(top_note({'name':'Harsh','notes' :[1,2,3,4]}))

