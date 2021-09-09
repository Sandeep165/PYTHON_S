'''
The 50-30-20 strategy is a simple way to budget, which involves spending 50% of after-tax income on needs, 30% after tax income on wants,
 and 20% after-tax income on savings or paying off debt.

Given the after-tax income as ati, what you are supposed to do is to make a function that will return a dictionary that shows how much 
a person needs to spend on needs, wants, and savings.

Examples
fifty_thirty_twenty(10000) ➞ { "Needs": 5000, "Wants": 3000, "Savings": 2000 }

fifty_thirty_twenty(50000) ➞ { "Needs": 25000, "Wants": 15000, "Savings": 10000 }

fifty_thirty_twenty(13450) ➞ { "Needs": 6725, "Wants": 4035, "Savings": 2690 }


Given a number and a dictionary with min and max properties, return True if the number lies within the given range (inclusive).

Examples
is_in_range(4, { "min": 0, "max": 5 }) ➞ True

is_in_range(4, { "min": 4, "max": 5 }) ➞ True

is_in_range(4, { "min": 6, "max": 10 }) ➞ False

is_in_range(5, { "min": 5, "max": 5 }) ➞ True
Notes
Numbers can be positive or negative, and they may not be integers.
You can assume min <= max is always true.

'''
def fifty_thirty_twenty(ati):
    keys = ["Needs","wants","savings"]
    values = [(ati*0.5),(ati*0.3),(ati*0.2)]

    return dict(zip(keys,values))

print(fifty_thirty_twenty(13450))

'''

Create a function that takes a string of name and checks how much good is the given name. A preloaded dictionary of alphabet scores is
 available in the Code tab. Add up the letters of your name to get the total score.

scores = {"A": 100, "B": 14, "C": 9, "D": 28, "E": 145, "F": 12, "G": 3,
          "H": 10, "I": 200, "J": 100, "K": 114, "L": 100, "M": 25,
          "N": 450, "O": 80, "P": 2, "Q": 12, "R": 400, "S": 113,
          "T": 405, "U": 11, "V": 10, "W": 10, "X": 3, "Y": 210, "Z": 23}
Return your result as per the following rules:

score <= 60:   "NOT TOO GOOD"

61 <= score <= 300:  "PRETTY GOOD"

301 <= score <= 599:  "VERY GOOD"

score >= 600:  "THE BEST"
Examples
name_score("MUBASHIR") ➞ "THE BEST"

name_score("YOU") ➞ "VERY GOOD"

name_score("MATT") ➞ "THE BEST"

name_score("PUBG") ➞ "NOT TOO GOOD"
'''
def goodNames(x):
    sum=0
    scores = {"A": 100, "B": 14, "C": 9, "D": 28, "E": 145, "F": 12, "G": 3,
          "H": 10, "I": 200, "J": 100, "K": 114, "L": 100, "M": 25,
          "N": 450, "O": 80, "P": 2, "Q": 12, "R": 400, "S": 113,
          "T": 405, "U": 11, "V": 10, "W": 10, "X": 3, "Y": 210, "Z": 23}
    for i in x:
        sum=sum+scores.get(i)
    if(sum>=600):
        print("Best")
    if(sum>=301 and sum<=599):
        print("good")
    if(sum>=61 and sum<=300 ):
        print("Preety")
    if(sum<61):
        print("Not so good")


goodNames("SHREESH")


def name_score(n):
    n=n.upper()
    sc=0
    scores = {"A": 100, "B": 14, "C": 9, "D": 28, "E": 145, "F": 12, "G": 3,
          "H": 10, "I": 200, "J": 100, "K": 114, "L": 100, "M": 25,
          "N": 450, "O": 80, "P": 2, "Q": 12, "R": 400, "S": 113,
          "T": 405, "U": 11, "V": 10, "W": 10, "X": 3, "Y": 210, "Z": 23}
    for i in range(len(n)):
        sc=sc+scores[n[i]]

    if sc<=60:
        return "Not So Good"
    elif sc>61 and sc<=300:
        return "Pretty Good"
    elif sc>301 and sc<=599:
        return "very Good"
    elif sc>=600:
        return "The Best"     

print(name_score('harsh'))

def name_score(name):
    my_score= 0
    scores = {"A": 100, "B": 14, "C": 9, "D": 28, "E": 145, "F": 12, "G": 3,
          "H": 10, "I": 200, "J": 100, "K": 114, "L": 100, "M": 25,
          "N": 450, "O": 80, "P": 2, "Q": 12, "R": 400, "S": 113,
          "T": 405, "U": 11, "V": 10, "W": 10, "X": 3, "Y": 210, "Z": 23}
    for letter in name:
        my_score += scores[letter]
    if(my_score <= 60):
        return "NOT TOO GOOD"
    elif(my_score in range(61, 301)):
        return "PRETTY GOOD"
    elif(my_score in range(301, 600)):
        return "VERY GOOD"
    return "THE BEST"


'''

Write a function that converts a dictionary into a list of keys-values tuples.

Examples
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]

dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
'''
# dictionary = {
#     "D":1,
#     "B":2,
#     "C":3}
# dict = dictionary.items()
# lst = list(sorted(dict))

# print(lst)


# def dict_to_list(dict1):
#     ans= []
#     for key in dict1.keys():
#         ans.append((key, dict1[key]))
#     return sorted(ans)
    

# print(dict_to_list({"Likes":2, "Dislikes":3, "followers":10}))



def dict_to_list(dict3):
    return sorted(dict3.items()) 

print(dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}))  

'''


Suppose you have a guest list of students and the country they are from, stored as key-value pairs in a dictionary.

GUEST_LIST = {
"Randy": "Germany",
"Karla": "France",
"Wendy": "Japan",
"Norman": "England",
"Sam": "Argentina"
}
Write a function that takes in a name and returns a name tag, that should read:

"Hi! I'm [name], and I'm from [country]."
If the name is not in the dictionary, return:

"Hi! I'm a guest."


greeting("Sam") ➞ "Hi! I'm Sam, and I'm from Argentina."

greeting("Monti") ➞ "Hi! I'm a guest."

'''

def greet(name):
    GUEST_LIST = {
    "Randy": "Germany",
    "Karla": "France",
    "Wendy": "Japan",
    "Norman": "England",
    "Sam": "Argentina"
    }
    return "Hi! I'm {}, and I'm from {}.".format(name,GUEST_LIST[name]) if name in GUEST_LIST.keys() else "Hi! I'm a guest."
    # if name in GUEST_LIST.keys():
    #     return "Hi! I'm {}, and I'm from {}.".format(name,GUEST_LIST[name])
    # else:
    #     return "Hi! I'm a guest."
print(greet("Sam"))
print(greet("Vishwas"))

# name = "Harry"
# country = "USA"
# print(f"My name is {name} I am from country {country}")
# res = "my name is {name} I am from country {country}".format(name  = "john")