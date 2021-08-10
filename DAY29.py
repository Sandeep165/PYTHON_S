'''
Start each sentence with an uppercase alphabet.
For every uppercase letter (other than the first alphabet), you have to place a fullstop(.) followed by an empty space.
There must be only one space between the words and sentences.
Sentence must end with a full stop(.)
Two continuous spaces are not allowed.
correct_sentences ("  mubashir loves  edabit  Matt  loves  edabit  ") ➞ "Mubashir loves edabit. Matt loves edabit."

# Remove extra spaces.
# Capitalise first character.
# Dot followed by an empty space before "Matt".
# A dot at the end.

'''
def correct_sentences(sentence):
    sentence = " ".join(sentence.split())
    ans= sentence.split(" ")
    for i in range(1, len(ans)):
        if(ans[i][0].isupper()):
            ans[i-1] += "."
    ans[-1] += "."
    ans[0]= ans[0].replace(ans[0], ans[0].capitalize())
    return " ".join(ans)


print(correct_sentences ("  mubashir loves  edabit  Matt  loves  edabit  "))


'''
Abigail and Benson are playing Rock, Paper, Scissors.

Each game is represented by an array of length 2, where the first element represents what Abigail played and 
the second element represents what Benson played.

Given a sequence of games, determine who wins the most number of matches. If they tie, output "Tie".

R stands for Rock
P stands for Paper
S stands for Scissors
Examples
calculate_score([["R", "P"], ["R", "S"], ["S", "P"]]) ➞ "Abigail"

# Benson wins the first game (Paper beats Rock).
# Abigail wins the second game (Rock beats Scissors).
# Abigail wins the third game (Scissors beats Paper). 
# Abigail wins 2/3.

calculate_score([["R", "R"], ["S", "S"]]) ➞ "Tie"

calculate_score([["S", "R"], ["R", "S"], ["R", "R"]]) ➞ "Tie"
'''

def calculate_score(lst):
    ref= {'P':'R', 'R':'S', 'S':'P'}
    a= 0; b= 0
    for case in lst:
        if(ref[case[0]] == case[1]):
            a += 1
        elif(ref[case[1]] == case[0]):
            b += 1
    return 'Abigail' if a > b else 'Benson' if a < b else 'Tie'

print(calculate_score([['S', 'R'], ['P', 'R']]))


'''


Imagine you have three numbers: a, b, and c. c is equal to either a or b, but you don't know which one. 
Your task is to create a function that returns whatever number c isn't, out of a and b. So, if c is equal to a,
 return b, and if c is equal to b, return a. Here's what makes this challenge difficult: you cannot use any if statements.

Examples
swap(1, 0, 0) ➞ 1
# a = 1, b = 0, c = b
# return a

swap(1, 3, 1) ➞ 3
# a = 1, b = 3, c = a
# return b

swap(27, 31, 31) ➞ 27
# a = 27, b = 31, c = b
# return a
Notes
To prevent cheating, you also can't call any functions.
c will always be equal to either a or b.
a will never equal b.
a, b, and c will always be integers
'''
def swap(a, b, c):
    return (a+b+c)-(2*c)

print(swap(27, 31, 31))


def swap(a, b, c):
    return a if c== b else b

print(swap(27, 31, 31))
